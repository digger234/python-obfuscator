import asyncio
import hashlib
import json
import math
import os
import platform
import random
import re
import signal
import socket
import subprocess
import sys
import threading
import time
import traceback
import msvcrt
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta
from tkinter import Tk, filedialog
from urllib.parse import urlparse
from threading import Lock
import aiohttp
import colorama
import httpx
import psutil
import requests
from colorama import Fore, Style
from rich.align import Align
from rich.box import DOUBLE_EDGE, ROUNDED
from rich.console import Console, Group
from rich.live import Live
from rich.padding import Padding
from rich.panel import Panel
from rich.progress import (Progress, SpinnerColumn, TextColumn, BarColumn,
                          TaskProgressColumn, TimeElapsedColumn)
from rich.style import Style as RichStyle
from rich.table import Table
from rich.text import Text

try:
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
except:
    pass

def check_and_install_dependencies():
    required_packages = {
        'httpx': 'httpx',
        'colorama': 'colorama',
        'rich': 'rich',
        'psutil': 'psutil',
        'aiohttp': 'aiohttp',
        'socksio': 'socksio',
        'httpx-socks': 'httpx_socks',
        'requests': 'requests'
    }

    console.print("[cyan]Đang kiểm tra thư viện...[/cyan]")
    for package, import_name in required_packages.items():
        try:
            __import__(import_name)
            console.print(f"[green]✓ {package} đã được cài đặt[/green]")
        except ImportError:
            console.print(f"[yellow]Đang cài đặt {package}...[/yellow]")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                console.print(f"[green]✓ Đã cài đặt thành công {package}[/green]")
            except subprocess.CalledProcessError:
                console.print(f"[red]❌ Không thể cài đặt {package}[/red]")
                console.print(f"[yellow]⚠️  Vui lòng cài đặt thủ công bằng lệnh: [bright_white]pip install {package}[/bright_white][/yellow]")
                sys.exit(1)
    console.print("[green]Tất cả thư viện đã được cài đặt![/green]")

console = Console()
check_and_install_dependencies()
colorama.init(autoreset=True)


PROXY_LINE_RE = re.compile(r'^\d{1,3}(?:\.\d{1,3}){3}:\d+$')

def create_async_client_with_proxy(proxy_config=None, **kwargs):
    try:
        cfg = {}
        if 'headers' not in kwargs or not kwargs.get('headers'):
            kwargs['headers'] = {'User-Agent': random.choice(cfg.get('user_agents', [
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36'
            ]))}
        if 'verify' not in kwargs:
            kwargs['verify'] = cfg.get('http_verify', False)
        if 'http2' not in kwargs:
            kwargs['http2'] = cfg.get('http2', False)
        if 'limits' not in kwargs:
            kwargs['limits'] = httpx.Limits(max_connections=100, max_keepalive_connections=50, keepalive_expiry=15.0)
        t = kwargs.get('timeout', None)
        if not isinstance(t, httpx.Timeout):
            ct = cfg.get('connect_timeout', 3)
            rt = cfg.get('read_timeout', 6)
            wt = cfg.get('write_timeout', 5)
            pt = cfg.get('pool_timeout', 3)
            kwargs['timeout'] = httpx.Timeout(connect=ct, read=max(rt, t) if isinstance(t, (int, float)) else rt, write=wt, pool=pt)
        if proxy_config:
            if isinstance(proxy_config, str):
                proxy_config = {"http://": proxy_config, "https://": proxy_config}
            transport = httpx.AsyncHTTPTransport(proxies=proxy_config, retries=2)
            return httpx.AsyncClient(transport=transport, **kwargs)
        return httpx.AsyncClient(**kwargs)
    except Exception as e:
        return None

def get_current_directory():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))


def load_user_settings():
    settings_file = os.path.join(get_current_directory(), "user_settings.json")
    if os.path.exists(settings_file):
        try:
            with open(settings_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {}
    return {}

def save_user_settings(settings):
    settings_file = os.path.join(get_current_directory(), "user_settings.json")
    try:
        with open(settings_file, 'w', encoding='utf-8') as f:
            json.dump(settings, f, indent=2, ensure_ascii=False)
        return True
    except (IOError, OSError):
        return False

def create_rainbow_text_animated(text, time_offset=0):
    rainbow_text = Text()
    for i, char in enumerate(text):
        pos = 0.3 * i + time_offset
        r = int(127 * (math.sin(pos) + 1))
        g = int(127 * (math.sin(pos + 2*math.pi/3) + 1))
        b = int(127 * (math.sin(pos + 4*math.pi/3) + 1))
        color_code = f"rgb({r},{g},{b})"
        rainbow_text.append(char)
        rainbow_text.stylize(color_code, i, i+1)
    return rainbow_text

def create_rainbow_text(text):
    return create_rainbow_text_animated(text, 0)

def enlarge_text(text, factor=2):
    try:
        if factor <= 1:
            return text
        pieces = []
        for ch in text:
            if ch == ' ':
                pieces.append(' ' * max(1, factor - 1))
            else:
                pieces.append(ch * factor)
        return ''.join(pieces)
    except Exception:
        return text

def create_gradient_border():
    return "bright_red"

def clear_screen():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    show_header()

class ProxyManager:
    def __init__(self):
        self.config = {}
        self.proxies_db = {}
        self.load_database()
        self.cleanup_old_records()

    def load_database(self):
        db_path = os.path.join(get_current_directory(), 'proxy_db.json')
        if os.path.exists(db_path):
            try:
                with open(db_path, 'r', encoding='utf-8') as f:
                    self.proxies_db = json.load(f)
            except (json.JSONDecodeError, IOError):
                self.proxies_db = {}

    def save_database(self):
        db_path = os.path.join(get_current_directory(), 'proxy_db.json')
        try:
            with open(db_path, 'w', encoding='utf-8') as f:
                json.dump(self.proxies_db, f, indent=4)
            return True
        except (IOError, OSError):
            return False

    def add_proxy(self, proxy_url, info):
        if proxy_url not in self.proxies_db:
            self.proxies_db[proxy_url] = {
                'added': datetime.now().isoformat(),
                'last_check': None,
                'checks': [],
                'fail_count': 0,
                'cooldown_until': None,
                'tempban_until': None
            }
        for k in ['fail_count','cooldown_until','tempban_until']:
            if k not in self.proxies_db[proxy_url]:
                self.proxies_db[proxy_url][k] = 0 if k == 'fail_count' else None
        self.proxies_db[proxy_url].update(info)
        self.save_database()

    def get_proxy_info(self, proxy_url):
        return self.proxies_db.get(proxy_url, {})

    def update_proxy_check(self, proxy_url, check_result):
        if proxy_url in self.proxies_db:
            now = datetime.now()
            rec = self.proxies_db[proxy_url]
            rec['last_check'] = now.isoformat()
            rec.setdefault('checks', [])
            rec['checks'].append({'time': now.isoformat(), 'result': check_result})
            if len(rec['checks']) > 10:
                rec['checks'] = rec['checks'][-10:]
            rec.setdefault('fail_count', 0)
            rec.setdefault('cooldown_until', None)
            rec.setdefault('tempban_until', None)
            cur_h = int(check_result.get('health_score', 0) or 0)
            alpha = 0.3
            prev = rec.get('ema_health')
            if prev is None:
                rec['ema_health'] = cur_h
            else:
                try:
                    rec['ema_health'] = int(alpha * cur_h + (1 - alpha) * int(prev))
                except (ValueError, TypeError) as e:
                    rec['ema_health'] = cur_h
            err = str(check_result.get('error', '') or '')
            if err in ('cooldown_active', 'tempban_active'):
                self.save_database()
                return
            status = check_result.get('status')
            cfg = {}
            if status == 'working':
                rec['fail_count'] = 0
                rec['tempban_until'] = None
                cd = int(cfg.get('cooldown_success_seconds', 8))
                rec['cooldown_until'] = (now + timedelta(seconds=cd)).isoformat()
            elif status == 'slow':
                rec['fail_count'] = max(0, int(rec.get('fail_count', 0)) - 1)
                cd = int(cfg.get('cooldown_success_seconds', 8))
                rec['cooldown_until'] = (now + timedelta(seconds=cd)).isoformat()
            else:
                rec['fail_count'] = int(rec.get('fail_count', 0)) + 1
                if any(x in err for x in ['429', '403']):
                    tb = int(cfg.get('cooldown_tempban_seconds', 60))
                    rec['tempban_until'] = (now + timedelta(seconds=tb)).isoformat()
                th = int(cfg.get('fail_threshold', 3))
                if rec['fail_count'] >= th:
                    cd = int(cfg.get('cooldown_fail_seconds', 20))
                    rec['cooldown_until'] = (now + timedelta(seconds=cd)).isoformat()
            self.save_database()

    def get_favorites(self):
        return []

    def add_to_favorites(self, proxy_url):
        pass

    def remove_from_favorites(self, proxy_url):
        pass

    def is_blacklisted(self, proxy_url):
        return False

    def add_to_blacklist(self, proxy_url):
        pass

    def cleanup_old_records(self, days=30):
        cutoff = datetime.now() - timedelta(days=days)
        for proxy in list(self.proxies_db.keys()):
            last_check = self.proxies_db[proxy].get('last_check')
            if last_check:
                last_check = datetime.fromisoformat(last_check)
                if last_check < cutoff:
                    del self.proxies_db[proxy]
        self.save_database()

def center_text(text, width=80):
    return text.center(width)

def rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

reset = "\033[0m"

def get_yes_no_input(message):
    while True:
        choice = console.input(f"{message} [white]").strip().lower()
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            console.print(f"[red]Vui lòng trả lời 'y' (có) hoặc 'n' (không)![/red]")
async def ping_host(host_or_hostport, timeout=1.0):
    try:
        target = host_or_hostport.strip()

        for scheme in ("http://", "https://", "socks4://", "socks5://"):
            if target.lower().startswith(scheme):
                target = target[len(scheme):]
                break

        if "@" in target:
            target = target.split("@", 1)[1]

        if ":" in target:
            host, port_str = target.rsplit(":", 1)
            try:
                port = int(port_str)
            except ValueError:
                port = 80
        else:
            host, port = target, 80
        start = time.time()
        _, writer = await asyncio.wait_for(asyncio.open_connection(host, port), timeout=timeout)
        try:
            if not writer.is_closing():
                writer.close()
                await writer.wait_closed()
            await writer.wait_closed()
        except RuntimeError as e:
            pass
        return (time.time() - start) * 1000
    except (OSError, asyncio.TimeoutError):
        return None
class ProxyCollector:
    def __init__(self, console_instance):
        self.sources = {

            'proxyscrape_http': 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http',
            'proxyscrape_socks4': 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4',
            'proxyscrape_socks5': 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5',
            'proxy-list-http': 'https://www.proxy-list.download/api/v1/get?type=http',
            'proxy-list-https': 'https://www.proxy-list.download/api/v1/get?type=https',
            'thespeedx_http': 'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
            'thespeedx_socks4': 'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt',
            'thespeedx_socks5': 'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt'
        }
        self.console = console_instance

    async def collect_from_source(self, url):
        cfg = {}
        try:
            client = create_async_client_with_proxy(None, follow_redirects=True)
            if not client:
                return set()
            async with client:
                domain_rate_limiter.wait(url)
                response = await client.get(url, timeout=cfg.get('read_timeout', 6))
                if response.status_code == 200:
                    content = response.text
                    proxies = set()
                    for line in content.split('\n'):
                        s = line.strip()
                        if PROXY_LINE_RE.match(s):
                            proxies.add(s)
                    return proxies
        except (httpx.RequestError, httpx.TimeoutException) as e:
            pass
        return set()

    async def collect_all(self):
        self.console.print("[bold yellow]Bắt đầu quá trình lấy proxy...[/bold yellow]")
        tasks = []
        for url in self.sources.values():
            tasks.append(self.collect_from_source(url))

        results = await asyncio.gather(*tasks)
        all_proxies = set()
        for proxy_set in results:
            if proxy_set:
                all_proxies.update(proxy_set)

        self.console.print(f"[bold yellow]Hoàn tất. Tổng số proxy thu được: {len(all_proxies)}[/bold yellow]")
        return list(all_proxies)
def scale_ascii_art(text, h_scale=2, w_scale=2):
    scaled_lines = []
    for line in text.split('\n'):
        widened = ''.join(ch * w_scale for ch in line)
        for _ in range(h_scale):
            scaled_lines.append(widened)
    return '\n'.join(scaled_lines)

def show_header():
    header_art = """
██████╗ ██████╗  ██████╗ ██╗  ██╗██╗   ██╗    ███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗
██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝    ████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
██████╔╝██████╔╝██║   ██║ ╚███╔╝  ╚████╔╝     ██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝
██╔═══╝ ██╔══██╗██║   ██║ ██╔██╗   ╚██╔╝      ██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗
██║     ██║  ██║╚██████╔╝██╔╝ ██╗   ██║       ██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝

🌟🌟🌟 PROXY MASTER - ENTERPRISE EDITION 🌟🌟🌟
🚀 Made by: yeppp 🚀
    """
    lines = header_art.strip().split('\n')
    for line in lines:
        if line.strip():
            if "PROXY MASTER" in line:
                console.print(Panel(create_rainbow_text(line.replace("PROXY MASTER - ENTERPRISE EDITION", "PROXY  MASTER  -  ENTERPRISE  EDITION")), border_style="bright_red", box=DOUBLE_EDGE, padding=(0, 2)), justify="center")
            else:
                rainbow_line = create_rainbow_text(line)
                console.print(rainbow_line, justify="center")
        else:
            console.print()
    console.print()

def show_header_rich():
    show_header()
def select_proxy_file():
    root = Tk()
    root.attributes('-topmost', True)
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="CHỌN FILE PROXY CẦN CHECK",
        filetypes=[("Tệp văn bản", "*.txt")]
    )
    root.destroy()
    return file_path

def validate_proxy_file(filename):
    try:
        with open(filename, 'r') as f:
            proxies = [line.strip() for line in f if line.strip()]
        if proxies:
            console.print(f"\n[green]✓ File hợp lệ! Tìm thấy {len(proxies)} proxy.[/green]")
            return True
        console.print(f"\n[red]✗ File không chứa proxy hợp lệ![/red]")
        return False
    except Exception:
        console.print(f"\n[red]✗ Không thể đọc file![/red]")
        return False

def find_file_in_common_dirs(filename):
    home_dir = os.path.expanduser('~')
    common_dirs = ['Desktop', 'Documents', 'Downloads']
    for directory in common_dirs:
        path = os.path.join(home_dir, directory, filename)
        if os.path.exists(path):
            console.print(f"[green]✓ Tìm thấy file tại: {path}[/green]")
            return path
    return None


def validate_proxy_format(proxy):
    auth_pattern = r'^([^:]+):([^@]+)@(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})$'
    basic_pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})$'

    auth_match = re.match(auth_pattern, proxy)
    if auth_match:
        ip_parts = auth_match.group(3).split('.')
        port = int(auth_match.group(4))
    else:
        basic_match = re.match(basic_pattern, proxy)
        if not basic_match:
            return False
        ip_parts = basic_match.group(1).split('.')
        port = int(basic_match.group(2))

    for part in ip_parts:
        if int(part) > 255:
            return False

    if port > 65535:
        return False

    return True

def parse_proxy_auth(proxy_url):
    if not proxy_url or not isinstance(proxy_url, str):
        return {'proxy': '', 'auth': None, 'has_auth': False, 'error': 'Invalid input'}
    try:
        clean_url = proxy_url
        original_protocol = None
        for protocol in ['http://', 'https://', 'socks4://', 'socks5://']:
            if clean_url.lower().startswith(protocol):
                original_protocol = protocol
                clean_url = clean_url[len(protocol):]
                break

        auth_pattern = r'^([^:]+):([^@]+)@(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})$'
        auth_match = re.match(auth_pattern, clean_url)

        if auth_match:
            username = auth_match.group(1)
            password = auth_match.group(2)
            ip = auth_match.group(3)
            port = auth_match.group(4)

            if not validate_ip(ip):
                return {'proxy': proxy_url, 'auth': None, 'has_auth': False, 'error': 'Invalid IP address'}
            if not validate_port(port):
                return {'proxy': proxy_url, 'auth': None, 'has_auth': False, 'error': 'Invalid port'}

            return {
                'proxy': f"{ip}:{port}",
                'auth': (username, password),
                'has_auth': True,
                'ip': ip,
                'port': port,
                'protocol': original_protocol or 'http://',
                'error': None
            }

        basic_pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})$'
        basic_match = re.match(basic_pattern, clean_url)
        if basic_match:
            ip = basic_match.group(1)
            port = basic_match.group(2)

            if not validate_ip(ip):
                return {'proxy': proxy_url, 'auth': None, 'has_auth': False, 'error': 'Invalid IP address'}
            if not validate_port(port):
                return {'proxy': proxy_url, 'auth': None, 'has_auth': False, 'error': 'Invalid port'}

            return {
                'proxy': f"{ip}:{port}",
                'auth': None,
                'has_auth': False,
                'ip': ip,
                'port': port,
                'protocol': original_protocol or 'http://',
                'error': None
            }

    except (re.error, AttributeError) as e:
        return {'proxy': proxy_url, 'auth': None, 'has_auth': False, 'error': f'Parsing error: {str(e)}'}

    return {'proxy': proxy_url, 'auth': None, 'has_auth': False, 'error': 'Invalid proxy format'}

def validate_ip(ip):
    try:
        if not isinstance(ip, str):
            return False
        parts = ip.split('.')
        if len(parts) != 4:
            return False
        return all(part.isdigit() and 0 <= int(part) <= 255 for part in parts)
    except (ValueError, AttributeError, TypeError):
        return False

def validate_port(port):
    try:
        port_num = int(port)
        return 0 < port_num <= 65535
    except (ValueError, TypeError):
        return False

def input_proxies_manually():
    console.print(f"\n[cyan]Nhập proxy thủ công[/cyan]")
    console.print("[yellow]Định dạng: ip:port (ví dụ: 127.0.0.1:8080)[/yellow]")
    console.print("[yellow]Mỗi proxy trên một hàng, nhập xong để trống và nhấn Enter để kết thúc:[/yellow]")
    lines = []
    while True:
        line = console.input(f"[white]> ").strip()
        if not line:
            break
        lines.append(line)
    proxies = []
    invalid_proxies = []

    for i, line in enumerate(lines, 1):
        proxy = line.strip()
        if proxy:
            if validate_proxy_format(proxy):
                proxies.append(proxy)
            else:
                invalid_proxies.append(f"Dòng {i}: {proxy}")

    if invalid_proxies:
        console.print(f"\n[red]✗ Các proxy không hợp lệ:[/red]")
        for invalid in invalid_proxies:
            console.print(f"[red]  - {invalid}[/red]")

        if proxies:
            console.print(f"\n[yellow]Tìm thấy {len(proxies)} proxy hợp lệ và {len(invalid_proxies)} proxy không hợp lệ.[/yellow]")
            continue_choice = get_yes_no_input(f"[cyan]Bạn muốn tiếp tục với các proxy hợp lệ? (y/n):[/cyan]")
            if not continue_choice:
                return []
        else:
            console.print(f"\n[red]Không có proxy hợp lệ nào![/red]")
            return []

    if proxies:
        console.print(f"\n[green]✓ Đã nhập thành công {len(proxies)} proxy hợp lệ:[/green]")
        for i, proxy in enumerate(proxies[:10], 1):
            console.print(f"[white]  {i}. {proxy}[/white]")

        if len(proxies) > 10:
            console.print(f"[yellow]  ... và {len(proxies) - 10} proxy khác[/yellow]")

        confirm = get_yes_no_input(f"\n[cyan]Xác nhận sử dụng các proxy này? (y/n):[/cyan]")
        if confirm:
            return proxies

    return []

class RateLimiter:
    def __init__(self, max_requests_per_second=10, burst_size=None, window_size=60):
        self.max_requests = max_requests_per_second
        self.burst_size = burst_size or max_requests_per_second * 2
        self.window_size = window_size
        self.requests = []
        self.lock = threading.Lock()
        self.total_requests = 0
        self.window_start = time.time()
        self.consecutive_failures = 0
        self.last_failure_time = 0
        self.adaptive_rate = max_requests_per_second
        self.response_times = []
        self.burst_detected = False
        self.burst_start_time = 0

    def update_response_time(self, response_time_ms):
        with self.lock:
            self.response_times.append((time.time(), response_time_ms))
            self.response_times = [(t, rt) for t, rt in self.response_times if time.time() - t < 30]

            if len(self.response_times) >= 5:
                avg_response = sum(rt for _, rt in self.response_times) / len(self.response_times)
                if avg_response > 2000:
                    self.adaptive_rate = max(1, self.adaptive_rate * 0.8)
                elif avg_response < 500:
                    self.adaptive_rate = min(self.max_requests * 2, self.adaptive_rate * 1.1)

    def record_failure(self):
        with self.lock:
            now = time.time()
            if now - self.last_failure_time < 5:
                self.consecutive_failures += 1
            else:
                self.consecutive_failures = 1
            self.last_failure_time = now

    def record_success(self):
        with self.lock:
            self.consecutive_failures = max(0, self.consecutive_failures - 1)

    def get_backoff_delay(self):
        if self.consecutive_failures == 0:
            return 0
        return min(30, 0.5 * (2 ** min(self.consecutive_failures, 6)))

    def detect_burst(self):
        now = time.time()
        recent_requests = [t for t in self.requests if now - t < 5]

        if len(recent_requests) > self.max_requests * 3:
            if not self.burst_detected:
                self.burst_detected = True
                self.burst_start_time = now
            return True
        elif self.burst_detected and now - self.burst_start_time > 30:
            self.burst_detected = False

        return self.burst_detected

    def wait_if_needed(self):
        with self.lock:
            now = time.time()

            if now - self.window_start >= self.window_size:
                self.total_requests = 0
                self.window_start = now

            self.requests = [req_time for req_time in self.requests if now - req_time < 1.0]

            backoff_delay = self.get_backoff_delay()
            if backoff_delay > 0:
                time.sleep(backoff_delay)
                now = time.time()

            if self.detect_burst():
                current_limit = max(1, int(self.adaptive_rate * 0.5))
            else:
                current_limit = int(self.adaptive_rate)

            if len(self.requests) >= current_limit:
                sleep_time = 1.0 - (now - self.requests[-current_limit])
                if sleep_time > 0:
                    time.sleep(sleep_time)
                    now = time.time()

            self.requests.append(now)
            self.total_requests += 1

rate_limiter = RateLimiter(max_requests_per_second=15, window_size=60)

class DomainRateLimiter:
    def __init__(self, cfg):
        self.cfg = cfg
        self.map = {}
        self.lock = threading.Lock()
        self.domain_stats = {}

    def _host(self, url):
        try:
            netloc = urlparse(url).netloc
            if not netloc:
                return None
            return netloc.split(':')[0]
        except Exception:
            return None

    def update_domain_performance(self, url, response_time_ms, success):
        host = self._host(url)
        if not host:
            return

        with self.lock:
            if host not in self.domain_stats:
                self.domain_stats[host] = {'response_times': [], 'success_rate': 1.0, 'total_requests': 0, 'successful_requests': 0}

            stats = self.domain_stats[host]
            stats['total_requests'] += 1
            if success:
                stats['successful_requests'] += 1
                stats['response_times'].append((time.time(), response_time_ms))
                stats['response_times'] = [(t, rt) for t, rt in stats['response_times'] if time.time() - t < 300]

            stats['success_rate'] = stats['successful_requests'] / stats['total_requests']

            limiter = self.map.get(host)
            if limiter:
                if success:
                    limiter.record_success()
                    limiter.update_response_time(response_time_ms)
                else:
                    limiter.record_failure()

    def wait(self, url):
        host = self._host(url)
        if not host:
            return

        limit_cfg = self.cfg.get('per_domain_rate_limit', {})
        base_rate = limit_cfg.get(host, 10)

        with self.lock:
            stats = self.domain_stats.get(host, {})
            success_rate = stats.get('success_rate', 1.0)

            adaptive_rate = base_rate
            if success_rate < 0.8:
                adaptive_rate = max(1, int(base_rate * 0.5))
            elif success_rate > 0.95:
                adaptive_rate = min(base_rate * 2, int(base_rate * 1.5))

            limiter = self.map.get(host)
            if not limiter:
                limiter = RateLimiter(max_requests_per_second=adaptive_rate, window_size=60)
                self.map[host] = limiter
            else:
                limiter.adaptive_rate = adaptive_rate

        limiter.wait_if_needed()

domain_rate_limiter = DomainRateLimiter({})

class LRUCache:
    def __init__(self, max_size=1000, ttl_seconds=3600):
        self.max_size = max_size
        self.ttl_seconds = ttl_seconds
        self.cache = {}
        self.access_order = []
        self.lock = threading.Lock()
        self.hit_count = 0
        self.miss_count = 0

    def _cleanup_expired(self):
        now = time.time()
        expired_keys = [k for k, (_, timestamp, _) in self.cache.items() if now - timestamp > self.ttl_seconds]
        for key in expired_keys:
            self._remove_key(key)

    def _remove_key(self, key):
        if key in self.cache:
            del self.cache[key]
        if key in self.access_order:
            self.access_order.remove(key)

    def _move_to_end(self, key):
        if key in self.access_order:
            self.access_order.remove(key)
        self.access_order.append(key)

    def get(self, key, default=None):
        with self.lock:
            self._cleanup_expired()
            if key in self.cache:
                value, timestamp, access_count = self.cache[key]
                self.cache[key] = (value, timestamp, access_count + 1)
                self._move_to_end(key)
                self.hit_count += 1
                return value
            else:
                self.miss_count += 1
                return default

    def put(self, key, value):
        with self.lock:
            now = time.time()
            self._cleanup_expired()

            if key in self.cache:
                self.cache[key] = (value, now, self.cache[key][2])
                self._move_to_end(key)
            else:
                if len(self.cache) >= self.max_size:
                    oldest_key = self.access_order[0]
                    self._remove_key(oldest_key)

                self.cache[key] = (value, now, 1)
                self.access_order.append(key)

    def invalidate(self, key):
        with self.lock:
            self._remove_key(key)

    def clear(self):
        with self.lock:
            self.cache.clear()
            self.access_order.clear()
            self.hit_count = 0
            self.miss_count = 0

    def get_stats(self):
        with self.lock:
            total_requests = self.hit_count + self.miss_count
            hit_rate = self.hit_count / total_requests if total_requests > 0 else 0
            return {
                'size': len(self.cache),
                'max_size': self.max_size,
                'hit_rate': hit_rate,
                'hit_count': self.hit_count,
            }

class CacheManager:
    def __init__(self):
        self.geo_cache = LRUCache(max_size=50000, ttl_seconds=86400)
        self.perf_cache = LRUCache(max_size=100000, ttl_seconds=7200)
        self.dns_cache = LRUCache(max_size=10000, ttl_seconds=7200)
        self.warmup_queue = []
        self.warmup_lock = threading.Lock()
        self.warmup_thread = None
        self.start_warmup_thread()
    def start_warmup_thread(self):
        if self.warmup_thread is None or not self.warmup_thread.is_alive():
            self.warmup_thread = threading.Thread(target=self._warmup_worker, daemon=True)
            self.warmup_thread.start()

    def _warmup_worker(self):
        while True:
            try:
                with self.warmup_lock:
                    if not self.warmup_queue:
                        time.sleep(5)
                        continue
                    key, cache_type, fetch_func = self.warmup_queue.pop(0)

                if cache_type == 'geo':
                    if self.geo_cache.get(key) is None:
                        try:
                            value = fetch_func()
                            if value:
                                self.geo_cache.put(key, value)
                        except Exception:
                            pass
                elif cache_type == 'perf':
                    if self.perf_cache.get(key) is None:
                        try:
                            value = fetch_func()
                            if value:
                                self.perf_cache.put(key, value)
                        except Exception:
                            pass

                time.sleep(0.1)
            except Exception:
                time.sleep(1)

    def schedule_warmup(self, key, cache_type, fetch_func):
        with self.warmup_lock:
            if len(self.warmup_queue) < 100:
                self.warmup_queue.append((key, cache_type, fetch_func))

    def get_geo_info(self, ip):
        return self.geo_cache.get(ip)

    def put_geo_info(self, ip, info):
        self.geo_cache.put(ip, info)

    def get_perf_info(self, proxy):
        return self.perf_cache.get(proxy)

    def put_perf_info(self, proxy, info):
        self.perf_cache.put(proxy, info)

    def get_dns_info(self, hostname):
        return self.dns_cache.get(hostname)

    def put_dns_info(self, hostname, ip):
        self.dns_cache.put(hostname, ip)

    def get_all_stats(self):
        return {
            'geo_cache': self.geo_cache.get_stats(),
            'perf_cache': self.perf_cache.get_stats(),
            'dns_cache': self.dns_cache.get_stats(),
            'warmup_queue_size': len(self.warmup_queue)
        }

cache_manager = CacheManager()

def _validate_ip_response(content):
    if not content:
        return None
    
    content = content.strip()
    
    ip_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if not re.match(ip_pattern, content):
        return None
    
    try:
        parts = content.split('.')
        if len(parts) != 4:
            return None
        for part in parts:
            num = int(part)
            if num < 0 or num > 255:
                return None
        
        import ipaddress
        ip = ipaddress.ip_address(content)
        if ip.is_loopback or ip.is_multicast:
            return None
        
        return content
    except:
        return None

async def _test_proxy_common_async(proxy_url, timeout=3, max_response_time=20000):
    try:
        start_time = time.time()
        
        test_urls = [
            'http://icanhazip.com',
            'http://api.ipify.org',
            'http://ident.me'
        ]
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': '*/*'
        }
        
        async with httpx.AsyncClient(
            proxies={'http://': proxy_url, 'https://': proxy_url},
            timeout=timeout,
            verify=True,
            headers=headers,
            follow_redirects=True,
            limits=httpx.Limits(max_connections=100, max_keepalive_connections=50)
        ) as client:
            tasks = [client.get(url) for url in test_urls]
            responses = await asyncio.gather(*tasks, return_exceptions=True)
            
            for response in responses:
                if isinstance(response, httpx.Response) and response.status_code == 200:
                    validated_ip = _validate_ip_response(response.text)
                    if validated_ip:
                        rt = int((time.time() - start_time) * 1000)
                        if rt < max_response_time:
                            return validated_ip, rt
    except:
        pass
    return None, None

def _test_proxy_common(proxy_url, timeout=5, max_response_time=20000):
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    
    return loop.run_until_complete(_test_proxy_common_async(proxy_url, timeout, max_response_time))

async def detect_proxy_anonymity(proxy_url, timeout=5):
    try:
        async with httpx.AsyncClient(
            proxies={'http://': proxy_url, 'https://': proxy_url},
            timeout=timeout,
            verify=True
        ) as client:
            response = await client.get('http://httpbin.org/headers')
            if response.status_code == 200:
                headers = response.json().get('headers', {})
                
                leak_headers = ['X-Forwarded-For', 'X-Real-Ip', 'Via', 'Forwarded', 'Client-Ip']
                has_leak = any(h in headers for h in leak_headers)
                
                if has_leak:
                    if 'Via' in headers or 'X-Forwarded-For' in headers:
                        return 'transparent'
                    return 'anonymous'
                return 'elite'
    except:
        pass
    return 'unknown'

async def test_proxy_enhanced(proxy_url, max_retries=2, rate_limiter=None):
    ip, rt = _test_proxy_common(proxy_url)
    if ip and rt:
        return ip, '?', rt
    return None, None, None

def detect_proxy_type(proxy_url):
    if not proxy_url or not isinstance(proxy_url, str):
        return "http"

    proxy_lower = proxy_url.lower()
    proxy_types = {
        "socks5://": "socks5",
        "socks4://": "socks4",
        "https://": "https"
    }

    for prefix, ptype in proxy_types.items():
        if proxy_lower.startswith(prefix):
            return ptype
    return "http"

def build_httpx_proxies(proxy_url, forced_type=None):
    try:
        info = parse_proxy_auth(proxy_url)
        if not info or info.get('error'):
            return None
        ptype = forced_type or detect_proxy_type(proxy_url)

        scheme = 'http' if ptype == 'http' else ('https' if ptype == 'https' else ptype)
        if info.get('has_auth') and info.get('auth'):
            user, pwd = info['auth']
            value = f"{scheme}://{user}:{pwd}@{info['proxy']}"
        else:
            value = f"{scheme}://{info['proxy']}"

        return {
            'http://': value,
            'https://': value
        }
    except Exception:
        return None

async def test_proxy(proxy_url):
    if not proxy_url:
        return None, None, None

    try:
        ip, country, response_time = await test_proxy_enhanced(proxy_url, rate_limiter=rate_limiter)
        if ip and response_time >= 0:
            return ip, country or "?", response_time
    except (httpx.RequestError, httpx.TimeoutException) as e:
        pass

    return None, None, None

def test_proxy_sync(proxy_url):
    ip, rt = _test_proxy_common(proxy_url)
    if ip and rt:
                try:
                    loop = asyncio.get_event_loop()
                    if loop.is_running():
                        with ThreadPoolExecutor() as executor:
                            future = executor.submit(asyncio.run, get_detailed_geolocation(ip))
                            geo_data = future.result(timeout=5)
                    else:
                        geo_data = asyncio.run(get_detailed_geolocation(ip))
                    
                    if geo_data:
                        country = geo_data.get('country_code', '??')
                    else:
                        country = '??'
                except:
                    country = '??'
                
                return ip, country, rt
    return None, None, None

async def get_detailed_geolocation(ip, rate_limiter=None):
    try:
        if not ip:
            return None
        cfg = {}
        ttl = cfg.get('geo_cache_ttl', 600)
        now = time.time()
        entry = cache_manager.get_geo_info(ip)
        if entry and (now - entry.get('ts', 0) <= ttl):
            return entry.get('data')

        apis = [
            f"http://ip-api.com/json/{ip}?fields=status,country,countryCode,region,city,isp,org,as,proxy,hosting",
            f"https://ipapi.co/{ip}/json/"
        ]

        async with httpx.AsyncClient(timeout=httpx.Timeout(connect=cfg.get('connect_timeout',3), read=cfg.get('read_timeout',6), write=cfg.get('write_timeout',5), pool=cfg.get('pool_timeout',3))) as client:
            for api_url in apis:
                try:
                    if rate_limiter:
                        rate_limiter.wait_if_needed()
                    domain_rate_limiter.wait(api_url)
                    response = await client.get(api_url)
                    if response.status_code == 200:
                        data = response.json()

                        if "status" in data and data["status"] == "success":
                            result = {
                                "country": data.get("country", "Không rõ"),
                                "country_code": data.get("countryCode", "??"),
                                "city": data.get("city", "Không rõ"),
                                "region": data.get("region", "Không rõ"),
                                "isp": data.get("isp", "Không rõ"),
                                "org": data.get("org", "Không rõ"),
                                "is_proxy": data.get("proxy", False),
                                "is_hosting": data.get("hosting", False),
                                "anonymity": "Elite" if not data.get("proxy", False) else "Transparent"
                            }
                            cache_manager.put_geo_info(ip, {"ts": now, "data": result})
                            return result

                        elif "country_name" in data:
                            result = {
                                "country": data.get("country_name", "Không rõ"),
                                "country_code": data.get("country_code", "??"),
                                "city": data.get("city", "Không rõ"),
                                "region": data.get("region", "Không rõ"),
                                "isp": data.get("org", "Không rõ"),
                                "org": data.get("org", "Không rõ"),
                                "is_proxy": False,
                                "is_hosting": False,
                                "anonymity": "Anonymous"
                            }
                            cache_manager.put_geo_info(ip, {"ts": now, "data": result})
                            return result

                except (httpx.RequestError, httpx.TimeoutException, json.JSONDecodeError):
                    continue

        fallback = {
            "country": "Không rõ",
            "country_code": "??",
            "city": "Không rõ",
            "region": "Không rõ",
            "isp": "Không rõ",
            "org": "Không rõ",
            "is_proxy": False,
            "is_hosting": False,
            "anonymity": "Không rõ"
        }
        cache_manager.put_geo_info(ip, {"ts": now, "data": fallback})
        return fallback

    except (httpx.RequestError, httpx.TimeoutException):
        return None

def get_optimal_thread_count():
    cpu_count = psutil.cpu_count(logical=True)
    return cpu_count * 4

print_lock = threading.Lock()

class CustomBarColumn(BarColumn):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.colors = [
            "#ff0000", "#ff7f00", "#ffff00", "#00ff00",
            "#0000ff", "#4b0082", "#9400d3"
        ]
        self.color_index = 0

    def render(self, task) -> Text:
        if task.total is None:
            return Text()

        if task.finished:
            self.complete_style = "bold bright_green"
            return super().render(task)

        self.color_index = (self.color_index + 1) % len(self.colors)
        self.pulse_style = RichStyle(color=self.colors[self.color_index])
        return super().render(task)

def create_rich_progress():
    return Progress(
        SpinnerColumn(spinner_name="dots", style="bold bright_cyan"),
        TextColumn("[bold cyan]🔍 Đang kiểm tra proxy...[/bold cyan]"),
        CustomBarColumn(bar_width=50, style="grey50", finished_style="bold bright_green"),
        TaskProgressColumn(),
        TimeElapsedColumn(),
        console=console
    )


def show_proxy_statistics(total, live, dead):

    stats_table = Table(title=create_rainbow_text("📊 Thống Kê Proxy"), show_header=True, header_style="bold blue",
                       border_style="bold bright_blue", box=DOUBLE_EDGE, highlight=True)

    stats_table.add_column("Loại", style="cyan", width=15)
    stats_table.add_column("Số Lượng", style="green", width=10, justify="center")
    stats_table.add_column("Tỷ Lệ", style="yellow", width=10, justify="center")

    live_rate = (live / total * 100) if total > 0 else 0
    dead_rate = (dead / total * 100) if total > 0 else 0

    stats_table.add_row("Tổng Proxy", f"{total:,}", "100%")
    stats_table.add_row("Proxy Sống", f"[green]{live:,}[/green]", f"[green]{live_rate:.1f}%[/green]")
    stats_table.add_row("Proxy Chết", f"[red]{dead:,}[/red]", f"[red]{dead_rate:.1f}%[/red]")

    console.print(stats_table)

def check_proxies(proxies, classify, classify_type, output_path, max_threads):
    def _is_valid_proxy(p):
        if not isinstance(p, str):
            return False
        p = p.strip()
        if not p:
            return False
        info = parse_proxy_auth(p)
        return info and not info.get('error')

    original_count = len(proxies)
    proxies = [p.strip() for p in proxies if _is_valid_proxy(p)]
    removed = original_count - len(proxies)
    if removed > 0:
        console.print(f"[yellow]Đã loại {removed} dòng không hợp lệ khỏi danh sách proxy.[/yellow]")
    
    proxies = list(dict.fromkeys(proxies))

    results = []
    live_proxies = []
    classified_proxies = {
        "socks4": {}, "socks5": {}, "http": {}, "https": {}
    }

    async def process_proxy_async(proxy, client):
        try:
            info = parse_proxy_auth(proxy)
            if not info or info.get('error'):
                return None

            ip = info.get('ip')
            port = int(info.get('port', 0) or 0)
            if not ip or not port:
                return None

            def check_socket():
                s = None
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(1.0)
                    return s.connect_ex((ip, port)) == 0
                except:
                    return False
                finally:
                    if s:
                        try:
                            s.close()
                        except:
                            pass
            
            loop = asyncio.get_event_loop()
            is_open = await loop.run_in_executor(None, check_socket)
            if not is_open:
                return None

            start_time = time.time()
            proxy_dict = {'http': proxy, 'https': proxy}
            test_hosts = [
                'http://icanhazip.com',
                'http://api.ipify.org',
                'http://ident.me'
            ]

            for i, url in enumerate(test_hosts):
                try:
                    response = await client.get(url, proxies=proxy_dict, timeout=3.0, follow_redirects=False)
                    if response.status_code in (200, 204, 301, 302):
                        rt = int((time.time() - start_time) * 1000)
                        
                        validated_ip = _validate_ip_response(response.text)
                        if not validated_ip:
                            return None
                        
                        try:
                            geo_data = await get_detailed_geolocation(ip)
                            country = geo_data.get('country_code', '?') if geo_data else '?'
                        except:
                            country = '?'
                        
                        anonymity = 'unknown'
                        try:
                            anonymity = await detect_proxy_anonymity(proxy, timeout=2)
                        except:
                            pass
                        
                        return (proxy, ip, country, rt, anonymity)
                except Exception:
                    if i < 2:
                        continue
                    else:
                        break
        except Exception:
            pass
        return None

    async def run_check():
        async with httpx.AsyncClient(
            limits=httpx.Limits(max_connections=max_threads, max_keepalive_connections=max(50, max_threads // 10)),
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'Accept': '*/*'
            },
            verify=True
        ) as client:
            semaphore = asyncio.Semaphore(max_threads)
            
            async def check_with_sem(proxy):
                async with semaphore:
                    return await process_proxy_async(proxy, client)
            
            batch_size = max_threads * 20
            with create_rich_progress() as progress:
                task = progress.add_task("[cyan]Đang kiểm tra proxy...", total=len(proxies))
                
                for i in range(0, len(proxies), batch_size):
                    batch = proxies[i:i + batch_size]
                    batch_results = await asyncio.gather(*[check_with_sem(p) for p in batch], return_exceptions=True)
                    
                    for result in batch_results:
                        if result and not isinstance(result, Exception):
                            results.append(result)
                            proxy, _, country, response_time, anonymity = result
                            anon_label = ''
                            if anonymity == 'elite':
                                anon_label = ' [Elite]'
                            elif anonymity == 'anonymous':
                                anon_label = ' [Anon]'
                            elif anonymity == 'transparent':
                                anon_label = ' [Trans]'
                            live_proxies.append(f"{proxy} | {response_time}ms{anon_label}")
                            if classify:
                                proxy_type = "http"
                                if proxy.startswith("socks4://"): proxy_type = "socks4"
                                elif proxy.startswith("socks5://"): proxy_type = "socks5"
                                elif proxy.startswith("https://"): proxy_type = "https"
                                if country not in classified_proxies[proxy_type]:
                                    classified_proxies[proxy_type][country] = []
                                classified_proxies[proxy_type][country].append((proxy, response_time, anonymity))
                        progress.advance(task)
    
    asyncio.run(run_check())

    if not results:
        console.print(f"\n[red]✗ Không có proxy nào sống! Không có file nào được xuất ra.[/red]")
        return results

    with open(output_path, "a", encoding='utf-8') as f:
        if f.tell() > 0:
            f.write("\n")
        output_lines = []
        for proxy, _, _, rt, anonymity in results:
            anon_label = ''
            if anonymity == 'elite':
                anon_label = ' [Elite]'
            elif anonymity == 'anonymous':
                anon_label = ' [Anon]'
            elif anonymity == 'transparent':
                anon_label = ' [Trans]'
            output_lines.append(f"{proxy} | {rt}ms{anon_label}")
        f.write("\n".join(output_lines))

    if classify:
        if classify_type == '1':
            country_file_path = os.path.join(get_current_directory(), "proxy_live_country.txt")
            with open(country_file_path, "a", encoding='utf-8') as f:
                if os.path.exists(country_file_path) and os.path.getsize(country_file_path) > 0:
                    f.write("\n")
                for proxy_type, countries in classified_proxies.items():
                    for country, proxy_list in countries.items():
                        if proxy_list:
                            f.write(f"[{country}]\n")
                            for proxy, resp_time, anonymity in proxy_list:
                                anon_label = ''
                                if anonymity == 'elite':
                                    anon_label = ' [Elite]'
                                elif anonymity == 'anonymous':
                                    anon_label = ' [Anon]'
                                elif anonymity == 'transparent':
                                    anon_label = ' [Trans]'
                                f.write(f"{proxy} | {resp_time}ms{anon_label}\n")
                            f.write("\n")
            console.print(f"[green]✓ Đã lưu proxy phân loại theo quốc gia: {country_file_path}[/green]")

        elif classify_type == '2':
            for proxy_type, countries in classified_proxies.items():
                proxy_list = []
                for country, plist in countries.items():
                    proxy_list.extend(plist)
                if proxy_list:
                    type_file_path = os.path.join(get_current_directory(), f"proxy_live_{proxy_type}.txt")
                    with open(type_file_path, "a", encoding='utf-8') as f:
                        if os.path.exists(type_file_path) and os.path.getsize(type_file_path) > 0:
                            f.write("\n")
                        output_lines = []
                        for proxy, resp_time, anonymity in proxy_list:
                            anon_label = ''
                            if anonymity == 'elite':
                                anon_label = ' [Elite]'
                            elif anonymity == 'anonymous':
                                anon_label = ' [Anon]'
                            elif anonymity == 'transparent':
                                anon_label = ' [Trans]'
                            output_lines.append(f"{proxy} | {resp_time}ms{anon_label}")
                        f.write("\n".join(output_lines))
                    console.print(f"[green]✓ Đã lưu proxy {proxy_type}: {type_file_path}[/green]")

        elif classify_type == '3':
            country_file_path = os.path.join(get_current_directory(), "proxy_live_country.txt")
            with open(country_file_path, "a", encoding='utf-8') as f:
                if os.path.exists(country_file_path) and os.path.getsize(country_file_path) > 0:
                    f.write("\n")
                for proxy_type, countries in classified_proxies.items():
                    for country, proxy_list in countries.items():
                        if proxy_list:
                            f.write(f"{country}:\n")
                            for proxy, resp_time, anonymity in proxy_list:
                                anon_label = ''
                                if anonymity == 'elite':
                                    anon_label = ' [Elite]'
                                elif anonymity == 'anonymous':
                                    anon_label = ' [Anon]'
                                elif anonymity == 'transparent':
                                    anon_label = ' [Trans]'
                                f.write(f"{proxy} | {resp_time}ms{anon_label}\n")
                            f.write("\n")
            console.print(f"[green]✓ Đã lưu proxy phân loại theo quốc gia: {country_file_path}[/green]")

            for proxy_type, countries in classified_proxies.items():
                proxy_list = []
                for country, plist in countries.items():
                    proxy_list.extend(plist)
                if proxy_list:
                    type_file_path = os.path.join(get_current_directory(), f"proxy_live_{proxy_type}.txt")
                    with open(type_file_path, "a", encoding='utf-8') as f:
                        if os.path.exists(type_file_path) and os.path.getsize(type_file_path) > 0:
                            f.write("\n")
                        output_lines = []
                        for proxy, resp_time, anonymity in proxy_list:
                            anon_label = ''
                            if anonymity == 'elite':
                                anon_label = ' [Elite]'
                            elif anonymity == 'anonymous':
                                anon_label = ' [Anon]'
                            elif anonymity == 'transparent':
                                anon_label = ' [Trans]'
                            output_lines.append(f"{proxy} | {resp_time}ms{anon_label}")
                        f.write("\n".join(output_lines))
                    console.print(f"[green]✓ Đã lưu proxy {proxy_type}: {type_file_path}[/green]")

    return results

def show_rainbow_message(message, duration=1):
    rainbow_text = create_rainbow_text(message.strip())
    console.print(rainbow_text, justify="center")
    time.sleep(duration)

def show_success_animation(message):
    success_msg = f"✨ {message} ✨"
    rainbow_text = create_rainbow_text(success_msg)

    console.print(Panel(
        rainbow_text,
        border_style="bold bright_green",
        padding=(1, 2),
        box=DOUBLE_EDGE,
        highlight=True
    ), justify="center")
    time.sleep(1)

def show_error_animation(message):
    error_msg = f"❌ {message} ❌"

    console.print(Panel(
        f"[bold bright_red]{error_msg}[/bold bright_red]",
        border_style="bold bright_red",
        padding=(1, 2),
        box=DOUBLE_EDGE,
        highlight=True
    ), justify="center")
    time.sleep(1)

async def get_latest_commit_from_all_repos_async():
    repos = [
        "mzyui/proxy-list",
        "TheSpeedX/PROXY-List",
        "roosterkid/openproxylist",
        "clarketm/proxy-list",
        "hookzof/socks5_list",
        "proxifly/free-proxy-list",
        "fate0/proxylist",
        "FifzzSENZE/Master-Proxy",
        "sunny9577/proxy-scraper",
        "ShiftyTR/Proxy-List",
        "monosans/proxy-list",
        "prxchk/proxy-list",
        "ALIILAPRO/Proxy",
        "almroot/proxylist",
        "aslisk/proxyhttps",
        "B4RC0DE-TM/proxy-list",
        "rdavydov/proxy-list",
        "jetkai/proxy-list",
        "ObcbO/getproxy",
        "opsxcq/proxy-list",
        "ProxyScraper/ProxyScraper",
        "Volodichev/proxy-list",
        "zevtyardt/proxy-list",
        "UserR3X/proxy-list",
        "ErcinDedeoglu/proxies",
        "officialputuid/KangProxy",
        "Zaeem20/FREE_PROXIES_LIST",
        "zloi-user/hideip.me",
        "MuRongPIG/Proxy-Master",
        "Anonym0usWork1221/Free-Proxies",
        "vakhov/fresh-proxy-list",
        "TheSpeedX/SOCKS-List",
        "im-razvan/proxy_list",
        "caliphdev/Proxy-List",
        "saisuiu/Lionkings-Http-Proxys-Proxies",
        "proxy4parsing/proxy-list",
        "MrMarble/proxy-list",
        "yemixzy/proxy-list",
        "Vann-Dev/proxy-list",
        "tuanminpay/live-proxy",
        "UptimerBot/proxy-list",
        "rx443/proxy-list",
        "TylerAmesIsGay/proxy-list",
        "casals-ar/proxy-list",
        "mmpx12/proxy-list",
        "SoliSpirit/proxy-list"
    ]

    latest_time = None
    successful_checks = 0

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/vnd.github.v3+json'
        }
        
        connector = aiohttp.TCPConnector(limit=50, limit_per_host=10, ssl=False)
        timeout = aiohttp.ClientTimeout(total=25, connect=10)
        
        async with aiohttp.ClientSession(headers=headers, connector=connector, timeout=timeout) as session:
            semaphore = asyncio.Semaphore(10)
            
            async def check_repo(repo):
                async with semaphore:
                    try:
                        url = f"https://api.github.com/repos/{repo}/commits?per_page=1"
                        async with session.get(url) as response:
                            if response.status == 200:
                                data = await response.json()
                                if data and len(data) > 0 and 'commit' in data[0]:
                                    commit_date = data[0]['commit']['author']['date']
                                    utc_time = datetime.fromisoformat(commit_date.replace('Z', '+00:00'))
                                    return utc_time
                    except asyncio.TimeoutError:
                        return None
                    except Exception:
                        return None
                    return None

            tasks = [check_repo(repo) for repo in repos]
            results = await asyncio.gather(*tasks, return_exceptions=True)

            for result in results:
                if isinstance(result, datetime) and result:
                    successful_checks += 1
                    if latest_time is None or result > latest_time:
                        latest_time = result
                        
    except Exception:
        pass

    if latest_time and successful_checks > 0:
        vn_time = latest_time + timedelta(hours=7)
        return vn_time.strftime("%Y-%m-%d %I:%M:%S %p (GMT+7)")
    
    return "Không xác định"

async def get_file_hash_async(url, session):
    try:
        async with session.head(url, timeout=30) as response:
            etag = response.headers.get('etag', '')
            last_modified = response.headers.get('last-modified', '')
            return hashlib.md5(f"{etag}{last_modified}".encode()).hexdigest()
    except (aiohttp.ClientError, asyncio.TimeoutError):
        return None

def load_session_data():
    cache_file = os.path.join(get_current_directory(), "proxy_session_data.cache")
    if os.path.exists(cache_file):
        try:
            with open(cache_file, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {}
    return {}

def save_session_data(data):
    cache_file = os.path.join(get_current_directory(), "proxy_session_data.cache")
    with open(cache_file, 'w') as f:
        json.dump(data, f)

def reset_session_data():
    cache_file = os.path.join(get_current_directory(), "proxy_session_data.cache")
    if os.path.exists(cache_file):
        os.remove(cache_file)


def rotate_sources(sources, rotation_key="default"):
    current_hour = int(time.time() // 3600)
    seed = hashlib.md5(f"{rotation_key}_{current_hour}".encode()).hexdigest()
    rotation_offset = int(seed[:8], 16) % len(sources)
    return sources[rotation_offset:] + sources[:rotation_offset]

def get_proxy_urls_with_rotation():
    base_urls = get_proxy_urls_static()
    rotated_urls = {}
    for category, urls in base_urls.items():
        rotated_urls[category] = rotate_sources(urls, f"proxy_{category}")
    return rotated_urls

def get_proxy_urls_static():
    return {
        'all': [
            'https://raw.githubusercontent.com/mzyui/proxy-list/refs/heads/main/all.txt',
            'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
            'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt',
            'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt',
            'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt',
            'https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS.txt',
            'https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4.txt',
            'https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5.txt',
            'https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt',
            'https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all.txt',
            'https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list',
            'https://vakhov.github.io/fresh-proxy-list/proxylist.txt',
            'https://raw.githubusercontent.com/antoinevastel/avastel-bot-ips-lists/master/avastel-proxy-bot-ips-1day.txt',
            'https://raw.githubusercontent.com/antoinevastel/avastel-bot-ips-lists/master/avastel-proxy-bot-ips-blocklist-5days.txt',
            'https://raw.githubusercontent.com/antoinevastel/avastel-bot-ips-lists/master/avastel-proxy-bot-ips-blocklist-8days.txt',
            'https://raw.githubusercontent.com/FifzzSENZE/Master-Proxy/master/proxies/all.txt',
            'https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt',
            'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/proxy.txt',
            'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/all.txt',
            'https://raw.githubusercontent.com/prxchk/proxy-list/main/all.txt',
            'https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/proxy.txt',
            'https://raw.githubusercontent.com/almroot/proxylist/master/list.txt',
            'https://raw.githubusercontent.com/aslisk/proxyhttps/main/https.txt',
            'https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/HTTP.txt',
            'https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/all.txt',
            'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt',
            'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt',
            'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt',
            'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt',
            'https://raw.githubusercontent.com/ObcbO/getproxy/master/http.txt',
            'https://raw.githubusercontent.com/ObcbO/getproxy/master/https.txt',
            'https://raw.githubusercontent.com/ObcbO/getproxy/master/socks4.txt',
            'https://raw.githubusercontent.com/ObcbO/getproxy/master/socks5.txt',
            'https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt',
            'https://raw.githubusercontent.com/opsxcq/proxy-list/master/list_http.txt',
            'https://raw.githubusercontent.com/opsxcq/proxy-list/master/list_https.txt',
            'https://raw.githubusercontent.com/opsxcq/proxy-list/master/list_socks4.txt',
            'https://raw.githubusercontent.com/opsxcq/proxy-list/master/list_socks5.txt',
            'https://raw.githubusercontent.com/ProxyScraper/ProxyScraper/master/proxies.txt',
            'https://raw.githubusercontent.com/ProxyScraper/ProxyScraper/master/proxies-http.txt',
            'https://raw.githubusercontent.com/ProxyScraper/ProxyScraper/master/proxies-https.txt',
            'https://raw.githubusercontent.com/ProxyScraper/ProxyScraper/master/proxies-socks4.txt',
            'https://raw.githubusercontent.com/ProxyScraper/ProxyScraper/master/proxies-socks5.txt',
            'https://raw.githubusercontent.com/Volodichev/proxy-list/main/http.txt',
            'https://raw.githubusercontent.com/Volodichev/proxy-list/main/https.txt',
            'https://raw.githubusercontent.com/Volodichev/proxy-list/main/socks4.txt',
            'https://raw.githubusercontent.com/Volodichev/proxy-list/main/socks5.txt',
            'https://raw.githubusercontent.com/zevtyardt/proxy-list/main/http.txt',
            'https://raw.githubusercontent.com/zevtyardt/proxy-list/main/https.txt',
            'https://raw.githubusercontent.com/zevtyardt/proxy-list/main/socks4.txt',
            'https://raw.githubusercontent.com/zevtyardt/proxy-list/main/socks5.txt',
            'https://raw.githubusercontent.com/UserR3X/proxy-list/main/http.txt',
            'https://raw.githubusercontent.com/UserR3X/proxy-list/main/https.txt',
            'https://raw.githubusercontent.com/UserR3X/proxy-list/main/socks4.txt',
            'https://raw.githubusercontent.com/UserR3X/proxy-list/main/socks5.txt',
            'https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt',
            'https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt',
            'https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt',
            'https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/http.txt',
            'https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/https.txt',
            'https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/socks4.txt',
            'https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/socks5.txt',
            'https://raw.githubusercontent.com/officialputuid/KangProxy/main/http/http.txt',
            'https://raw.githubusercontent.com/officialputuid/KangProxy/main/https/https.txt',
            'https://raw.githubusercontent.com/officialputuid/KangProxy/main/socks4/socks4.txt',
            'https://raw.githubusercontent.com/officialputuid/KangProxy/main/socks5/socks5.txt',
            'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt',
            'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/https.txt',
            'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks4.txt',
            'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks5.txt',
            'https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt',
            'https://raw.githubusercontent.com/zloi-user/hideip.me/main/https.txt',
            'https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt',
            'https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt',
            'https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt',
            'https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks4.txt',
            'https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks5.txt',
            'https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/http_proxies.txt',
            'https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/https_proxies.txt',
            'https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/socks4_proxies.txt',
            'https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/socks5_proxies.txt',
            'https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt',
            'https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/https.txt',
            'https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt',
            'https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt',
            'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt',
            'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt',
            'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt',
            'https://raw.githubusercontent.com/hookzof/socks5_list/master/tg/mtproto.txt',
            'https://raw.githubusercontent.com/hookzof/socks5_list/master/tg/socks.txt',
            'https://raw.githubusercontent.com/im-razvan/proxy_list/main/http.txt',
            'https://raw.githubusercontent.com/caliphdev/Proxy-List/master/http.txt',
            'https://raw.githubusercontent.com/caliphdev/Proxy-List/master/socks4.txt',
            'https://raw.githubusercontent.com/caliphdev/Proxy-List/master/socks5.txt',
            'https://raw.githubusercontent.com/saisuiu/Lionkings-Http-Proxys-Proxies/main/free.txt',
            'https://raw.githubusercontent.com/saisuiu/Lionkings-Http-Proxys-Proxies/main/cnfree.txt',
            'https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt',
            'https://raw.githubusercontent.com/MrMarble/proxy-list/main/all.txt',
            'https://raw.githubusercontent.com/yemixzy/proxy-list/main/proxies/http.txt',
            'https://raw.githubusercontent.com/yemixzy/proxy-list/main/proxies/socks4.txt',
            'https://raw.githubusercontent.com/yemixzy/proxy-list/main/proxies/socks5.txt',
            'https://raw.githubusercontent.com/Vann-Dev/proxy-list/main/proxies/http.txt',
            'https://raw.githubusercontent.com/Vann-Dev/proxy-list/main/proxies/https.txt',
            'https://raw.githubusercontent.com/Vann-Dev/proxy-list/main/proxies/socks4.txt',
            'https://raw.githubusercontent.com/Vann-Dev/proxy-list/main/proxies/socks5.txt',
            'https://raw.githubusercontent.com/tuanminpay/live-proxy/master/http.txt',
            'https://raw.githubusercontent.com/tuanminpay/live-proxy/master/socks4.txt',
            'https://raw.githubusercontent.com/tuanminpay/live-proxy/master/socks5.txt',
            'https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt',
            'https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt',
            'https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt',
            'https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTP_RAW.txt',
            'https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/http.txt',
            'https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/socks4.txt',
            'https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/socks5.txt',
            'https://raw.githubusercontent.com/rx443/proxy-list/main/online/http.txt',
            'https://raw.githubusercontent.com/rx443/proxy-list/main/online/https.txt',
            'https://raw.githubusercontent.com/rx443/proxy-list/main/online/socks4.txt',
            'https://raw.githubusercontent.com/rx443/proxy-list/main/online/socks5.txt',
            'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt',
            'https://raw.githubusercontent.com/TylerAmesIsGay/proxy-list/main/http.txt',
            'https://raw.githubusercontent.com/TylerAmesIsGay/proxy-list/main/https.txt',
            'https://raw.githubusercontent.com/TylerAmesIsGay/proxy-list/main/socks4.txt',
            'https://raw.githubusercontent.com/TylerAmesIsGay/proxy-list/main/socks5.txt',
            'https://raw.githubusercontent.com/casals-ar/proxy-list/main/https',
            'https://raw.githubusercontent.com/casals-ar/proxy-list/main/http',
            'https://raw.githubusercontent.com/casals-ar/proxy-list/main/socks5',
            'API_PROXYSCRAPE',
            'API_GEONODE',
            'API_PROXYLIST',
            'API_FREEPROXY',
            'API_PROXYNOVA',
            'API_SPYSONE',
            'API_PROXYSCAN',
            'API_PROXYROTATOR',
            'API_PROXYHUB',
            'API_PROXYSPACE',
            'API_PUBPROXY',
            'API_PROXYRACK'
        ],
        'http': [
            'https://raw.githubusercontent.com/mzyui/proxy-list/refs/heads/main/http.txt',
            'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
            'https://vakhov.github.io/fresh-proxy-list/http.txt',
            'https://raw.githubusercontent.com/SoliSpirit/proxy-list/main/http.txt',
            'https://raw.githubusercontent.com/FifzzSENZE/Master-Proxy/master/proxies/http.txt',
            'https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/http/data.txt',
            'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt',
            'https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt',
            'https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/http.txt',
            'https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt',
            'https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/http.txt',
            'https://raw.githubusercontent.com/officialputuid/KangProxy/main/http/http.txt',
            'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt',
            'https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt',
            'https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt',
            'https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/http_proxies.txt',
            'https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt',
            'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt',
            'https://raw.githubusercontent.com/im-razvan/proxy_list/main/http.txt',
            'https://raw.githubusercontent.com/caliphdev/Proxy-List/master/http.txt',
            'https://raw.githubusercontent.com/saisuiu/Lionkings-Http-Proxys-Proxies/main/free.txt',
            'https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt',
            'https://raw.githubusercontent.com/yemixzy/proxy-list/main/proxies/http.txt',
            'https://raw.githubusercontent.com/Vann-Dev/proxy-list/main/proxies/http.txt',
            'https://raw.githubusercontent.com/tuanminpay/live-proxy/master/http.txt',
            'https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTP_RAW.txt',
            'https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/http.txt',
            'https://raw.githubusercontent.com/rx443/proxy-list/main/online/http.txt',
            'https://raw.githubusercontent.com/TylerAmesIsGay/proxy-list/main/http.txt',
            'https://raw.githubusercontent.com/casals-ar/proxy-list/main/http',
            'https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt',
            'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt',
            'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt',
            'https://raw.githubusercontent.com/ObcbO/getproxy/master/http.txt',
            'https://raw.githubusercontent.com/opsxcq/proxy-list/master/list_http.txt',
            'https://raw.githubusercontent.com/ProxyScraper/ProxyScraper/master/proxies-http.txt',
            'https://raw.githubusercontent.com/Volodichev/proxy-list/main/http.txt',
            'https://raw.githubusercontent.com/zevtyardt/proxy-list/main/http.txt',
            'https://raw.githubusercontent.com/UserR3X/proxy-list/main/http.txt',
            'API_PROXYSCRAPE',
            'API_GEONODE',
            'API_PROXYLIST',
            'API_FREEPROXY',
            'API_PUBPROXY'
        ],
        'https': [
            'https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS.txt',
            'https://vakhov.github.io/fresh-proxy-list/https.txt',
            'https://raw.githubusercontent.com/SoliSpirit/proxy-list/main/https.txt',
            'https://raw.githubusercontent.com/FifzzSENZE/Master-Proxy/master/proxies/https.txt',
            'https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/https/data.txt',
            'https://raw.githubusercontent.com/mzyui/proxy-list/refs/heads/main/https.txt',
            'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt',
            'https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/https.txt',
            'https://raw.githubusercontent.com/officialputuid/KangProxy/main/https/https.txt',
            'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/https.txt',
            'https://raw.githubusercontent.com/zloi-user/hideip.me/main/https.txt',
            'https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/https_proxies.txt',
            'https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/https.txt',
            'https://raw.githubusercontent.com/Vann-Dev/proxy-list/main/proxies/https.txt',
            'https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt',
            'https://raw.githubusercontent.com/rx443/proxy-list/main/online/https.txt',
            'https://raw.githubusercontent.com/TylerAmesIsGay/proxy-list/main/https.txt',
            'https://raw.githubusercontent.com/casals-ar/proxy-list/main/https',
            'https://raw.githubusercontent.com/aslisk/proxyhttps/main/https.txt',
            'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt',
            'https://raw.githubusercontent.com/ObcbO/getproxy/master/https.txt',
            'https://raw.githubusercontent.com/opsxcq/proxy-list/master/list_https.txt',
            'https://raw.githubusercontent.com/ProxyScraper/ProxyScraper/master/proxies-https.txt',
            'https://raw.githubusercontent.com/Volodichev/proxy-list/main/https.txt',
            'https://raw.githubusercontent.com/zevtyardt/proxy-list/main/https.txt',
            'https://raw.githubusercontent.com/UserR3X/proxy-list/main/https.txt',
            'API_PROXYSCRAPE',
            'API_GEONODE',
            'API_PROXYNOVA',
            'API_SPYSONE'
        ],
        'socks4': [
            'https://raw.githubusercontent.com/mzyui/proxy-list/refs/heads/main/socks4.txt',
            'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt',
            'https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4.txt',
            'https://vakhov.github.io/fresh-proxy-list/socks4.txt',
            'https://raw.githubusercontent.com/SoliSpirit/proxy-list/main/socks4.txt',
            'https://raw.githubusercontent.com/FifzzSENZE/Master-Proxy/master/proxies/socks4.txt',
            'https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/socks4/data.txt',
            'https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/socks4.txt',
            'https://raw.githubusercontent.com/officialputuid/KangProxy/main/socks4/socks4.txt',
            'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks4.txt',
            'https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt',
            'https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks4.txt',
            'https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/socks4_proxies.txt',
            'https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt',
            'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt',
            'https://raw.githubusercontent.com/caliphdev/Proxy-List/master/socks4.txt',
            'https://raw.githubusercontent.com/yemixzy/proxy-list/main/proxies/socks4.txt',
            'https://raw.githubusercontent.com/Vann-Dev/proxy-list/main/proxies/socks4.txt',
            'https://raw.githubusercontent.com/tuanminpay/live-proxy/master/socks4.txt',
            'https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt',
            'https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/socks4.txt',
            'https://raw.githubusercontent.com/rx443/proxy-list/main/online/socks4.txt',
            'https://raw.githubusercontent.com/TylerAmesIsGay/proxy-list/main/socks4.txt',
            'https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt',
            'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt',
            'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt',
            'https://raw.githubusercontent.com/ObcbO/getproxy/master/socks4.txt',
            'https://raw.githubusercontent.com/opsxcq/proxy-list/master/list_socks4.txt',
            'https://raw.githubusercontent.com/ProxyScraper/ProxyScraper/master/proxies-socks4.txt',
            'https://raw.githubusercontent.com/Volodichev/proxy-list/main/socks4.txt',
            'https://raw.githubusercontent.com/zevtyardt/proxy-list/main/socks4.txt',
            'https://raw.githubusercontent.com/UserR3X/proxy-list/main/socks4.txt'
        ],
        'socks5': [
            'https://raw.githubusercontent.com/mzyui/proxy-list/refs/heads/main/socks5.txt',
            'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt',
            'https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5.txt',
            'https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt',
            'https://vakhov.github.io/fresh-proxy-list/socks5.txt',
            'https://raw.githubusercontent.com/SoliSpirit/proxy-list/main/socks5.txt',
            'https://raw.githubusercontent.com/FifzzSENZE/Master-Proxy/master/proxies/socks5.txt',
            'https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/socks5/data.txt',
            'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt',
            'https://raw.githubusercontent.com/prxchk/proxy-list/main/socks5.txt',
            'https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/socks5.txt',
            'https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt',
            'https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/socks5.txt',
            'https://raw.githubusercontent.com/officialputuid/KangProxy/main/socks5/socks5.txt',
            'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks5.txt',
            'https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt',
            'https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks5.txt',
            'https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/socks5_proxies.txt',
            'https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt',
            'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt',
            'https://raw.githubusercontent.com/hookzof/socks5_list/master/tg/socks.txt',
            'https://raw.githubusercontent.com/caliphdev/Proxy-List/master/socks5.txt',
            'https://raw.githubusercontent.com/yemixzy/proxy-list/main/proxies/socks5.txt',
            'https://raw.githubusercontent.com/Vann-Dev/proxy-list/main/proxies/socks5.txt',
            'https://raw.githubusercontent.com/tuanminpay/live-proxy/master/socks5.txt',
            'https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt',
            'https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/socks5.txt',
            'https://raw.githubusercontent.com/rx443/proxy-list/main/online/socks5.txt',
            'https://raw.githubusercontent.com/TylerAmesIsGay/proxy-list/main/socks5.txt',
            'https://raw.githubusercontent.com/casals-ar/proxy-list/main/socks5',
            'https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt',
            'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt',
            'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt',
            'https://raw.githubusercontent.com/ObcbO/getproxy/master/socks5.txt',
            'https://raw.githubusercontent.com/opsxcq/proxy-list/master/list_socks5.txt',
            'https://raw.githubusercontent.com/ProxyScraper/ProxyScraper/master/proxies-socks5.txt',
            'https://raw.githubusercontent.com/Volodichev/proxy-list/main/socks5.txt',
            'https://raw.githubusercontent.com/zevtyardt/proxy-list/main/socks5.txt',
            'https://raw.githubusercontent.com/UserR3X/proxy-list/main/socks5.txt'
        ]
    }

class SourceHealthMonitor:
    def __init__(self):
        self.health_file = os.path.join(get_current_directory(), "source_health.json")
        self.health_data = self.load_health_data()

    def _get_source_id(self, url):
        return hashlib.sha256(url.encode()).hexdigest()[:16]

    def load_health_data(self):
        try:
            if os.path.exists(self.health_file):
                with open(self.health_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            pass
        return {}

    def save_health_data(self):
        try:
            with open(self.health_file, 'w', encoding='utf-8') as f:
                json.dump(self.health_data, f, indent=2)
        except (IOError, OSError) as e:
            pass

    def update_source_health(self, url, success, response_time=0, proxy_count=0):
        source_id = self._get_source_id(url)
        if source_id not in self.health_data:
            self.health_data[source_id] = {
                "success_count": 0,
                "fail_count": 0,
                "total_requests": 0,
                "avg_response_time": 0,
                "last_success": None,
                "last_fail": None,
                "total_proxies": 0,
                "health_score": 100
            }

        data = self.health_data[source_id]
        data["total_requests"] += 1

        if success:
            data["success_count"] += 1
            data["last_success"] = time.time()
            data["total_proxies"] += proxy_count
            if data["avg_response_time"] == 0:
                data["avg_response_time"] = response_time
            else:
                data["avg_response_time"] = (data["avg_response_time"] + response_time) / 2
        else:
            data["fail_count"] += 1
            data["last_fail"] = time.time()
        success_rate = data["success_count"] / data["total_requests"]
        time_penalty = 0
        if data["last_fail"] and data["last_success"]:
            hours_since_last_success = (time.time() - data["last_success"]) / 3600
            if hours_since_last_success > 24:
                time_penalty = min(50, hours_since_last_success - 24)

        data["health_score"] = max(0, int((success_rate * 100) - time_penalty))

        self.save_health_data()

    def is_source_healthy(self, url, min_health_score=30):
        source_id = self._get_source_id(url)
        if source_id not in self.health_data:
            return True

        data = self.health_data[source_id]
        return data["health_score"] >= min_health_score

    def filter_healthy_sources(self, urls, min_health_score=30):
        return [url for url in urls if self.is_source_healthy(url, min_health_score)]
source_health_monitor = SourceHealthMonitor()

def get_proxy_urls():
    urls = get_proxy_urls_with_rotation()
    filtered_urls = {}

    for category, url_list in urls.items():
        unique_urls = list(dict.fromkeys(url_list))
        healthy_urls = source_health_monitor.filter_healthy_sources(unique_urls)
        if healthy_urls:
            filtered_urls[category] = healthy_urls

    return filtered_urls

async def fetch_api_proxies_async(session, api_type):
    try:
        if api_type == 'API_PROXYSCRAPE':
            urls = [
                "https://api.proxyscrape.com/v2/?request=get&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
                "https://api.proxyscrape.com/v2/?request=get&protocol=socks4&timeout=10000&country=all&ssl=all&anonymity=all",
                "https://api.proxyscrape.com/v2/?request=get&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all"
            ]
            all_proxies = []
            for url in urls:
                try:
                    async with session.get(url, timeout=10) as response:
                        if response.status == 200:
                            text = await response.text()
                            proxies = [line.strip() for line in text.split('\n') if line.strip()]
                            all_proxies.extend(proxies)
                except:
                    continue
            return all_proxies
        elif api_type == 'API_GEONODE':
            all_proxies = []
            for page in range(1, 6):
                try:
                    url = f"https://proxylist.geonode.com/api/proxy-list?limit=500&page={page}&sort_by=lastChecked&sort_type=desc"
                    async with session.get(url, timeout=10) as response:
                        if response.status == 200:
                            data = await response.json()
                            if 'data' in data and data['data']:
                                for proxy_info in data['data']:
                                    if 'ip' in proxy_info and 'port' in proxy_info:
                                        proxy = f"{proxy_info['ip']}:{proxy_info['port']}"
                                        all_proxies.append(proxy)
                            else:
                                break
                        else:
                            break
                except:
                    break
            return all_proxies
        elif api_type == 'API_PROXYLIST':
            all_proxies = []
            protocols = ['http', 'socks4', 'socks5']
            for protocol in protocols:
                try:
                    url = f"https://www.proxy-list.download/api/v1/get?type={protocol}"
                    async with session.get(url, timeout=10) as response:
                        if response.status == 200:
                            text = await response.text()
                            proxies = [line.strip() for line in text.split('\n')
                                    if re.match(r'^\d{1,3}(\.\d{1,3}){3}:\d+$', line.strip())]
                            all_proxies.extend(proxies)
                except:
                    continue
            return all_proxies
        elif api_type == 'API_FREEPROXY':
            all_proxies = []
            urls = [
                "https://www.proxy-list.download/api/v0/get?l=en&t=http",
                "https://www.proxy-list.download/api/v0/get?l=en&t=socks4",
                "https://www.proxy-list.download/api/v0/get?l=en&t=socks5"
            ]
            for url in urls:
                try:
                    async with session.get(url, timeout=10) as response:
                        if response.status == 200:
                            data = await response.json()
                            if isinstance(data, list) and len(data) > 0:
                                for item in data[0]:
                                    if 'IP' in item and 'PORT' in item:
                                        proxy = f"{item['IP']}:{item['PORT']}"
                                        all_proxies.append(proxy)
                except:
                    continue
            return all_proxies
        elif api_type == 'API_PROXYNOVA':
            try:
                url = "https://www.proxynova.com/proxy-server-list/country-code/xx/"
                async with session.get(url, timeout=10) as response:
                    if response.status == 200:
                        text = await response.text()
                        import re
                        pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d+)'
                        matches = re.findall(pattern, text)
                        return [f"{ip}:{port}" for ip, port in matches[:200]]
            except:
                pass
            return []
        elif api_type == 'API_SPYSONE':
            try:
                urls = [
                    "http://spys.one/en/http-proxy-list/",
                    "http://spys.one/en/socks-proxy-list/"
                ]
                all_proxies = []
                for url in urls:
                    async with session.get(url, timeout=10) as response:
                        if response.status == 200:
                            text = await response.text()
                            import re
                            pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d+)'
                            matches = re.findall(pattern, text)
                            all_proxies.extend([f"{ip}:{port}" for ip, port in matches[:100]])
                return all_proxies
            except:
                pass
            return []
        elif api_type == 'API_PROXYSCAN':
            all_proxies = []
            protocols = ['http', 'socks4', 'socks5']
            for protocol in protocols:
                try:
                    url = f"https://www.proxyscan.io/download?type={protocol}"
                    async with session.get(url, timeout=10) as response:
                        if response.status == 200:
                            text = await response.text()
                            proxies = [line.strip() for line in text.split('\n') if line.strip() and ':' in line]
                            all_proxies.extend(proxies)
                except:
                    continue
            return all_proxies
        elif api_type == 'API_PROXYROTATOR':
            try:
                url = "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/http.txt"
                async with session.get(url, timeout=10) as response:
                    if response.status == 200:
                        text = await response.text()
                        return [line.strip() for line in text.split('\n') if line.strip()]
            except:
                pass
            return []
        elif api_type == 'API_PROXYHUB':
            all_proxies = []
            try:
                url = "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt"
                async with session.get(url, timeout=10) as response:
                    if response.status == 200:
                        text = await response.text()
                        proxies = [line.strip() for line in text.split('\n') if line.strip()]
                        all_proxies.extend(proxies)
            except:
                pass
            try:
                url = "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt"
                async with session.get(url, timeout=10) as response:
                    if response.status == 200:
                        text = await response.text()
                        proxies = [line.strip() for line in text.split('\n') if line.strip()]
                        all_proxies.extend(proxies)
            except:
                pass
            try:
                url = "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt"
                async with session.get(url, timeout=10) as response:
                    if response.status == 200:
                        text = await response.text()
                        proxies = [line.strip() for line in text.split('\n') if line.strip()]
                        all_proxies.extend(proxies)
            except:
                pass
            return all_proxies
        elif api_type == 'API_PROXYSPACE':
            all_proxies = []
            try:
                urls = [
                    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
                    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
                    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt"
                ]
                for url in urls:
                    async with session.get(url, timeout=10) as response:
                        if response.status == 200:
                            text = await response.text()
                            proxies = [line.strip() for line in text.split('\n') if line.strip()]
                            all_proxies.extend(proxies)
            except:
                pass
            return all_proxies
        elif api_type == 'API_PUBPROXY':
            all_proxies = []
            try:
                protocols = ['http', 'socks4', 'socks5']
                for protocol in protocols:
                    for page in range(1, 6):
                        url = f"http://pubproxy.com/api/proxy?limit=20&format=txt&type={protocol}&level=anonymous"
                        async with session.get(url, timeout=10) as response:
                            if response.status == 200:
                                text = await response.text()
                                proxies = [line.strip() for line in text.split('\n') if line.strip() and ':' in line]
                                all_proxies.extend(proxies)
                        await asyncio.sleep(0.5)
            except:
                pass
            return all_proxies
        elif api_type == 'API_PROXYRACK':
            all_proxies = []
            try:
                url = "https://api.proxyrack.net/free-proxy-list"
                async with session.get(url, timeout=10) as response:
                    if response.status == 200:
                        data = await response.json()
                        if isinstance(data, list):
                            for item in data:
                                if 'ip' in item and 'port' in item:
                                    proxy = f"{item['ip']}:{item['port']}"
                                    all_proxies.append(proxy)
            except:
                pass
            return all_proxies
    except (httpx.RequestError, httpx.TimeoutException):
        return []

async def check_for_updates_async():
    urls = get_proxy_urls()
    session_data = load_session_data()

    async with aiohttp.ClientSession() as session:
        for proxy_type, url_list in urls.items():
            tasks = []
            for i, url in enumerate(url_list):
                tasks.append(get_file_hash_async(url, session))

            hashes = await asyncio.gather(*tasks)

            for i, url in enumerate(url_list):
                current_hash = hashes[i]
                old_hash = session_data.get(f'{proxy_type}_{i}_hash', '')

                if current_hash and current_hash != old_hash:
                    session_data[f'{proxy_type}_{i}_hash'] = current_hash
                    session_data[f'{proxy_type}_{i}_downloaded'] = []

    return session_data

async def get_proxy_count_async(proxy_type='all'):
    urls = get_proxy_urls()
    total_count = 0
    successful_sources = 0
    seen_proxies = set()

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive'
        }
        
        connector = aiohttp.TCPConnector(limit=150, limit_per_host=30, ssl=False)
        timeout = aiohttp.ClientTimeout(total=20, connect=8)
        
        async with aiohttp.ClientSession(headers=headers, connector=connector, timeout=timeout) as session:
            semaphore = asyncio.Semaphore(50)
            
            async def fetch_url_count(url):
                async with semaphore:
                    max_retries = 2
                    for attempt in range(max_retries):
                        try:
                            if url.startswith('API_'):
                                proxies = await fetch_api_proxies_async(session, url)
                                if proxies:
                                    unique_count = 0
                                    for proxy in proxies:
                                        proxy_clean = proxy.strip()
                                        if proxy_clean not in seen_proxies:
                                            seen_proxies.add(proxy_clean)
                                            unique_count += 1
                                    return unique_count
                            else:
                                async with session.get(url) as response:
                                    if response.status == 200:
                                        text = await response.text()
                                        lines = text.split('\n')
                                        unique_count = 0
                                        for line in lines:
                                            line = line.strip()
                                            if line and PROXY_LINE_RE.match(line):
                                                if line not in seen_proxies:
                                                    seen_proxies.add(line)
                                                    unique_count += 1
                                        return unique_count
                                    elif response.status == 404 or response.status == 403:
                                        return 0
                                    elif response.status == 429:
                                        await asyncio.sleep(1)
                                        continue
                                    return 0
                        except asyncio.TimeoutError:
                            if attempt < max_retries - 1:
                                await asyncio.sleep(0.5)
                                continue
                            return 0
                        except Exception:
                            if attempt < max_retries - 1:
                                await asyncio.sleep(0.5)
                                continue
                            return 0
                    return 0

            url_list = urls.get(proxy_type, [])
            tasks = [fetch_url_count(url) for url in url_list]
            results = await asyncio.gather(*tasks, return_exceptions=True)

            for result in results:
                if isinstance(result, int) and result > 0:
                    total_count += result
                    successful_sources += 1
                        
    except Exception:
        pass

    if total_count == 0 or successful_sources < 3:
        try:
            fallback_urls = [
                'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
                'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt',
                'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt',
                'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/all.txt',
                'https://raw.githubusercontent.com/mzyui/proxy-list/refs/heads/main/all.txt',
                'https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS.txt',
                'https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4.txt',
                'https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5.txt',
                'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt',
                'https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt'
            ]
            
            fallback_count = 0
            fallback_seen = set()
            for url in fallback_urls:
                try:
                    with httpx.Client(headers=headers, verify=False, timeout=6) as client:
                        r = client.get(url)
                        if r.status_code == 200:
                            lines = r.text.split('\n')
                            for line in lines:
                                line = line.strip()
                                if line and PROXY_LINE_RE.match(line):
                                    if line not in fallback_seen:
                                        fallback_seen.add(line)
                                        fallback_count += 1
                except Exception:
                    pass
            
            if fallback_count > 0:
                return fallback_count
        except Exception:
            pass

    return total_count

async def get_total_proxy_count_async(proxy_types):
    if 'all' in proxy_types:
        return await get_proxy_count_async('all')
    
    tasks = [get_proxy_count_async(pt) for pt in proxy_types]
    results = await asyncio.gather(*tasks)
    return sum(results)

async def count_available_new_proxies_async(proxy_types):
    urls = get_proxy_urls()
    session_data = load_session_data()

    if not session_data:
        total_proxies = await get_total_proxy_count_async(proxy_types)
        return total_proxies

    total_from_sources = await get_total_proxy_count_async(proxy_types)
    excluded_count = 0
    
    for proxy_type in proxy_types:
        for url_index in range(len(urls.get(proxy_type, []))):
            key = f'{proxy_type}_{url_index}_downloaded'
            if key in session_data:
                excluded_count += len(session_data[key])

    available_count = max(0, total_from_sources - excluded_count)
    return available_count

async def get_total_count_for_types_async(proxy_types):
    if proxy_types == ['all']:
        return await get_proxy_count_async('all')
    tasks = [get_proxy_count_async(pt) for pt in proxy_types]
    results = await asyncio.gather(*tasks)
    return sum(results)

def get_downloaded_count_from_cache(proxy_types):
    session_data = load_session_data()
    if not session_data:
        return 0
    prefixes = ['all'] if proxy_types == ['all'] else proxy_types
    total = 0
    for key, val in session_data.items():
        if key.endswith('_downloaded') and isinstance(val, list):
            for prefix in prefixes:
                if key.startswith(f"{prefix}_"):
                    total += len(val)
                    break
    return total

async def download_proxies_with_progress_async(proxy_types, count, classify_output=False, will_check=False):
    urls = get_proxy_urls()
    session_data = load_session_data()
    all_proxies = []

    status_text = "🔄 Đang thu thập proxy từ internet..."
    rainbow_text = create_rainbow_text(status_text)
    with console.status(rainbow_text, spinner="aesthetic"):
        semaphore = asyncio.Semaphore(100)

        async def fetch_proxies(session, proxy_type, url_index, url):
            async with semaphore:
                start_time = time.time()
                try:
                    if url.startswith('API_'):
                        proxies = await fetch_api_proxies_async(session, url)
                        response_time = time.time() - start_time
                        source_health_monitor.update_source_health(url, True, response_time, len(proxies))
                        return proxy_type, url_index, proxies
                    else:
                        async with session.get(url, timeout=10) as response:
                            response_time = time.time() - start_time
                            if response.status == 200:
                                text = await response.text()
                                proxies = [line.strip() for line in text.split('\n')
                                           if re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+$', line.strip())]
                                source_health_monitor.update_source_health(url, True, response_time, len(proxies))
                                return proxy_type, url_index, proxies
                            else:
                                source_health_monitor.update_source_health(url, False, response_time, 0)
                                return proxy_type, url_index, []
                except (aiohttp.ClientError, asyncio.TimeoutError) as e:
                    response_time = time.time() - start_time
                    source_health_monitor.update_source_health(url, False, response_time, 0)
                    return proxy_type, url_index, []

        async with aiohttp.ClientSession() as session:
            download_tasks = []
            for proxy_type in proxy_types:
                for url_index, url in enumerate(urls[proxy_type]):
                    download_tasks.append(fetch_proxies(session, proxy_type, url_index, url))

            results = await asyncio.gather(*download_tasks)

            seen_proxies = set()
            for proxy_type, url_index, proxies_list in results:
                downloaded_hashes = set(session_data.get(f'{proxy_type}_{url_index}_downloaded', []))

                for proxy in proxies_list:
                    proxy_clean = proxy.strip()
                    if proxy_clean not in seen_proxies:
                        seen_proxies.add(proxy_clean)
                        proxy_hash = hashlib.sha256(proxy_clean.encode()).hexdigest()
                    if proxy_hash not in downloaded_hashes:
                            all_proxies.append((proxy_clean, proxy_type, url_index))

    if len(all_proxies) == 0:
        reset_session_data()
        console.print(f"\n[yellow on black]⚠️ Đã hết proxy mới có sẵn, cache đã được reset tự động.[/yellow on black]")
        return [], None

    if len(all_proxies) < count:
        count = len(all_proxies)
        console.print(f"[yellow]Chỉ có thể lấy {count} proxy[/yellow]")

    selected_proxy_data = random.sample(all_proxies, count) if len(all_proxies) >= count else all_proxies

    selected_proxies = [proxy_data[0] for proxy_data in selected_proxy_data]

    for proxy_data in selected_proxy_data:
        proxy, proxy_type, url_index = proxy_data
        proxy_hash = hashlib.sha256(proxy.encode()).hexdigest()
        key = f'{proxy_type}_{url_index}_downloaded'

        if key not in session_data:
            session_data[key] = []
        if proxy_hash not in session_data[key]:
            session_data[key].append(proxy_hash)

    save_session_data(session_data)

    output_file = None

    if not will_check:
        if classify_output and len(proxy_types) > 1:
            classified_proxies = {}
            for ptype in proxy_types:
                classified_proxies[ptype] = []

            for i, proxy in enumerate(selected_proxies):
                proxy_type = proxy_types[i % len(proxy_types)]
                classified_proxies[proxy_type].append(proxy)

            for ptype, plist in classified_proxies.items():
                if plist:
                    output_file = os.path.join(get_current_directory(), f"proxy_{ptype}.txt")
                    with open(output_file, 'a', encoding='utf-8') as f:
                        if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
                            f.write("\n")
                        f.write('\n'.join(plist))


                    console.print(f"[green]✓ Đã lưu {len(plist)} proxy {ptype}: {output_file}[/green]")
        else:
            if len(proxy_types) == 1 and proxy_types[0] != 'all':
                output_file = os.path.join(get_current_directory(), f"proxy_{proxy_types[0]}.txt")
            else:
                output_file = os.path.join(get_current_directory(), "proxy_public.txt")

            with open(output_file, 'a', encoding='utf-8') as f:
                if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
                    f.write("\n")
                f.write('\n'.join(selected_proxies))
            console.print(f"[green]✓ Đã lưu {len(selected_proxies)} proxy: {output_file}[/green]")

    return selected_proxies, output_file

async def handle_system_config(proxy_manager):
    while True:
        clear_screen()
        config_title = create_rainbow_text("◆◆◆ CÀI ĐẶT NHANH ◆◆◆")

        user_settings = load_user_settings()
        menu1_settings = user_settings.get('menu1_settings', {})
        menu2_settings = user_settings.get('menu2_check_settings', {})

        menu_content = Text("", justify="left")
        menu_content.append("1. 🔧  Chỉnh sửa cài đặt Menu 1 (Kiểm tra proxy)\n", style="bold cyan")
        menu_content.append("2. 🔧  Chỉnh sửa cài đặt Menu 2 (Thu thập proxy)\n", style="bold yellow")
        menu_content.append("3. 🔧  Chỉnh sửa cài đặt Menu 5 (Proxy Scanner)\n", style="bold magenta")
        menu_content.append("4. 👁️  Xem cài đặt hiện tại\n", style="bold green")
        menu_content.append("5. 🗑️  Xóa tất cả cài đặt\n", style="bold red")
        menu_content.append("0. ❌  Thoát", style="bold white")

        menu_panel = Panel(
            menu_content,
            title=config_title,
            border_style="bold bright_magenta",
            padding=(2, 4),
            title_align="center",
            box=ROUNDED,
            highlight=True
        )
        console.print(menu_panel, justify="center")

        choice = console.input("\n[bold bright_cyan]◆ Nhập lựa chọn của bạn (0-5): [/bold bright_cyan]").strip()

        if choice == '1':
            await _config_menu1_settings()
        elif choice == '2':
            await _config_menu2_settings()
        elif choice == '3':
            await _config_menu5_settings()
        elif choice == '4':
            await _show_current_settings()
        elif choice == '5':
            await _clear_all_settings()
        elif choice == '0':
            break
        else:
            console.print("[red]Lựa chọn không hợp lệ![/red]")
            time.sleep(1)

async def _config_menu1_settings():
    while True:
        clear_screen()
        console.print(create_rainbow_text("🔧 CHỈNH SỬA CÀI ĐẶT MENU 1"))
        
        user_settings = load_user_settings()
        menu1_settings = user_settings.get('menu1_settings', {})
        
        content = Text.from_markup(
            f"[bold white]1.[/bold white] Số luồng: [bold bright_green]{menu1_settings.get('max_threads', 50)}[/bold bright_green]\n"
            f"[bold white]2.[/bold white] Thời gian chờ: [bold bright_green]{menu1_settings.get('timeout', 10)}s[/bold bright_green]\n"
            f"[bold white]3.[/bold white] File kết quả: [bold bright_green]{menu1_settings.get('output_file', 'working_proxies.txt')}[/bold bright_green]\n"
            f"[bold white]4.[/bold white] Phân loại proxy: [bold bright_green]{'Có' if menu1_settings.get('classify_proxies', True) else 'Không'}[/bold bright_green]\n"
            f"[bold white]5.[/bold white] Loại phân loại: [bold bright_green]{menu1_settings.get('classify_type', 'country')}[/bold bright_green]\n"
            f"[bold white]6.[/bold white] Giao diện Rich: [bold bright_green]{'Bật' if menu1_settings.get('use_rich_interface', True) else 'Tắt'}[/bold bright_green]\n"
            f"[bold white]7.[/bold white] Tự động lưu: [bold bright_green]{'Bật' if menu1_settings.get('auto_save_results', True) else 'Tắt'}[/bold bright_green]\n"
            f"[bold white]8.[/bold white] Kiểm tra tốc độ: [bold bright_green]{'Bật' if menu1_settings.get('check_proxy_speed', False) else 'Tắt'}[/bold bright_green]\n"
            "[bold white]0.[/bold white] Quay lại"
        )
        
        panel_width = min(console.size.width - 10, 110)
        panel = Panel(Align.center(content), title="Cài đặt Menu 1", border_style="cyan", padding=(2,6), width=panel_width, box=ROUNDED, highlight=True)
        console.print(panel, justify="center")
        choice = console.input(Text("\n◆ Chọn: ", style="bold bright_white")).strip()
        
        if choice == '1':
            try:
                new_threads = int(console.input("◆ Nhập số luồng mới: "))
                menu1_settings['max_threads'] = new_threads
                user_settings['menu1_settings'] = menu1_settings
                save_user_settings(user_settings)
            except ValueError: 
                console.print("[red]Lỗi: Phải là số.[/red]")
        elif choice == '2':
            try:
                new_timeout = int(console.input("◆ Nhập thời gian chờ mới (giây): "))
                if new_timeout >= 1: 
                    menu1_settings['timeout'] = new_timeout
                    user_settings['menu1_settings'] = menu1_settings
                    save_user_settings(user_settings)
            except ValueError: 
                console.print("[red]Lỗi: Phải là số.[/red]")
        elif choice == '3':
            new_file = console.input("◆ Nhập tên file kết quả mới: ")
            if new_file:
                menu1_settings['output_file'] = new_file
                user_settings['menu1_settings'] = menu1_settings
                save_user_settings(user_settings)
        elif choice == '4':
            menu1_settings['classify_proxies'] = not menu1_settings.get('classify_proxies', True)
            user_settings['menu1_settings'] = menu1_settings
            save_user_settings(user_settings)
        elif choice == '5':
            menu1_settings['classify_type'] = 'protocol' if menu1_settings.get('classify_type', 'country') == 'country' else 'country'
            user_settings['menu1_settings'] = menu1_settings
            save_user_settings(user_settings)
        elif choice == '6':
            menu1_settings['use_rich_interface'] = not menu1_settings.get('use_rich_interface', True)
            user_settings['menu1_settings'] = menu1_settings
            save_user_settings(user_settings)
        elif choice == '7':
            menu1_settings['auto_save_results'] = not menu1_settings.get('auto_save_results', True)
            user_settings['menu1_settings'] = menu1_settings
            save_user_settings(user_settings)
        elif choice == '8':
            menu1_settings['check_proxy_speed'] = not menu1_settings.get('check_proxy_speed', False)
            user_settings['menu1_settings'] = menu1_settings
            save_user_settings(user_settings)
        elif choice == '0':
            break
        else:
            console.print("[red]Lựa chọn không hợp lệ![/red]")
        time.sleep(0.5)

async def _config_menu2_settings():
    while True:
        clear_screen()
        console.print(create_rainbow_text("🔧 CHỈNH SỬA CÀI ĐẶT MENU 2"))
        
        user_settings = load_user_settings()
        menu2_settings = user_settings.get('menu2_check_settings', {})
        
        content = Text.from_markup(
            f"[bold white]1.[/bold white] Tự động kiểm tra: [bold bright_green]{'Có' if menu2_settings.get('auto_check', True) else 'Không'}[/bold bright_green]\n"
            f"[bold white]2.[/bold white] Phân loại kết quả: [bold bright_green]{'Có' if menu2_settings.get('classify_output', True) else 'Không'}[/bold bright_green]\n"
            f"[bold white]3.[/bold white] Phân loại theo: [bold bright_green]{menu2_settings.get('classify_type', 'quốc gia')}[/bold bright_green]\n"
            f"[bold white]4.[/bold white] File kết quả: [bold bright_green]{menu2_settings.get('output_file', 'collected_proxies.txt')}[/bold bright_green]\n"
            f"[bold white]5.[/bold white] Timeout: [bold bright_green]{menu2_settings.get('timeout', 10)}s[/bold bright_green]\n"
            f"[bold white]6.[/bold white] Max threads: [bold bright_green]{menu2_settings.get('max_threads', 50)}[/bold bright_green]\n"
            "[bold white]0.[/bold white] Quay lại"
        )
        
        panel_width = min(console.size.width - 10, 110)
        panel = Panel(Align.center(content), title="Cài đặt Menu 2", border_style="yellow", padding=(2,6), width=panel_width, box=ROUNDED, highlight=True)
        console.print(panel, justify="center")
        choice = console.input(Text("\n◆ Chọn: ", style="bold bright_white")).strip()
        
        if choice == '1':
            console.print(f"\n[cyan]Tự động kiểm tra proxy sau khi thu thập? (y/n):[/cyan]")
            console.print(f"[white]Hiện tại: {'Có' if menu2_settings.get('auto_check', True) else 'Không'}[/white]")
            new_auto_check = get_yes_no_input("[cyan]Nhập giá trị mới (y/n): [/cyan]")
            menu2_settings['auto_check'] = new_auto_check
            user_settings['menu2_check_settings'] = menu2_settings
            save_user_settings(user_settings)
            console.print(f"[green]✓ Đã cập nhật: {'Có' if new_auto_check else 'Không'}[/green]")
        elif choice == '2':
            console.print(f"\n[cyan]Phân loại kết quả? (y/n):[/cyan]")
            console.print(f"[white]Hiện tại: {'Có' if menu2_settings.get('classify_output', True) else 'Không'}[/white]")
            new_classify_output = get_yes_no_input("[cyan]Nhập giá trị mới (y/n): [/cyan]")
            menu2_settings['classify_output'] = new_classify_output
            user_settings['menu2_check_settings'] = menu2_settings
            save_user_settings(user_settings)
            console.print(f"[green]✓ Đã cập nhật: {'Có' if new_classify_output else 'Không'}[/green]")
        elif choice == '3':
            console.print(f"\n[cyan]Phân loại theo quốc gia? (y/n):[/cyan]")
            console.print(f"[white]Hiện tại: {menu2_settings.get('classify_type', 'quốc gia')}[/white]")
            classify_by_country = get_yes_no_input("[cyan]Phân loại theo quốc gia? (y/n): [/cyan]")
            new_classify_type = 'country' if classify_by_country else 'protocol'
            menu2_settings['classify_type'] = new_classify_type
            user_settings['menu2_check_settings'] = menu2_settings
            save_user_settings(user_settings)
            console.print(f"[green]✓ Đã cập nhật: {new_classify_type}[/green]")
        elif choice == '4':
            console.print(f"\n[cyan]Tên file kết quả (mặc định collected_proxies.txt):[/cyan]")
            console.print(f"[white]Hiện tại: {menu2_settings.get('output_file', 'collected_proxies.txt')}[/white]")
            new_output_file = console.input("[cyan]Nhập tên file mới: [/cyan]") or "collected_proxies.txt"
            menu2_settings['output_file'] = new_output_file
            user_settings['menu2_check_settings'] = menu2_settings
            save_user_settings(user_settings)
            console.print(f"[green]✓ Đã cập nhật: {new_output_file}[/green]")
        elif choice == '5':
            console.print(f"\n[cyan]Thời gian chờ (giây):[/cyan]")
            console.print(f"[white]Hiện tại: {menu2_settings.get('timeout', 10)}s[/white]")
            try:
                new_timeout = int(console.input("[cyan]Nhập timeout mới (giây): [/cyan]") or "10")
                if new_timeout >= 1:
                    menu2_settings['timeout'] = new_timeout
                    user_settings['menu2_check_settings'] = menu2_settings
                    save_user_settings(user_settings)
                    console.print(f"[green]✓ Đã cập nhật: {new_timeout}s[/green]")
                else:
                    console.print("[red]Timeout phải >= 1 giây![/red]")
            except ValueError: 
                console.print("[red]Vui lòng nhập số hợp lệ![/red]")
        elif choice == '6':
            console.print(f"\n[cyan]Số luồng tối đa:[/cyan]")
            console.print(f"[white]Hiện tại: {menu2_settings.get('max_threads', 50)}[/white]")
            try:
                new_max_threads = int(console.input("[cyan]Nhập số luồng mới: [/cyan]") or "50")
                menu2_settings['max_threads'] = new_max_threads
                user_settings['menu2_check_settings'] = menu2_settings
                save_user_settings(user_settings)
                console.print(f"[green]✓ Đã cập nhật: {new_max_threads}[/green]")
            except ValueError: 
                console.print("[red]Vui lòng nhập số hợp lệ![/red]")
        elif choice == '0':
            break
        else:
            console.print("[red]Lựa chọn không hợp lệ![/red]")
        time.sleep(0.5)

async def _config_menu5_settings():
    while True:
        clear_screen()
        console.print(create_rainbow_text("🔧 CHỈNH SỬA CÀI ĐẶT MENU 5"))
        
        user_settings = load_user_settings()
        menu5_settings = user_settings.get('menu5_scanner_settings', {})
        
        content = Text.from_markup(
            f"[bold white]1.[/bold white] Số luồng scan: [bold bright_green]{menu5_settings.get('max_threads', 100)}[/bold bright_green]\n"
            f"[bold white]2.[/bold white] Timeout: [bold bright_green]{menu5_settings.get('timeout', 2000)}ms[/bold bright_green]\n"
            f"[bold white]3.[/bold white] File kết quả: [bold bright_green]{menu5_settings.get('output_file', 'scanned_proxies.txt')}[/bold bright_green]\n"
            f"[bold white]4.[/bold white] Phân loại proxy: [bold bright_green]{'Có' if menu5_settings.get('classify', True) else 'Không'}[/bold bright_green]\n"
            f"[bold white]5.[/bold white] Loại phân loại: [bold bright_green]{menu5_settings.get('classify_type', 'protocol')}[/bold bright_green]\n"
            f"[bold white]6.[/bold white] Tự động dọn dẹp log: [bold bright_green]{'Có' if menu5_settings.get('auto_clean', True) else 'Không'}[/bold bright_green]\n"
            "[bold white]0.[/bold white] Quay lại"
        )
        
        panel_width = min(console.size.width - 10, 110)
        panel = Panel(Align.center(content), title="Cài đặt Menu 5", border_style="magenta", padding=(2,6), width=panel_width, box=ROUNDED, highlight=True)
        console.print(panel, justify="center")
        choice = console.input(Text("\n◆ Chọn: ", style="bold bright_white")).strip()
        
        if choice == '1':
            try:
                new_threads = int(console.input("◆ Nhập số luồng scan mới: "))
                menu5_settings['max_threads'] = new_threads
                user_settings['menu5_scanner_settings'] = menu5_settings
                save_user_settings(user_settings)
                console.print(f"[green]✓ Đã cập nhật: {new_threads}[/green]")
            except ValueError:
                console.print("[red]Lỗi: Phải là số.[/red]")
        elif choice == '2':
            try:
                new_timeout = int(console.input("◆ Nhập timeout mới (ms): "))
                if new_timeout >= 100:
                    menu5_settings['timeout'] = new_timeout
                    user_settings['menu5_scanner_settings'] = menu5_settings
                    save_user_settings(user_settings)
                    console.print(f"[green]✓ Đã cập nhật: {new_timeout}ms[/green]")
                else:
                    console.print("[red]Timeout phải >= 100ms![/red]")
            except ValueError:
                console.print("[red]Lỗi: Phải là số.[/red]")
        elif choice == '3':
            new_file = console.input("◆ Nhập tên file kết quả mới: ")
            if new_file:
                menu5_settings['output_file'] = new_file
                user_settings['menu5_scanner_settings'] = menu5_settings
                save_user_settings(user_settings)
                console.print(f"[green]✓ Đã cập nhật: {new_file}[/green]")
        elif choice == '4':
            menu5_settings['classify'] = not menu5_settings.get('classify', True)
            user_settings['menu5_scanner_settings'] = menu5_settings
            save_user_settings(user_settings)
            console.print(f"[green]✓ Đã cập nhật: {'Có' if menu5_settings['classify'] else 'Không'}[/green]")
        elif choice == '5':
            current = menu5_settings.get('classify_type', 'protocol')
            menu5_settings['classify_type'] = 'country' if current == 'protocol' else 'protocol'
            user_settings['menu5_scanner_settings'] = menu5_settings
            save_user_settings(user_settings)
            console.print(f"[green]✓ Đã cập nhật: {menu5_settings['classify_type']}[/green]")
        elif choice == '6':
            menu5_settings['auto_clean'] = not menu5_settings.get('auto_clean', True)
            user_settings['menu5_scanner_settings'] = menu5_settings
            save_user_settings(user_settings)
            status = 'Có' if menu5_settings['auto_clean'] else 'Không'
            console.print(f"[green]✓ Đã cập nhật: {status} (Xóa log sau 7 ngày hoặc > 50MB)[/green]")
        elif choice == '0':
            break
        else:
            console.print("[red]Lựa chọn không hợp lệ![/red]")
        time.sleep(0.5)

async def _show_current_settings():
    clear_screen()
    console.print(create_rainbow_text("👁️ CÀI ĐẶT HIỆN TẠI"))
    
    user_settings = load_user_settings()
    menu1_settings = user_settings.get('menu1_settings', {})
    menu2_settings = user_settings.get('menu2_check_settings', {})
    menu5_settings = user_settings.get('menu5_scanner_settings', {})
    
    if not menu1_settings and not menu2_settings and not menu5_settings:
        console.print("[yellow]Chưa có cài đặt nào được lưu![/yellow]")
    else:
        if menu1_settings:
            console.print("\n[bold cyan]📋 Cài đặt Menu 1 (Kiểm tra proxy):[/bold cyan]")
            console.print(f"  • Số luồng: {menu1_settings.get('max_threads', 'N/A')}")
            console.print(f"  • Timeout: {menu1_settings.get('timeout', 'N/A')}s")
            console.print(f"  • File kết quả: {menu1_settings.get('output_file', 'N/A')}")
            console.print(f"  • Phân loại: {'Có' if menu1_settings.get('classify_proxies') else 'Không'}")
            console.print(f"  • Loại phân loại: {menu1_settings.get('classify_type', 'N/A')}")
        
        if menu2_settings:
            console.print("\n[bold yellow]📋 Cài đặt Menu 2 (Thu thập proxy):[/bold yellow]")
            console.print(f"  • Tự động kiểm tra: {'Có' if menu2_settings.get('auto_check') else 'Không'}")
            console.print(f"  • Phân loại kết quả: {'Có' if menu2_settings.get('classify_output') else 'Không'}")
            console.print(f"  • Phân loại theo: {menu2_settings.get('classify_type', 'quốc gia')}")
            console.print(f"  • File kết quả: {menu2_settings.get('output_file', 'collected_proxies.txt')}")
            console.print(f"  • Timeout: {menu2_settings.get('timeout', 10)}s")
            console.print(f"  • Max threads: {menu2_settings.get('max_threads', 50)}")
        
        if menu5_settings:
            console.print("\n[bold magenta]📋 Cài đặt Menu 5 (Proxy Scanner):[/bold magenta]")
            console.print(f"  • Số luồng scan: {menu5_settings.get('max_threads', 'N/A')}")
            console.print(f"  • Timeout: {menu5_settings.get('timeout', 'N/A')}ms")
            console.print(f"  • File kết quả: {menu5_settings.get('output_file', 'N/A')}")
            console.print(f"  • Phân loại: {'Có' if menu5_settings.get('classify') else 'Không'}")
            console.print(f"  • Loại phân loại: {menu5_settings.get('classify_type', 'N/A')}")
            console.print(f"  • Tự động dọn dẹp: {'Có' if menu5_settings.get('auto_clean', True) else 'Không'}")
    
    console.input("\n[cyan]Nhấn Enter để tiếp tục...[/cyan]")

async def _clear_all_settings():
    clear_screen()
    console.print(create_rainbow_text("🗑️ XÓA TẤT CẢ CÀI ĐẶT"))
    
    if get_yes_no_input("[red]Bạn có chắc muốn xóa tất cả cài đặt? (y/n): [/red]"):
        settings_file = os.path.join(get_current_directory(), "user_settings.json")
        if os.path.exists(settings_file):
            os.remove(settings_file)
        console.print("[green]✓ Đã xóa tất cả cài đặt![/green]")
    else:
        console.print("[yellow]Đã hủy thao tác![/yellow]")
    
    console.input("\n[cyan]Nhấn Enter để tiếp tục...[/cyan]")


async def get_free_proxies_async():
    console.print(f"\n[cyan]Đang kiểm tra cập nhật proxy từ nhiều kho lưu trữ ...[/cyan]")

    await check_for_updates_async()

    console.print(f"\n[cyan]Chức năng lấy proxy public miễn phí[/cyan]")

    last_updated = await get_latest_commit_from_all_repos_async()
    console.print(f"[yellow]Cập nhật lần cuối: {last_updated}[/yellow]")

    total_count = await get_proxy_count_async('all')
    if total_count == 0:
        console.print(f"\n[red]✗ Không thể kết nối tới các kho lưu trữ proxy hoặc không có proxy nào![/red]")
        console.input(f"\n[cyan]Nhấn Enter để quay lại menu chính...[/cyan]")
        return

    console.print(f"[green]Tổng số proxy hiện có sẵn: {total_count:,}[/green]")

    while True:
        try:
            count = int(console.input(f"\n[cyan]Nhập số lượng proxy muốn lấy (1-{total_count:,}):[/cyan] [white]"))
            if 1 <= count <= total_count:
                break
            console.print(f"[red]Vui lòng nhập số từ 1 đến {total_count:,}![/red]")
        except ValueError:
            console.print(f"[red]Vui lòng nhập số hợp lệ![/red]")

    choose_type = get_yes_no_input(f"\n[cyan]Bạn muốn chọn proxy theo loại không? (y/n):[/cyan]")

    if choose_type:
        console.print(f"\n[cyan]Chọn loại proxy (có thể chọn nhiều, cách nhau bởi dấu phẩy):[/cyan]")
        console.print(f"[white]1. HTTP[/white]")
        console.print(f"[white]2. HTTPS[/white]")
        console.print(f"[white]3. SOCKS4[/white]")
        console.print(f"[white]4. SOCKS5[/white]")

        while True:
            choices = console.input(f"\n[cyan]Nhập lựa chọn (ví dụ: 1,2 hoặc 3,4):[/cyan] [white]").strip()
            try:
                choice_list = [int(x.strip()) for x in choices.split(',')]
                if all(1 <= x <= 4 for x in choice_list):
                    proxy_types = []
                    for choice in choice_list:
                        if choice == 1:
                            proxy_types.append('http')
                        elif choice == 2:
                            proxy_types.append('https')
                        elif choice == 3:
                            proxy_types.append('socks4')
                        elif choice == 4:
                            proxy_types.append('socks5')
                    break
                console.print(f"[red]Vui lòng chỉ nhập số 1, 2, 3 hoặc 4![/red]")
            except ValueError:
                console.print(f"[red]Định dạng không hợp lệ! Ví dụ: 1,2[/red]")
    else:
        proxy_types = ['all']

    console.print(f"\n[yellow]Đang kiểm tra số proxy mới có sẵn...[/yellow]")
    available_new_proxies = await count_available_new_proxies_async(proxy_types)

    if available_new_proxies == 0:
        reset_session_data()
        console.print(f"\n[yellow]✓ Đã hết proxy mới có sẵn, cache đã được reset. Bạn có thể chạy lại để lấy tất cả proxy từ đầu.[/yellow]")
        console.input(f"\n[cyan]Nhấn Enter để quay lại menu chính...[/cyan]")
        return

    if available_new_proxies < count:
        console.print(f"\n[yellow]⚠ Chỉ còn {available_new_proxies:,} proxy mới chưa được lấy (bạn yêu cầu {count:,})[/yellow]")
        confirm = get_yes_no_input(f"[cyan]Bạn có muốn lấy {available_new_proxies:,} proxy này không? (y/n):[/cyan]")
        if not confirm:
            console.input(f"\n[cyan]Nhấn Enter để quay lại menu chính...[/cyan]")
            return
        count = available_new_proxies
    else:
        console.print(f"[green]✓ Còn {available_new_proxies:,} proxy mới có thể lấy.[/green]")

    user_settings = load_user_settings()
    menu2_settings = user_settings.get('menu2_check_settings', {})
    
    classify_output = menu2_settings.get('classify', False)
    if len(proxy_types) > 1 and not classify_output:
        classify_output = get_yes_no_input(f"\n[cyan]Bạn muốn phân loại proxy ở file đầu ra không? (y/n):[/cyan]")

    check_now = menu2_settings.get('auto_check', True)

    check_settings = None
    if check_now:
        check_settings = {}
        
        output_file = menu2_settings.get('output_file', 'proxy_live.txt')
        check_settings['output_file'] = output_file
        
        classify_proxies = menu2_settings.get('classify', True)
        check_settings['classify'] = classify_proxies
        
        if check_settings['classify']:
            classify_option = menu2_settings.get('classify_option', '1')
            check_settings['classify_option'] = classify_option
        
        max_threads = menu2_settings.get('max_threads', 10)
        check_settings['max_threads'] = max_threads

    try:
        if check_now:
            proxies, output_file = await download_proxies_with_progress_async(proxy_types, count, classify_output, True)
            
            if not proxies:
                console.input(f"\n[cyan]Nhấn Enter để quay lại menu chính...[/cyan]")
                return

            clear_screen()
            console.print(f"\n[green]✓ Đã thu thập thành công {len(proxies):,} proxy![/green]")
            console.print(f"\n[cyan]Bắt đầu kiểm tra proxy với {check_settings['max_threads']} luồng...[/cyan]")

            run_proxy_check_from_memory(proxies, check_settings)
        else:
            proxies, output_file = await download_proxies_with_progress_async(proxy_types, count, classify_output, False)
            
            if not proxies:
                console.input(f"\n[cyan]Nhấn Enter để quay lại menu chính...[/cyan]")
                return

            console.print(f"\n[green]✓ Đã thu thập thành công {len(proxies):,} proxy![/green]")
            console.print(f"\n[green]✓ Đã lưu proxy vào file: {output_file}[/green]")

    except Exception as e:
        console.print(f"\n[red]Lỗi khi tải proxy: {str(e)}[/red]")

    console.input(f"\n[cyan]Nhấn Enter để quay lại menu chính...[/cyan]")

async def handle_proxy_check(proxy_manager, source_type='file', proxy_file=None, proxy_list=None):
    time.sleep(1)
    clear_screen()
    
    user_settings = load_user_settings()
    menu1_settings = user_settings.get('menu1_settings', {})
    if menu1_settings:
        settings = {
            'max_threads': menu1_settings.get('max_threads', 50),
            'timeout': menu1_settings.get('timeout', 10),
            'output_file': menu1_settings.get('output_file', 'working_proxies.txt'),
            'classify': menu1_settings.get('classify_proxies', True),
            'classify_type': menu1_settings.get('classify_type', 'country')
        }
        console.print(f"[green]✓ Sử dụng cấu hình đã lưu: {settings['max_threads']} luồng, {settings['timeout']}s timeout[/green]")
    else:
        settings = {
            'max_threads': int(console.input("[cyan]Nhập số luồng (mặc định 50): [/cyan]") or "50"),
            'timeout': int(console.input("[cyan]Nhập timeout (mặc định 10s): [/cyan]") or "10"),
            'output_file': console.input("[cyan]Tên file kết quả (mặc định working_proxies.txt): [/cyan]") or "working_proxies.txt",
            'classify': get_yes_no_input("[cyan]Phân loại proxy? (y/n): [/cyan]"),
            'classify_type': 'country' if get_yes_no_input("[cyan]Phân loại theo quốc gia? (y/n): [/cyan]") else 'protocol'
        }
        if get_yes_no_input("\n[cyan]Lưu cấu hình này cho lần sau? (y/n): [/cyan]"):
            menu1_settings = {
                'max_threads': settings['max_threads'],
                'timeout': settings['timeout'],
                'output_file': settings['output_file'],
                'classify_proxies': settings['classify'],
                'classify_type': settings['classify_type']
            }
            user_settings['menu1_settings'] = menu1_settings
            save_user_settings(user_settings)
            console.print("[green]✓ Đã lưu cấu hình![/green]")
            time.sleep(0.5)
    
    clear_screen()
    console.print(create_rainbow_text("✨ Bắt đầu kiểm tra proxy ✨"))

    if source_type == 'file':
        with open(proxy_file, 'r') as f:
            proxy_list = [line.strip() for line in f if line.strip()]
            console.print(f"\n[yellow on black]🔍 Bắt đầu kiểm tra {len(proxy_list)} proxy...[/yellow on black]")
    elif source_type == 'memory':
        console.print(f"\n[yellow on black]🔍 Bắt đầu kiểm tra {len(proxy_list)} proxy...[/yellow on black]")
    else:
        console.print(f"\n[red]Lỗi: Không có danh sách proxy để kiểm tra![/red]")
        return

    output_path = os.path.join(get_current_directory(), settings['output_file'])
    results_sync = check_proxies(
        proxy_list,
        classify=settings['classify'],
        classify_type=settings['classify_type'],
        output_path=output_path,
        max_threads=settings['max_threads']
    )

    live_count = len(results_sync)
    results_title = create_rainbow_text("🎯 KẾT QUẢ KIỂM TRA PROXY 🎯")

    clear_screen()
    show_header()
    results_table = Table(show_header=True, header_style="bold magenta",
                         border_style="bold bright_magenta", box=DOUBLE_EDGE, highlight=True)

    results_table.add_column("📊 Loại", style="bold cyan", width=20, justify="center")
    results_table.add_column("🔢 Số Lượng", style="bold white", width=15, justify="center")
    results_table.add_column("📈 Tỷ Lệ", style="bold yellow", width=15, justify="center")
    results_table.add_column("📋 Trạng Thái", style="bold", width=35, justify="center")

    total = len(proxy_list)
    dead_count = total - live_count
    live_rate = (live_count / total * 100) if total > 0 else 0
    dead_rate = (dead_count / total * 100) if total > 0 else 0

    results_table.add_row("📦 Tổng Proxy", f"{total:,}", "---", "🔍 Đã kiểm tra")
    results_table.add_row("✅ Proxy Sống", f"[bright_green]{live_count:,}[/bright_green]",
                         f"[bright_green]{live_rate:.1f}%[/bright_green]",
                         "🚀 Hoạt động tốt" if live_count > 0 else "⚫ Không có")
    results_table.add_row("❌ Proxy Chết", f"[bright_red]{dead_count:,}[/bright_red]",
                         f"[bright_red]{dead_rate:.1f}%[/bright_red]",
                         "💀 Không hoạt động" if dead_count > 0 else "⚫ Không có")

    console.print(Panel(results_title, border_style="bold bright_green", padding=(1, 2)))
    console.print(results_table)

    console.input(f"\n[cyan]Nhấn Enter để quay lại menu chính...[/cyan]")

async def handle_proxy_collection(proxy_manager):
    user_settings = load_user_settings()
    menu2_settings = user_settings.get('menu2_check_settings', {})
    
    if menu2_settings:
        auto_check = menu2_settings.get('auto_check', True)
        classify_output = menu2_settings.get('classify', True)
        console.print(f"[green]✓ Sử dụng cấu hình đã lưu: auto_check={auto_check}, classify_output={classify_output}[/green]")
    else:
        auto_check = get_yes_no_input("[cyan]Tự động kiểm tra proxy sau khi thu thập? (y/n): [/cyan]")
        classify_output = get_yes_no_input("[cyan]Phân loại kết quả? (y/n): [/cyan]")
        if get_yes_no_input("\n[cyan]Lưu cấu hình này cho lần sau? (y/n): [/cyan]"):
            menu2_settings = {
                'auto_check': auto_check,
                'classify_output': classify_output
            }
            user_settings['menu2_check_settings'] = menu2_settings
            save_user_settings(user_settings)
            console.print("[green]✓ Đã lưu cấu hình![/green]")
            time.sleep(0.5)
        
        clear_screen()
        console.print(create_rainbow_text("✨ Bắt đầu thu thập proxy ✨"))
    
    proxy_count = int(console.input("[cyan]Nhập số lượng proxy muốn lấy (mặc định 100): [/cyan]") or "100")
    proxy_types = ['http', 'https'] if get_yes_no_input("[cyan]Lấy cả HTTP và HTTPS? (y/n): [/cyan]") else ['http']

    console.print("\n[cyan]Thu thập proxy từ nhiều nguồn...[/cyan]")

    collector = ProxyCollector(console)
    proxies = await collector.collect_all()

    if not proxies:
        console.print("\n[red on black]❌ Không tìm thấy proxy nào![/red on black]")
        console.input("\n[cyan]Nhấn Enter để quay lại menu chính...[/cyan]")
        return

    collect_text = create_rainbow_text(f"Đã thu thập được {len(proxies)} proxy!")
    console.print(f"\n{collect_text}")

    if auto_check or get_yes_no_input("\n[cyan]Bạn có muốn kiểm tra các proxy vừa thu thập không? (y/n): [/cyan]"):
        try:
            await handle_proxy_check(proxy_manager, source_type='memory', proxy_list=proxies)
        except KeyboardInterrupt:
            console.print(f"\n[yellow on black]⚠️ Đã hủy thao tác kiểm tra proxy![/yellow on black]")
    else:
        save_path = os.path.join(get_current_directory(), 'collected_proxies.txt')
        with open(save_path, 'w') as f:
            for proxy in proxies:
                f.write(f"{proxy}\n")
        console.print(f"\n[green]Đã lưu danh sách proxy vào:[/green] [white]{save_path}[/white]")
        console.input("\n[cyan]Nhấn Enter để quay lại menu chính...[/cyan]")

def run_proxy_check(proxy_file, settings):
    console.print(f"\n[yellow]Đang kiểm tra proxy với {settings['max_threads']} luồng...\n[/yellow]")

    with open(proxy_file, 'r', encoding='utf-8') as f:
        proxies = [line.strip() for line in f if line.strip()]

    output_path = os.path.join(get_current_directory(), settings['output_file'])

    results = check_proxies(
        proxies,
        settings['classify'],
        settings.get('classify_option', 'n'),
        output_path,
        settings['max_threads']
    )
    session = load_session_data()
    session['last_checked_output'] = output_path
    save_session_data(session)
    live_count = len(results)

    results_title = create_rainbow_text("🎯 KẾT QUẢ KIỂM TRA PROXY 🎯")

    clear_screen()
    results_table = Table(show_header=True, header_style="bold magenta",
                         border_style="bold bright_magenta", box=DOUBLE_EDGE, highlight=True)

    results_table.add_column("📊 Loại", style="bold cyan", width=20, justify="center")
    results_table.add_column("🔢 Số Lượng", style="bold white", width=15, justify="center")
    results_table.add_column("📈 Tỷ Lệ", style="bold yellow", width=15, justify="center")
    results_table.add_column("📋 Trạng Thái", style="bold", width=20, justify="center")

    total = len(proxies)
    dead_count = total - live_count
    live_rate = (live_count / total * 100) if total > 0 else 0
    dead_rate = (dead_count / total * 100) if total > 0 else 0

    results_table.add_row("📦 Tổng Proxy", f"{total:,}", "---", "🔍 Đã kiểm tra")
    results_table.add_row("✅ Proxy Sống", f"[bright_green]{live_count:,}[/bright_green]",
                         f"[bright_green]{live_rate:.1f}%[/bright_green]",
                         "🚀 Hoạt động tốt" if live_count > 0 else "⚫ Không có")
    results_table.add_row("❌ Proxy Chết", f"[bright_red]{dead_count:,}[/bright_red]",
                         f"[bright_red]{dead_rate:.1f}%[/bright_red]",
                         "💀 Không hoạt động" if dead_count > 0 else "⚫ Không có")

    if live_count > 0:
        results_table.add_row("💾 File Kết Quả", f"[green]Đã lưu[/green]", "---", f"[white]📁 {output_path}[/white]")

    clear_screen()
    show_header()
    console.print(Panel(results_title, border_style="bold bright_green", padding=(1, 2)))
    console.print(results_table)

def run_proxy_check_from_memory(proxy_list, settings):
    console.print(f"\n[yellow]Đang kiểm tra proxy với {settings['max_threads']} luồng...\n[/yellow]")

    output_path = os.path.join(get_current_directory(), settings['output_file'])

    results = check_proxies(
        proxy_list,
        settings['classify'],
        settings.get('classify_option', 'n'),
        output_path,
        settings['max_threads']
    )
    live_count = len(results)

    results_title = create_rainbow_text("🎯 KẾT QUẢ KIỂM TRA PROXY 🎯")

    results_table = Table(show_header=True, header_style="bold magenta",
                         border_style="bold bright_magenta", box=DOUBLE_EDGE, highlight=True)

    results_table.add_column("📊 Loại", style="bold cyan", width=20, justify="center")
    results_table.add_column("🔢 Số Lượng", style="bold white", width=15, justify="center")
    results_table.add_column("📈 Tỷ Lệ", style="bold yellow", width=15, justify="center")
    results_table.add_column("📋 Trạng Thái", style="bold", width=35, justify="center")

    total = len(proxy_list)
    dead_count = total - live_count
    live_rate = (live_count / total * 100) if total > 0 else 0
    dead_rate = (dead_count / total * 100) if total > 0 else 0

    results_table.add_row("📦 Tổng Proxy", f"{total:,}", "---", "🔍 Đã kiểm tra")
    results_table.add_row("✅ Proxy Sống", f"[bright_green]{live_count:,}[/bright_green]",
                         f"[bright_green]{live_rate:.1f}%[/bright_green]",
                         "🚀 Hoạt động tốt" if live_count > 0 else "⚫ Không có")
    results_table.add_row("❌ Proxy Chết", f"[bright_red]{dead_count:,}[/bright_red]",
                         f"[bright_red]{dead_rate:.1f}%[/bright_red]",
                         "💀 Không hoạt động" if dead_count > 0 else "⚫ Không có")

    if live_count > 0:
        results_table.add_row("💾 File Kết Quả", f"[green]Đã lưu[/green]", "---", f"[white]📁 {output_path}[/white]")

    console.print("\n" + "="*80)
    console.print(Panel(results_title, border_style="bold bright_green", padding=(1, 2)))
    console.print(results_table)
    console.print("="*80)

PROXY_SERVER_HOST = '127.0.0.1'
PROXY_SERVER_PORT = 8888
PROXY_LIST_FILE = 'proxy_live.txt'

class RotatingProxyServer:
    def __init__(self, host, port, console, proxy_list_file=None):
        self.host = host
        self.port = port
        self.console = console
        self.active_connections = 0
        self.total_bytes_transferred = 0
        self.logs = []
        self.start_time = datetime.now()
        self.is_running = False
        self.server = None
        self.proxy_list_file = proxy_list_file or PROXY_LIST_FILE
        self.proxies = self.load_proxies()
        self.dashboard_title = create_rainbow_text("◆ Bảng điều khiển Proxy Server ◆")
        self.log_rows = 3

    def add_log(self, message):
        timestamp = datetime.now().strftime('%H:%M:%S')
        color = "bright_white"
        if "❌" in message or "‼️" in message:
            color = "bright_red"
        elif "➕" in message or "↪️" in message:
            color = "bright_blue"
        elif "✅" in message or "♻️" in message:
            color = "bright_green"
        elif "⚠️" in message:
            color = "bright_yellow"
        log_text = Text()
        log_text.append(f"[{timestamp}] ", style="bright_black")
        log_text.append(message, style=f"bold {color}")
        self.logs.append(log_text)
        if len(self.logs) > 10:
            self.logs.pop(0)

    def mark_proxy_failed(self, proxy):
        proxy['fail_count'] += 1
        if proxy['fail_count'] >= 3:
            proxy['status'] = 'bad'
            proxy['last_fail_time'] = time.time()
            self.add_log(f"🚫 Proxy {proxy['address']} tạm khóa trong 5 phút.")

    def load_proxies(self):
        if not os.path.exists(self.proxy_list_file):
            self.add_log(f"❌ Lỗi: Không tìm thấy file '{self.proxy_list_file}'.")
            return []
        with open(self.proxy_list_file, 'r') as f:
            proxies = [{'address': line.strip(), 'status': 'good', 'fail_count': 0, 'last_fail_time': 0}
                       for line in f if line.strip()]
            self.add_log(f"✅ Đã tải {len(proxies)} proxy từ {self.proxy_list_file}")
            return proxies

    def get_proxy(self):
        now = time.time()
        for p in self.proxies:
            if p['status'] == 'bad' and now - p['last_fail_time'] > 300:
                p['status'] = 'good'
                p['fail_count'] = 0
                self.add_log(f"♻️  Proxy {p['address']} đã được hồi sinh.")

        good_proxies = [p for p in self.proxies if p['status'] == 'good']
        if not good_proxies:
            self.add_log("⚠️  Không còn proxy tốt nào, thử reset tất cả...")
            for p in self.proxies:
                p['status'] = 'good'
            good_proxies = self.proxies
            if not good_proxies:
                return None
        return random.choice(good_proxies)

    async def transfer_data(self, reader, writer):
        while True:
            try:
                data = await asyncio.wait_for(reader.read(4096), timeout=60.0)
                if not data:
                    break
                self.total_bytes_transferred += len(data)
                writer.write(data)
                await writer.drain()
            except (asyncio.CancelledError, ConnectionResetError):
                break
            except Exception as e:
                self.add_log(f"‼️ Lỗi transfer: {e}")
                break
        if not writer.is_closing():
            writer.close()
            await writer.wait_closed()

    async def handle_client(self, client_reader, client_writer):
        self.active_connections += 1
        addr = client_writer.get_extra_info('peername')
        self.add_log(f"➕ Kết nối mới từ: {addr[0]}:{addr[1]}")
        try:
            request_line_bytes = await asyncio.wait_for(client_reader.readline(), timeout=5.0)
            if not request_line_bytes: return

            request_line = request_line_bytes.decode('utf-8', errors='ignore').strip()
            parts = request_line.split()
            if len(parts) != 3: return

            method, target, _ = parts

            if method.upper() == 'CONNECT':
                target_host, _ = target.split(':')
                while await client_reader.readline() != b'\r\n': pass

                proxy = self.get_proxy()
                if not proxy:
                    self.add_log("❌ Hết proxy để sử dụng.")
                    return

                try:
                    proxy_host, proxy_port = proxy['address'].split(':')
                except:
                    self.add_log(f"❌ Proxy format không hợp lệ: {proxy['address']}")
                    self.mark_proxy_failed(proxy)
                    return
                
                self.add_log(f"↪️  {target_host} -> {proxy['address']}")
                try:
                    proxy_reader, proxy_writer = await asyncio.open_connection(proxy_host, int(proxy_port))
                    proxy_writer.write(f"CONNECT {target} HTTP/1.1\r\nHost: {target_host}\r\n\r\n".encode())
                    await proxy_writer.drain()
                    response_line = await proxy_reader.readline()
                    if b"200" in response_line:
                        client_writer.write(b"HTTP/1.1 200 Connection Established\r\n\r\n")
                        await client_writer.drain()
                        await asyncio.gather(
                            asyncio.create_task(self.transfer_data(client_reader, proxy_writer)),
                            asyncio.create_task(self.transfer_data(proxy_reader, client_writer))
                        )
                    else:
                        self.add_log(f"❌ Proxy {proxy['address']} từ chối kết nối")
                        self.mark_proxy_failed(proxy)
                except Exception as e:
                    self.add_log(f"❌ Lỗi kết nối proxy {proxy['address']}: {e}")
                    self.mark_proxy_failed(proxy)
            else:
                proxy = self.get_proxy()
                if not proxy:
                    self.add_log("❌ Hết proxy cho yêu cầu HTTP.")
                    return

                try:
                    proxy_host, proxy_port = proxy['address'].split(':')
                except:
                    self.add_log(f"❌ Proxy format không hợp lệ: {proxy['address']}")
                    self.mark_proxy_failed(proxy)
                    return
                
                self.add_log(f"↪️  HTTP {target} -> {proxy['address']}")
                try:
                    proxy_reader, proxy_writer = await asyncio.open_connection(proxy_host, int(proxy_port))
                    proxy_writer.write(request_line_bytes)
                    while True:
                        line_bytes = await asyncio.wait_for(client_reader.readline(), timeout=2.0)
                        proxy_writer.write(line_bytes)
                        if line_bytes == b'\r\n': break
                    await proxy_writer.drain()
                    await asyncio.gather(
                        asyncio.create_task(self.transfer_data(client_reader, proxy_writer)),
                        asyncio.create_task(self.transfer_data(proxy_reader, client_writer))
                    )
                except Exception as e:
                    self.add_log(f"❌ Lỗi HTTP proxy {proxy['address']}: {e}")
                    self.mark_proxy_failed(proxy)
        except asyncio.TimeoutError:
            self.add_log(f"⌛ Timeout từ {addr[0]}")
        except Exception as e:
            self.add_log(f"‼️ Lỗi client {addr[0]}: {e}")
        finally:
            self.add_log(f"➖ Đóng kết nối từ: {addr[0]}")
            self.active_connections -= 1
            if not client_writer.is_closing():
                client_writer.close()
                await client_writer.wait_closed()

    def _generate_dashboard(self):
        uptime = str(datetime.now() - self.start_time).split('.')[0]
        status_style, status_text = ("bold green", "ĐANG CHẠY") if self.is_running else ("bold red", "ĐÃ DỪNG")
        info_text = Text()
        info_text.append("🟢 Trạng thái: ", style="bold bright_white")
        info_text.append(status_text, style=status_style)
        info_text.append("\n")
        if self.server:
            formatted_addrs = []
            for sock in self.server.sockets:
                s = sock.getsockname()
                try:
                    host, port = s[0], s[1]
                except Exception:
                    host, port = str(s), ""
                formatted_addrs.append(f"{host}:{port}")
            addrs = ', '.join(formatted_addrs)
            info_text.append("📍 Địa chỉ: ", style="bold bright_white")
            info_text.append(addrs, style="bold bright_cyan")
            info_text.append("\n")
        info_text.append("⏱ Thời gian hoạt động: ", style="bold bright_white")
        info_text.append(uptime, style="bold bright_yellow")
        info_text.append("\n")
        info_text.append("🔗 Kết nối hoạt động: ", style="bold bright_white")
        info_text.append(str(self.active_connections), style="bold bright_blue")
        info_text.append("\n")
        info_text.append("📦 Dung lượng đã truyền: ", style="bold bright_white")
        info_text.append(f"{self.total_bytes_transferred / 1024 / 1024:.2f} MB", style="bold bright_magenta")

        log_table = Table(title="Nhật ký kết nối", title_style="bold bright_white", box=None, show_header=False)
        log_table.add_column()
        rows = getattr(self, "log_rows", 6)
        logs_to_show = list(self.logs[-rows:])
        while len(logs_to_show) < rows:
            logs_to_show.insert(0, " ")
        for log in logs_to_show:
            log_table.add_row(log)

        main_panel = Panel(
            Group(Align.center(info_text), "\n", Align.center(log_table)),
            title=self.dashboard_title,
            border_style="bold bright_magenta",
            padding=(1, 2)
        )

        footer = Align.left(Text("⚠  Nhấn Ctrl + C để dừng server", style="bold bright_yellow"))
        return Group(main_panel, footer)

    async def start(self):
        if not self.proxies:
            self.console.print("[red]Không có proxy nào để khởi động server.[/red]")
            return

        self.is_running = True
        self.server = await asyncio.start_server(self.handle_client, self.host, self.port)
        refresher_task = None
        try:
            self.console.clear()
            with Live(self._generate_dashboard(), console=self.console, screen=False, refresh_per_second=5, auto_refresh=False) as live:
                async def refresher():
                    while self.is_running:
                        live.update(self._generate_dashboard(), refresh=True)
                        await asyncio.sleep(1)
                refresher_task = asyncio.create_task(refresher())
                await self.server.serve_forever()
        except (asyncio.CancelledError, KeyboardInterrupt):
            pass
        finally:
            self.is_running = False
            if refresher_task: refresher_task.cancel()
            if self.server:
                self.server.close()
                await self.server.wait_closed()


async def start_proxy_server():
    """Khởi động proxy server xoay vòng với màn hình giải thích."""
    clear_screen()

    explanation_text = (
        "[bold bright_magenta]◆ PROXY SERVER LÀ GÌ? ◆[/bold bright_magenta]\n\n"
        "[bright_green]Đây là một server proxy cá nhân chạy ngay trên máy của bạn.[/bright_green]\n\n"
        "[bold bright_yellow]1. Nó làm gì?[/bold bright_yellow]\n"
        "   - Server sẽ tự động lấy một proxy ngẫu nhiên từ [bold cyan]danh sách proxy đã kiểm tra gần nhất[/bold cyan] của bạn (hoặc từ tệp bạn chỉ định).\n"
        "   - Mọi kết nối internet từ trình duyệt/ứng dụng của bạn sẽ được \"xoay vòng\" qua các proxy này.\n\n"
        "[bold bright_yellow]2. Làm thế nào để sử dụng?[/bold bright_yellow]\n"
        "   - Sau khi server khởi động, bạn cần vào cài đặt của trình duyệt (Chrome, Firefox,...).\n"
        "   - Tìm đến phần cài đặt mạng (Network/Proxy Settings).\n"
        "   - Thiết lập proxy HTTP/HTTPS thành:\n"
        f"     - [bold]Địa chỉ (Host/IP):[/bold] [cyan]{PROXY_SERVER_HOST}[/cyan]\n"
        f"     - [bold]Cổng (Port):[/bold] [cyan]{PROXY_SERVER_PORT}[/cyan]\n\n"
        "[bold bright_yellow]3. Lợi ích là gì?[/bold bright_yellow]\n"
        "   - [bold]Ẩn địa chỉ IP thật:[/bold] Các trang web sẽ thấy IP của proxy, không phải IP của bạn.\n"
        "   - [bold]Tự động đổi IP:[/bold] Server liên tục xoay vòng qua danh sách proxy, tăng tính ẩn danh.\n\n"
        "[bold bright_green]Mẹo:[/bold bright_green] [green]Hãy chạy chức năng [1] để tạo danh sách proxy chất lượng và lưu lại; server sẽ tự dùng danh sách đã kiểm tra gần nhất hoặc tệp bạn chỉ định.[/green]"
    )

    console.print(Panel(explanation_text, title="Hướng dẫn sử dụng", border_style="cyan", padding=(1, 2)))
    console.input("\n[bold bright_cyan]Nhấn [Enter] để khởi động server...[/bold bright_cyan]")
    clear_screen()

    proxy_file_to_use = None
    session = load_session_data()
    if isinstance(session, dict):
        last_out = session.get('last_checked_output')
        if last_out and os.path.exists(last_out):
            proxy_file_to_use = last_out
    if not proxy_file_to_use and os.path.exists(PROXY_LIST_FILE):
        proxy_file_to_use = PROXY_LIST_FILE
    if not proxy_file_to_use:
        file_input = console.input("\n[bold bright_cyan]Nhập tên file hoặc đường dẫn danh sách proxy (.txt): [/bold bright_cyan]").strip()
        if os.path.exists(file_input) and validate_proxy_file(file_input):
            proxy_file_to_use = file_input
    if not proxy_file_to_use:
        console.print(Panel("[bold red]Lỗi: Không tìm thấy danh sách proxy để khởi động server.[/bold red]\n[yellow]Hãy chạy chức năng 'Kiểm tra proxy' (mục 1) hoặc cung cấp đường dẫn file hợp lệ.[/yellow]", title="Lỗi", border_style="red"))
        console.input("\n[cyan]Nhấn Enter để quay lại menu chính...[/cyan]")
        return

    server = RotatingProxyServer(host=PROXY_SERVER_HOST, port=PROXY_SERVER_PORT, console=console, proxy_list_file=proxy_file_to_use)
    try:
        await server.start()
    except Exception as e:
        console.print(f"[bold red]Lỗi không xác định khi chạy server: {e}[/bold red]")

    console.print("\n[green]Proxy Server đã tắt.[/green]")
    console.input("\n[cyan]Nhấn Enter để quay lại menu chính...[/cyan]")

async def scan_ip_range_for_proxies(start_ip, end_ip, ports, timeout, max_threads, results_queue, stop_event, pause_event, stats_dict, stats_lock, seen_proxies, dead_hashes, proxy_hash):
    def ip_to_int(ip):
        parts = ip.split('.')
        return (int(parts[0]) << 24) + (int(parts[1]) << 16) + (int(parts[2]) << 8) + int(parts[3])
    
    def int_to_ip(num):
        return f"{(num >> 24) & 255}.{(num >> 16) & 255}.{(num >> 8) & 255}.{num & 255}"
    
    def check_port_sync(ip, port):
        sock = None
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.3)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            result = sock.connect_ex((ip, port))
            return result == 0
        except:
            return False
        finally:
            if sock:
                try:
                    sock.close()
                except:
                    pass
    
    start_num = ip_to_int(start_ip)
    end_num = ip_to_int(end_ip)
    
    executor = ThreadPoolExecutor(max_workers=max_threads)
    
    try:
        async def check_ip_port(ip, port):
            if stop_event.is_set():
                return None
            
            if not pause_event.is_set():
                while not pause_event.is_set():
                    await asyncio.sleep(0.1)
                    if stop_event.is_set():
                        return None
            
            proxy_str = f"{ip}:{port}"
            if proxy_str in seen_proxies:
                return None
            
            if proxy_hash(proxy_str) in dead_hashes:
                return None
            
            try:
                loop = asyncio.get_event_loop()
                is_open = await loop.run_in_executor(executor, check_port_sync, ip, port)
                
                with stats_lock:
                    stats_dict['scanned'] += 1
                
                if is_open:
                    with stats_lock:
                        stats_dict['ports_open'] += 1
                    
                    result = await quick_detect_proxy_type(proxy_str, timeout)
                    
                    with stats_lock:
                        stats_dict['proxy_attempts'] += 1
                    
                    if result:
                        proxy_type, response_time = result
                        if response_time <= timeout:
                            seen_proxies.add(proxy_str)
                            return {'proxy': proxy_str, 'type': proxy_type, 'ip': ip, 'port': port, 'response_time': response_time}
                        else:
                            with stats_lock:
                                stats_dict['validation_failed'] += 1
                            p_hash = proxy_hash(proxy_str)
                            dead_hashes.add(p_hash)
                    else:
                        with stats_lock:
                            stats_dict['validation_failed'] += 1
                        p_hash = proxy_hash(proxy_str)
                        dead_hashes.add(p_hash)
                else:
                    p_hash = proxy_hash(proxy_str)
                    dead_hashes.add(p_hash)
            except Exception:
                pass
            return None
        
        semaphore = asyncio.Semaphore(max_threads)
        
        async def scan_with_semaphore(ip, port):
            async with semaphore:
                result = await check_ip_port(ip, port)
                if result:
                    await results_queue.put(result)
        
        tasks = []
        batch_size = max_threads * 50
        
        import random
        ip_nums = list(range(start_num, end_num + 1))
        random.shuffle(ip_nums)
        
        for ip_num in ip_nums:
            if stop_event.is_set():
                break
            ip = int_to_ip(ip_num)
            for port in ports:
                if stop_event.is_set():
                    break
                tasks.append(scan_with_semaphore(ip, port))
                if len(tasks) >= batch_size:
                    await asyncio.gather(*tasks, return_exceptions=True)
                    tasks = []
        
        if tasks:
            await asyncio.gather(*tasks, return_exceptions=True)
    
    finally:
        executor.shutdown(wait=False)

async def quick_detect_proxy_type(proxy_str, timeout):
    try:
        ip, port = proxy_str.split(':')
        port = int(port)
        
        proxy_dict = {'http': f"http://{proxy_str}"}
        short_timeout = min(timeout/1000.0, 2.0)
        
        start = time.time()
        try:
            async with httpx.AsyncClient(
                proxies=proxy_dict, 
                timeout=short_timeout,
                follow_redirects=False,
                verify=False,
                limits=httpx.Limits(max_connections=200, max_keepalive_connections=50)
            ) as client:
                response = await client.get('http://icanhazip.com')
                response_time = int((time.time() - start) * 1000)
                if response.status_code == 200:
                    validated_ip = _validate_ip_response(response.text)
                    if validated_ip:
                        return ('HTTP', response_time)
        except:
            pass
        
        return None
    except:
        pass
    return None

async def get_proxy_country(proxy_str):
    try:
        ip = proxy_str.split(':')[0]
        geo_data = await get_detailed_geolocation(ip)
        if geo_data:
            return geo_data.get('country_code', 'Unknown')
    except:
        pass
    return 'Unknown'

async def handle_proxy_scanner():
    clear_screen()
    console.print(create_rainbow_text("🔎 QUÉT VÀ TÌM PROXY MỚI 🔎"))
    
    user_settings = load_user_settings()
    menu5_settings = user_settings.get('menu5_scanner_settings', {})
    
    if menu5_settings:
        settings = {
            'max_threads': menu5_settings.get('max_threads', 100),
            'timeout': menu5_settings.get('timeout', 2000),
            'output_file': menu5_settings.get('output_file', 'scanned_proxies.txt'),
            'classify': menu5_settings.get('classify', True),
            'classify_type': menu5_settings.get('classify_type', 'protocol'),
            'auto_clean': menu5_settings.get('auto_clean', True)
        }
        console.print(f"[green]✓ Sử dụng cấu hình đã lưu: {settings['max_threads']} luồng, {settings['timeout']}ms timeout[/green]")
    else:
        console.print("\n[yellow]⚙️ Cấu hình Scanner[/yellow]")
        try:
            max_threads = int(console.input("[cyan]Nhập số luồng scan (mặc định 100): [/cyan]") or "100")
            max_threads = max(1, min(max_threads, 1000))
        except:
            max_threads = 100
        
        try:
            timeout = int(console.input("[cyan]Nhập timeout cho mỗi kết nối (ms, mặc định 2000): [/cyan]") or "2000")
            timeout = max(100, min(timeout, 60000))
        except:
            timeout = 2000
        output_file = console.input("[cyan]Tên file kết quả (mặc định scanned_proxies.txt): [/cyan]") or "scanned_proxies.txt"
        classify = get_yes_no_input("[cyan]Phân loại proxy? (y/n): [/cyan]")
        
        classify_type = 'protocol'
        if classify:
            console.print("\n[cyan]Phân loại theo:[/cyan]")
            console.print("[white]1. Loại protocol (HTTP/HTTPS/SOCKS4/SOCKS5)[/white]")
            console.print("[white]2. Quốc gia[/white]")
            classify_choice = console.input("[cyan]Nhập lựa chọn (1-2): [/cyan]").strip()
            classify_type = 'country' if classify_choice == '2' else 'protocol'
        
        console.print("\n[cyan]⚠️  Tự động dọn dẹp log proxy DIE:[/cyan]")
        console.print("[white]- Xóa log sau 7 ngày[/white]")
        console.print("[white]- Xóa khi file > 50MB[/white]")
        auto_clean = get_yes_no_input("[cyan]Bật tự động dọn dẹp? (y/n): [/cyan]")
        
        settings = {
            'max_threads': max_threads,
            'timeout': timeout,
            'output_file': output_file,
            'classify': classify,
            'classify_type': classify_type,
            'auto_clean': auto_clean
        }
        
        if get_yes_no_input("\n[cyan]Lưu cấu hình này cho lần sau? (y/n): [/cyan]"):
            user_settings['menu5_scanner_settings'] = settings
            save_user_settings(user_settings)
            console.print("[green]✓ Đã lưu cấu hình![/green]")
            time.sleep(0.5)
    
    clear_screen()
    
    output_path = os.path.join(get_current_directory(), settings['output_file'])
    dead_log_path = os.path.join(get_current_directory(), '.dead_proxies.db')
    seen_proxies = set()
    dead_hashes = set()
    
    TTL_DAYS = 7
    MAX_FILE_SIZE_MB = 50
    
    def proxy_hash(proxy_str):
        return hash(proxy_str) & 0xFFFFFFFF
    
    def write_dead_db(file_path, hashes_set, ttl_days=7):
        file_path = os.path.abspath(file_path)
        dir_path = os.path.dirname(file_path)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as f:
            f.write(b'DEAD')
            f.write((1).to_bytes(4, 'little'))
            f.write(int(time.time()).to_bytes(8, 'little'))
            f.write(len(hashes_set).to_bytes(4, 'little'))
            f.write(ttl_days.to_bytes(4, 'little'))
            f.write(b'\x00' * 8)
            for hash_int in hashes_set:
                f.write(hash_int.to_bytes(4, 'little'))
            f.flush()
            os.fsync(f.fileno())
    
    def read_dead_db(file_path):
        try:
            with open(file_path, 'rb') as f:
                magic = f.read(4)
                if magic != b'DEAD':
                    return None, None, None
                version = int.from_bytes(f.read(4), 'little')
                created = int.from_bytes(f.read(8), 'little')
                count = int.from_bytes(f.read(4), 'little')
                ttl_days = int.from_bytes(f.read(4), 'little')
                f.read(8)
                hashes = set()
                for _ in range(count):
                    hash_bytes = f.read(4)
                    if len(hash_bytes) == 4:
                        hashes.add(int.from_bytes(hash_bytes, 'little'))
                return created, ttl_days, hashes
        except:
            return None, None, None
    
    def append_dead_hash(file_path, hash_int, ttl_days=7):
        try:
            if not os.path.exists(file_path):
                write_dead_db(file_path, {hash_int}, ttl_days)
            else:
                with open(file_path, 'r+b') as f:
                    f.seek(12)
                    count_bytes = f.read(4)
                    current_count = int.from_bytes(count_bytes, 'little')
                    f.seek(12)
                    f.write((current_count + 1).to_bytes(4, 'little'))
                    f.seek(0, 2)
                    f.write(hash_int.to_bytes(4, 'little'))
        except:
            pass
    
    if os.path.exists(output_path):
        try:
            with open(output_path, 'r', encoding='utf-8') as f:
                for line in f:
                    proxy_line = line.strip()
                    if proxy_line:
                        proxy = proxy_line.split('|')[0].strip() if '|' in proxy_line else proxy_line
                        seen_proxies.add(proxy)
        except:
            pass
    
    should_load = True
    if settings.get('auto_clean', True):
        if os.path.exists(dead_log_path):
            try:
                file_size_mb = os.path.getsize(dead_log_path) / 1024 / 1024
                if file_size_mb > MAX_FILE_SIZE_MB:
                    os.remove(dead_log_path)
                    should_load = False
                else:
                    created, ttl_days, hashes = read_dead_db(dead_log_path)
                    if created:
                        days_old = (time.time() - created) / 86400
                        if days_old > TTL_DAYS:
                            os.remove(dead_log_path)
                            should_load = False
            except:
                pass
    
    if should_load and os.path.exists(dead_log_path):
        try:
            created, ttl_days, hashes = read_dead_db(dead_log_path)
            if hashes:
                dead_hashes = hashes
            else:
                os.remove(dead_log_path)
        except:
            try:
                if os.path.exists(dead_log_path):
                    os.remove(dead_log_path)
            except:
                pass
    
    datacenter_ranges = [
        ('5.8.0.0', '5.8.255.255'),
        ('5.188.0.0', '5.188.255.255'),
        ('23.88.0.0', '23.95.255.255'),
        ('31.131.0.0', '31.131.255.255'),
        ('37.9.0.0', '37.9.255.255'),
        ('45.8.0.0', '45.15.255.255'),
        ('46.8.0.0', '46.8.255.255'),
        ('62.84.0.0', '62.84.255.255'),
        ('77.83.0.0', '77.83.255.255'),
        ('78.24.0.0', '78.31.255.255'),
        ('80.78.0.0', '80.78.255.255'),
        ('82.146.0.0', '82.146.255.255'),
        ('85.195.0.0', '85.195.255.255'),
        ('89.108.0.0', '89.108.255.255'),
        ('91.90.0.0', '91.95.255.255'),
        ('94.140.0.0', '94.143.255.255'),
        ('95.140.0.0', '95.143.255.255'),
        ('103.8.0.0', '103.15.255.255'),
        ('104.16.0.0', '104.31.255.255'),
        ('109.94.0.0', '109.95.255.255'),
        ('128.140.0.0', '128.143.255.255'),
        ('138.68.0.0', '138.68.255.255'),
        ('139.59.0.0', '139.59.255.255'),
        ('142.93.0.0', '142.93.255.255'),
        ('143.198.0.0', '143.198.255.255'),
        ('157.230.0.0', '157.230.255.255'),
        ('159.89.0.0', '159.89.255.255'),
        ('165.22.0.0', '165.22.255.255'),
        ('167.71.0.0', '167.71.255.255'),
        ('178.62.0.0', '178.62.255.255'),
        ('185.4.0.0', '185.7.255.255'),
        ('188.166.0.0', '188.166.255.255'),
        ('194.67.0.0', '194.67.255.255'),
        ('206.189.0.0', '206.189.255.255'),
    ]
    
    proxy_ports_priority = [3128, 8080, 1080, 80, 8888, 9050, 8118, 3129, 8081, 9999, 4145, 443, 8000]
    
    ip_ranges = datacenter_ranges
    common_ports = proxy_ports_priority
    
    results_queue = asyncio.Queue()
    stop_event = asyncio.Event()
    pause_event = asyncio.Event()
    found_proxies = []
    is_paused = [False]
    stats_dict = {
        'scanned': 0,
        'total_ips': 0,
        'ports_open': 0,
        'proxy_attempts': 0,
        'validation_failed': 0
    }
    stats_lock = Lock()
    file_lock = Lock()
    
    console.print("\n")
    notes_content = Text()
    notes_content.append("🔍 MENU 5 - PROXY SCANNER\n\n", style="bold cyan")
    notes_content.append("Chức năng:\n", style="bold yellow")
    notes_content.append("• Tool tự động GENERATE hàng triệu IP:Port\n", style="white")
    notes_content.append("• Scan & test từng cái để tìm proxy LIVE\n", style="white")
    notes_content.append("• Lưu proxy live vào file ngay khi tìm thấy\n\n", style="white")
    
    notes_content.append("📊 Các chỉ số hiển thị:\n", style="bold yellow")
    notes_content.append("• ", style="white")
    notes_content.append("Checks", style="bold cyan")
    notes_content.append(": Tổng số IP:Port đã scan (port check)\n", style="white")
    notes_content.append("• ", style="white")
    notes_content.append("Mở", style="bold green")
    notes_content.append(": Số ports mở được (có thể kết nối)\n", style="white")
    notes_content.append("• ", style="white")
    notes_content.append("Test", style="bold yellow")
    notes_content.append(": Số lần test proxy (gửi HTTP request)\n", style="white")
    notes_content.append("• ", style="white")
    notes_content.append("Dead", style="bold red")
    notes_content.append(": Proxy test fail (không trả về IP)\n", style="white")
    notes_content.append("• ", style="white")
    notes_content.append("Live", style="bold bright_green")
    notes_content.append(": Proxy thật (đã lưu vào file)\n\n", style="white")
    
    notes_content.append("⚠️  Lưu ý quan trọng:\n", style="bold yellow")
    notes_content.append("• Tỉ lệ tìm thấy CỰC THẤP (~0.001%)\n", style="red")
    notes_content.append("• Có thể quét HÀNG TRIỆU mới thấy 1 proxy\n", style="red")
    notes_content.append("• Menu này dành cho mấy thằng bị rảnh và máy mạnh\n\n", style="red")
    
    notes_content.append("💡 Muốn proxy NHANH?\n", style="bold yellow")
    notes_content.append("→ Tăng threads lên (tầm 1000 threads là ngon :D)\n", style="bright_green")
    
    notes_content.append("⚙️  Cấu hình:\n", style="bold yellow")
    notes_content.append(f"• Luồng: {settings['max_threads']} | Timeout: {settings['timeout']}ms\n", style="white")
    notes_content.append(f"• File lưu: {settings['output_file']}\n", style="white")
    notes_content.append(f"• Điều khiển: P=Tạm dừng | Q=Dừng", style="white")
    
    notes_panel = Panel(
        notes_content,
        border_style="bold yellow",
        padding=(1, 2),
        title="📋 HƯỚNG DẪN SỬ DỤNG",
        title_align="left"
    )
    console.print(notes_panel)
    
    if not get_yes_no_input("\n[cyan]Đã hiểu & tiếp tục? (y/n): [/cyan]"):
        return
    
    clear_screen()
    
    scanner_tasks = []
    display_task = None
    keyboard_thread = None
    signal_caught = [False]
    
    def signal_handler(sig, frame):
        if not signal_caught[0]:
            signal_caught[0] = True
            console.print("\n\n[bold yellow]⚠️  Bắt tín hiệu dừng, đang lưu dữ liệu...[/bold yellow]")
            stop_event.set()
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    try:
        def keyboard_listener_thread():
            while not stop_event.is_set():
                try:
                    if msvcrt.kbhit():
                        key = msvcrt.getch().decode('utf-8', errors='ignore').lower()
                        if key == 'p':
                            is_paused[0] = not is_paused[0]
                            if is_paused[0]:
                                pause_event.clear()
                            else:
                                pause_event.set()
                        elif key == 'q':
                            stop_event.set()
                            break
                    time.sleep(0.05)
                except Exception as e:
                    time.sleep(0.05)
        
        async def display_results():
            start_time = time.time()
            last_flush_time = time.time()
            
            with Live(console=console, refresh_per_second=4) as live:
                while not stop_event.is_set():
                    try:
                        while not results_queue.empty():
                            result = results_queue.get_nowait()
                            proxy_str = result['proxy']
                            
                            if proxy_str in seen_proxies:
                                continue
                            
                            seen_proxies.add(proxy_str)
                            found_proxies.append(result)
                            
                            with file_lock:
                                try:
                                    response_time = result.get('response_time', 0)
                                    output_line = f"{proxy_str} | {response_time}ms\n"
                                    with open(output_path, 'a', encoding='utf-8') as f:
                                        f.write(output_line)
                                        f.flush()
                                except (IOError, OSError) as write_err:
                                    try:
                                        os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
                                        with open(output_path, 'a', encoding='utf-8') as f:
                                            f.write(output_line)
                                            f.flush()
                                    except:
                                        pass
                                except Exception as write_err:
                                    pass
                        
                        with stats_lock:
                            elapsed = time.time() - start_time
                            scanned = stats_dict['scanned']
                            ports_open = stats_dict['ports_open']
                            proxy_attempts = stats_dict['proxy_attempts']
                            validation_failed = stats_dict['validation_failed']
                            speed = scanned / elapsed if elapsed > 0 else 0
                        
                        status = "⏸️ TẠM DỪNG" if is_paused[0] else "▶️ ĐANG QUÉT"
                        
                        info = Text()
                        info.append(f"🎯 Live: ", style="bold white")
                        info.append(f"{len(found_proxies)}", style="bold green")
                        info.append(f" | ", style="bold white")
                        info.append(status, style="bold yellow")
                        info.append(f" | ⚡ {speed:.1f}/s", style="bold magenta")
                        info.append("\n")
                        info.append(f"📊 Checks: ", style="bold white")
                        info.append(f"{scanned:,}", style="bold cyan")
                        info.append(f" → Mở: ", style="bold white")
                        info.append(f"{ports_open:,}", style="bold green")
                        info.append(f" → Test: ", style="bold white")
                        info.append(f"{proxy_attempts:,}", style="bold yellow")
                        info.append(f" → Dead: ", style="bold white")
                        info.append(f"{validation_failed:,}", style="bold red")
                        
                        table = Table(title=info, border_style="green", show_lines=True)
                        table.add_column("IP:Port", style="cyan", width=22)
                        table.add_column("Loại", style="yellow", width=10)
                        table.add_column("Tốc độ", style="magenta", width=12)
                        table.add_column("Trạng thái", style="green", width=15)
                        
                        for p in found_proxies[-10:]:
                            rt = p.get('response_time', 0)
                            table.add_row(p['proxy'], p['type'], f"{rt}ms", "✅ OK")
                        
                        if not found_proxies:
                            table.add_row("Chưa tìm thấy proxy...", "---", "---", "⏳ Đang tìm")
                        
                        current_time = time.time()
                        if current_time - last_flush_time >= 5.0:
                            try:
                                with stats_lock:
                                    all_dead_now = dead_hashes.copy()
                                if all_dead_now:
                                    write_dead_db(dead_log_path, all_dead_now, TTL_DAYS)
                                last_flush_time = current_time
                            except Exception as e:
                                pass
                        
                        live.update(table)
                        await asyncio.sleep(0.25)
                    except asyncio.CancelledError:
                        break
                    except Exception as display_err:
                        await asyncio.sleep(0.25)
        
        pause_event.set()
        keyboard_thread = threading.Thread(target=keyboard_listener_thread, daemon=True)
        keyboard_thread.start()
        
        display_task = asyncio.create_task(display_results())
        
        for start_ip, end_ip in ip_ranges:
            if stop_event.is_set():
                break
            scanner_task = asyncio.create_task(
                scan_ip_range_for_proxies(start_ip, end_ip, common_ports, 
                                         settings['timeout'], settings['max_threads'], 
                                         results_queue, stop_event, pause_event, 
                                         stats_dict, stats_lock, seen_proxies, dead_hashes, proxy_hash)
            )
            scanner_tasks.append(scanner_task)
        
        await asyncio.gather(*scanner_tasks, return_exceptions=True)
        
    except KeyboardInterrupt:
        console.print("\n[yellow]⏸️  Đang dừng...[/yellow]")
        stop_event.set()
    finally:
        stop_event.set()
        
        for task in scanner_tasks:
            if task and not task.done():
                task.cancel()
        
        if display_task and not display_task.done():
            await asyncio.sleep(2.0)
            display_task.cancel()
        
        if keyboard_thread and keyboard_thread.is_alive():
            keyboard_thread.join(timeout=1)
        
        with stats_lock:
            final_dead = dead_hashes.copy()
        
        if found_proxies:
            try:
                with file_lock:
                    with open(output_path, 'w', encoding='utf-8') as f:
                        for p in found_proxies:
                            proxy_str = p['proxy']
                            response_time = p.get('response_time', 0)
                            f.write(f"{proxy_str} | {response_time}ms\n")
                        f.flush()
                        os.fsync(f.fileno())
            except Exception as e:
                console.print(f"[red]✗ Lỗi ghi live file: {e}[/red]")
        
        if final_dead:
            try:
                write_dead_db(dead_log_path, final_dead, TTL_DAYS)
                console.print(f"[dim cyan]💾 Đã loại trừ {len(final_dead)} proxy dead trong file .dead_proxies.db[/dim cyan]")
            except Exception as e:
                console.print(f"[red]✗ Lỗi ghi dead file: {e}[/red]")
        
        signal.signal(signal.SIGINT, signal.SIG_DFL)
        signal.signal(signal.SIGTERM, signal.SIG_DFL)
    
    clear_screen()
    console.print(create_rainbow_text("✅ HOÀN THÀNH QUÉT PROXY"))
    console.print(f"\n[green]📊 Tìm thấy: {len(found_proxies)} proxy | File: {settings['output_file']}[/green]")
    
    if found_proxies and settings['classify']:
        console.print(f"\n[cyan]Đang phân loại proxy...[/cyan]")
        
        if settings['classify_type'] == 'protocol':
            classified = {}
            for p in found_proxies:
                ptype = p['type']
                if ptype not in classified:
                    classified[ptype] = []
                rt = p.get('response_time', 0)
                classified[ptype].append(f"{p['proxy']} | {rt}ms")
            
            for ptype, proxy_lines in classified.items():
                filename = f"scanned_{ptype.lower()}.txt"
                filepath = os.path.join(get_current_directory(), filename)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write('\n'.join(proxy_lines))
                console.print(f"[green]✓ {ptype}: {len(proxy_lines)} proxy → {filename}[/green]")
        else:
            console.print("[yellow]Phân loại theo quốc gia (song song, nhanh hơn)...[/yellow]")
            
            async def get_country_batch(proxy_data):
                try:
                    country = await get_proxy_country(proxy_data['proxy'])
                    rt = proxy_data.get('response_time', 0)
                    return (country, f"{proxy_data['proxy']} | {rt}ms")
                except:
                    return ('Unknown', f"{proxy_data['proxy']} | {proxy_data.get('response_time', 0)}ms")
            
            with create_rich_progress() as progress:
                task = progress.add_task("[cyan]Đang xác định quốc gia...", total=len(found_proxies))
                
                semaphore = asyncio.Semaphore(50)
                
                async def get_country_with_sem(proxy_data):
                    async with semaphore:
                        result = await get_country_batch(proxy_data)
                        progress.advance(task)
                        return result
                
                results = await asyncio.gather(*[get_country_with_sem(p) for p in found_proxies])
            
            classified_by_country = {}
            for country, proxy_line in results:
                if country not in classified_by_country:
                    classified_by_country[country] = []
                classified_by_country[country].append(proxy_line)
            
            for country, proxy_lines in classified_by_country.items():
                filename = f"scanned_{country.lower()}.txt"
                filepath = os.path.join(get_current_directory(), filename)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write('\n'.join(proxy_lines))
                console.print(f"[green]✓ {country}: {len(proxy_lines)} proxy → {filename}[/green]")
    
    console.input("\n[cyan]Nhấn Enter để quay lại menu chính...[/cyan]")

async def schedule_tasks():
    await handle_proxy_scanner()


async def main():
    proxy_manager = ProxyManager()

    clear_screen()
    show_rainbow_message("◆ Đang khởi động Proxy Master Suite ◆".center(60), duration=1)

    await asyncio.sleep(1)

    while True:
        clear_screen()

        config = {}

        if True:
            welcome_text = create_rainbow_text("◆◆◆ CHÀO MỪNG ĐẾN VỚI PROXY MASTER SUITE ◆◆◆")

            rainbow_line = create_rainbow_text("─" * 140)

            menu_content = Text()
            menu_content.append(rainbow_line)
            menu_content.append("\n\n")
            menu_content.append(welcome_text)
            menu_content.append("\n\n")
            menu_content.append("Chọn chức năng:", style="italic bright_white")
            menu_content.append("\n\n")

            clear_screen()
            menu_content.append("【 1 】", style="bold bright_green")
            menu_content.append("  🔍  ", style=None)
            menu_content.append("Kiểm tra và phân tích proxy", style="bold bright_green")
            menu_content.append("\n")

            menu_content.append("【 2 】", style="bold bright_blue")
            menu_content.append("  📥  ", style=None)
            menu_content.append("Thu thập proxy miễn phí", style="bold bright_blue")
            menu_content.append("\n")

            menu_content.append("【 3 】", style="bold bright_magenta")
            menu_content.append("  ⚙️  ", style=None)
            menu_content.append("Cấu hình hệ thống", style="bold bright_magenta")
            menu_content.append("\n")

            menu_content.append("【 4 】", style="bold yellow")
            menu_content.append("  🌐  ", style=None)
            menu_content.append("Proxy Server", style="bold yellow")
            menu_content.append("\n")

            menu_content.append("【 5 】", style="bold cyan")
            menu_content.append("  🔎  ", style=None)
            menu_content.append("Proxy scanner", style="bold cyan")
            menu_content.append("\n")

            menu_content.append("【 6 】", style="bold bright_red")
            menu_content.append("  🚪  ", style=None)
            menu_content.append("Thoát chương trình", style="bold bright_red")
            menu_content.append("\n\n")
            menu_content.append(rainbow_line)

            menu_content = Align.center(menu_content)

            menu_panel = Panel(
                menu_content,
                border_style="bold bright_magenta",
                padding=(0, 3),
                title=create_rainbow_text("◆◆◆ MENU CHÍNH ◆◆◆"),
                title_align="center",
                width=150,
                box=DOUBLE_EDGE,
                highlight=True
            )
            console.print(menu_panel, justify="center")
            try:
                choice = console.input("\n[bold bright_cyan]◆ Nhập lựa chọn của bạn (1-6): [/bold bright_cyan]").strip()
            except (EOFError, KeyboardInterrupt):
                console.print("\n[yellow]Cảm ơn bạn đã sử dụng tool![/yellow]")
                return

        if choice == '1':
            try:
                if True:
                    show_rainbow_message("◆ Đang khởi động module kiểm tra proxy ◆".center(60), duration=2)
                    time.sleep(0.5)
                    clear_screen()

                    input_title = create_rainbow_text("◆◆◆ LỰA CHỌN PHƯƠNG THỨC NHẬP PROXY ◆◆◆")

                    input_content = Text()
                    input_content.append(input_title)
                    input_content.append("\n\n")
                    input_content.append("「 Chọn phương thức nhập proxy 」", style="italic bright_white")
                    input_content.append("\n\n")
                    input_content.append("【 1 】", style="bold bright_green")
                    input_content.append(" Mở cửa sổ chọn file (.txt)", style="bright_white")
                    input_content.append("\n")
                    input_content.append("【 2 】", style="bold bright_yellow")
                    input_content.append(" Nhập tên file hoặc đường dẫn", style="bright_white")
                    input_content.append("\n")
                    input_content.append("【 3 】", style="bold bright_blue")
                    input_content.append(" Nhập thủ công", style="bright_white")
                    input_content.append("\n\n")
                    input_content.append("⚠️  Định dạng: ip:port, mỗi proxy một dòng", style="italic yellow")

                    input_panel = Panel(
                        input_content,
                        border_style="bold bright_yellow",
                        padding=(2, 4),
                        title=create_rainbow_text("◆◆◆ BẢNG ĐIỀU KHIỂN NHẬP ◆◆◆"),
                        title_align="center",
                        box=DOUBLE_EDGE,
                        highlight=True
                    )
                    console.print(input_panel, justify="center")
                    input_choice = console.input("\n[bold bright_cyan]◆ Chọn phương thức (1, 2 hoặc 3): [/bold bright_cyan]").strip()

                    if input_choice == '1':
                        proxy_file = select_proxy_file()
                        if proxy_file and validate_proxy_file(proxy_file):
                            await handle_proxy_check(proxy_manager, 'file', proxy_file=proxy_file)
                    elif input_choice == '2':
                        proxy_file_input = console.input("\n[bold bright_cyan]◆ Nhập tên file hoặc đường dẫn: [/bold bright_cyan]").strip()
                        if os.path.exists(proxy_file_input):
                            if validate_proxy_file(proxy_file_input):
                                await handle_proxy_check(proxy_manager, 'file', proxy_file=proxy_file_input)
                        else:
                            found_path = find_file_in_common_dirs(proxy_file_input)
                            if found_path and validate_proxy_file(found_path):
                                await handle_proxy_check(proxy_manager, 'file', proxy_file=found_path)
                            else:
                                console.print(f"\n[red]✗ File không tồn tại: {proxy_file_input}[/red]")
                    elif input_choice == '3':
                        proxies = input_proxies_manually()
                        if proxies:
                            await handle_proxy_check(proxy_manager, 'memory', proxy_list=proxies)
                    else:
                        console.print("[red]Lựa chọn không hợp lệ![/red]")
            except Exception as e:
                console.print(f"\n[bold red]Đã xảy ra lỗi không mong muốn trong quá trình kiểm tra proxy: {e}[/bold red]")
                console.input("\n[cyan]Nhấn Enter để quay lại menu chính...")

        elif choice == '2':
            clear_screen()
            try:
                await get_free_proxies_async()
            except KeyboardInterrupt:
                console.print(f"\n[yellow on black]⚠️ Đã hủy thao tác thu thập proxy![/yellow on black]")
                await asyncio.sleep(1)

        elif choice == '3':
            clear_screen()
            await handle_system_config(proxy_manager)

        elif choice == '4':
            await start_proxy_server()

        elif choice == '5':
            await schedule_tasks()

        elif choice == '6':
            if get_yes_no_input("\n[yellow]Bạn có chắc muốn thoát? (y/n): [/yellow]"):
                clear_screen()
                show_header()
                console.print("\n[green]Cảm ơn bạn đã sử dụng Proxy Master Suite![/green]")
                await asyncio.sleep(1)
                break

if __name__ == "__main__":
    try:

        if not os.path.exists(os.path.join(os.path.dirname(__file__), '.deps_checked')):
            check_and_install_dependencies()
            with open(os.path.join(os.path.dirname(__file__), '.deps_checked'), 'w') as f:
                f.write('')

        try:
            asyncio.run(main())
        except RuntimeError as e:
            if "Event loop is closed" in str(e):
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                loop.run_until_complete(main())
                loop.close()
            else:
                raise

    except KeyboardInterrupt:
        console.print("\n[yellow]Đã hủy thao tác![/yellow]")
    except Exception as e:
        console.print(f"\n[red]Lỗi không mong muốn: {str(e)}[/red]")
        if "--debug" in sys.argv:
            traceback.print_exc()
    finally:
        try:
            for task in asyncio.all_tasks():
                task.cancel()
        except (RuntimeError, asyncio.CancelledError) as e:
            pass
        console.print("[green]Cảm ơn bạn đã sử dụng tool![/green]")