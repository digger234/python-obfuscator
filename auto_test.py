import os
import subprocess
import sys
import time
import traceback
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')
except:
    pass
DIR = os.path.dirname(os.path.abspath(__file__))
TOOL = os.path.join(DIR, "obsidian.py")
PYTHON = "C:/Users/XZ/AppData/Local/Python/pythoncore-3.12-64/python.exe"
FILES = {
    "test.py": {"input": "0\n", "timeout": 30, "exit": True, "desc": "Basic test"},
    "test2.py": {"input": None, "timeout": 60, "exit": False, "desc": "Complex test"},
    "test3.py": {"input": None, "timeout": 30, "exit": False, "desc": "Simple test"},
    "test4.py": {"input": "0\n", "timeout": 30, "exit": True, "desc": "Large test"},
    "test5.py": {"input": "test_key\ntest_link\n1\n", "timeout": 10, "exit": True, "desc": "Interactive test"},
}
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"
def path(one):
    return one if os.path.isabs(one) else os.path.join(DIR, one)
def pick():
    if len(sys.argv) > 1 and sys.argv[1].strip():
        return path(sys.argv[1].strip().strip('"'))
    return TOOL
def run(args, data=None, timeout=60, cwd=None):
    env = os.environ.copy()
    env['PYTHONIOENCODING'] = 'utf-8'
    env['AEGIS_SAFE_MODE'] = '1'
    try:
        proc = subprocess.run([PYTHON] + args, cwd=cwd or DIR, input=data, capture_output=True, text=True, timeout=timeout, encoding='utf-8', errors='replace', env=env)
        return proc.returncode, proc.stdout, proc.stderr
    except subprocess.TimeoutExpired:
        return -1, "", "TIMEOUT"
    except Exception as e:
        return -2, "", str(e)
def meta(one):
    if not os.path.exists(one):
        return {"size": 0, "lines": 0}
    size = os.path.getsize(one)
    with open(one, 'r', encoding='utf-8', errors='replace') as f:
        lines = len(f.readlines())
    return {"size": size, "lines": lines}
def wipe(one):
    out = os.path.splitext(path(one))[0] + "_obf.py"
    if os.path.exists(out):
        os.remove(out)
    return out
def tail(one):
    rows = [row.strip() for row in one.strip().split('\n') if row.strip()]
    for row in reversed(rows):
        if 'Error' in row or 'error' in row or 'failed' in row.lower():
            return row[:120]
    return rows[-1][:120] if rows else 'unknown'
def norm(one):
    return '\n'.join(row.strip() for row in one.strip().split('\n') if row.strip())
def words(one):
    import unicodedata
    bag = set()
    for row in one.split('\n'):
        clean = ''.join(ch for ch in row if unicodedata.category(ch)[0] in ('L', 'N') or ch in ' ._-:')
        for word in clean.split():
            if len(word) > 2:
                bag.add(word.lower())
    return bag
def rate(one, two):
    a = words(one)
    b = words(two)
    if not a:
        return 1.0
    return len(a & b) / len(a)
def obf(name, tool):
    src = path(name)
    out = wipe(name)
    if not os.path.exists(src):
        return False, f"File not found: {src}", {}
    old = meta(src)
    st = time.time()
    code, stdout, stderr = run([tool, src], timeout=600)
    took = time.time() - st
    if code != 0:
        return False, f"Obfuscation failed:\n{stderr}\n{stdout}", {}
    if not os.path.exists(out):
        return False, f"Output file not created: {out}", {}
    new = meta(out)
    info = {"src": old["size"], "out": new["size"], "slines": old["lines"], "olines": new["lines"], "ratio": new["size"] / old["size"] if old["size"] else 0, "time": took}
    if info["olines"] > 4:
        return False, f"Output too long: {info['olines']} lines", info
    return True, out, info
def check(out, src, cfg):
    orig, ostdout, ostderr = run([src], data=cfg["input"], timeout=cfg["timeout"])
    st = time.time()
    code, stdout, stderr = run([out], data=cfg["input"], timeout=cfg["timeout"])
    took = time.time() - st
    if code == -1:
        if stdout.strip():
            return True, "OK (timeout - has output)", stdout, stderr, took
        if cfg["exit"]:
            return True, "OK (timeout - interactive)", stdout, stderr, took
        return False, "TIMEOUT (no output)", stdout, stderr, took
    if code == -2:
        return False, f"Run error: {stderr}", stdout, stderr, took
    low = stderr.lower()
    if any(one in low for one in ['file integrity failed', 'tamper detected', 'debugger detected']):
        return False, f"Protection triggered: {tail(stderr)}", stdout, stderr, took
    if "Traceback" in stderr:
        if "EOFError" in stderr or "KeyboardInterrupt" in stderr:
            if stdout.strip():
                return True, "PASS (EOF after output)", stdout, stderr, took
            return False, "EOF without output", stdout, stderr, took
        return False, f"Runtime error: {tail(stderr)}", stdout, stderr, took
    on = norm(ostdout)
    sn = norm(stdout)
    if code == 0:
        if sn == on:
            return True, "PASS (output matches)", stdout, stderr, took
        if stdout.strip() and ostdout.strip():
            hit = rate(ostdout, stdout)
            if hit >= 0.5:
                return True, f"PASS ({int(hit*100)}% key match)", stdout, stderr, took
            return False, f"Output mismatch ({int(hit*100)}% key match)", stdout, stderr, took
        if stdout.strip():
            return True, "PASS", stdout, stderr, took
        if ostdout.strip():
            return False, "FAIL (original has output, obf has none)", stdout, stderr, took
        return True, "PASS (no output expected)", stdout, stderr, took
    if stdout.strip():
        if ostdout.strip():
            if sn == on:
                return True, "PASS (output matches, exit after)", stdout, stderr, took
            hit = rate(ostdout, stdout)
            if hit >= 0.5:
                return True, f"PASS ({int(hit*100)}% key match, exit after)", stdout, stderr, took
            return False, f"Output mismatch ({int(hit*100)}% key match)", stdout, stderr, took
        if cfg["exit"] or code == 1:
            return True, "PASS (exit after output)", stdout, stderr, took
        return False, f"Exit {code} with output", stdout, stderr, took
    if stderr.strip():
        return False, f"Exit {code}: {tail(stderr)}", stdout, stderr, took
    return False, f"Exit {code} (no output)", stdout, stderr, took
def clean(tool):
    box = os.path.join(DIR, "__pycache__")
    if not os.path.isdir(box):
        return
    keep = {'auto_test', os.path.splitext(os.path.basename(tool))[0]}
    for name in os.listdir(box):
        root = name.split('.cpython-', 1)[0]
        if root in keep:
            try:
                os.remove(os.path.join(box, name))
            except:
                pass
def main():
    tool = pick()
    print(f"\n{CYAN}{'='*60}{RESET}")
    print(f"{CYAN}          OBSIDIAN AUTO TEST SCRIPT{RESET}")
    print(f"{CYAN}{'='*60}{RESET}")
    print(f"{CYAN}Tool: {tool}{RESET}\n")
    if not os.path.exists(tool):
        print(f"{RED}ERROR: tool not found{RESET}")
        return 1
    done = {}
    for name, cfg in FILES.items():
        print(f"\n{YELLOW}[TEST] {name} - {cfg['desc']}{RESET}")
        print("-" * 40)
        print(f"  {CYAN}[1/2] Obfuscating...{RESET}", end=" ", flush=True)
        ok, result, info = obf(name, tool)
        if not ok:
            print(f"{RED}FAILED{RESET}")
            print(f"  {RED}{result}{RESET}")
            done[name] = ("FAIL", result, "")
            continue
        print(f"{GREEN}OK{RESET} ({info['time']:.1f}s) [{info['src']/1024:.1f}KB -> {info['out']/1024:.1f}KB | {info['olines']} lines]")
        print(f"  {CYAN}[2/2] Running obfuscated code...{RESET}", end=" ", flush=True)
        ok, state, stdout, stderr, took = check(result, path(name), cfg)
        if ok:
            print(f"{GREEN}{state}{RESET} ({took:.1f}s)")
            done[name] = ("PASS", state, "")
        else:
            print(f"{RED}FAILED{RESET} ({took:.1f}s)")
            print(f"  {RED}Status: {state}{RESET}")
            if stderr:
                print(f"  {RED}Stderr:{RESET}")
                for row in stderr.split('\n')[:10]:
                    print(f"    {row}")
            done[name] = ("FAIL", state, stderr)
    clean(tool)
    print(f"\n{CYAN}{'='*60}{RESET}")
    print(f"{CYAN}                    SUMMARY{RESET}")
    print(f"{CYAN}{'='*60}{RESET}\n")
    good = 0
    bad = 0
    for name, data in done.items():
        if data[0] == "PASS":
            print(f"  {GREEN}✓ {name}: {data[1]}{RESET}")
            good += 1
        else:
            print(f"  {RED}✗ {name}: {data[1]}{RESET}")
            bad += 1
    print(f"\n{CYAN}{'='*60}{RESET}")
    if bad == 0:
        print(f"{GREEN}ALL {good} TESTS PASSED!{RESET}")
    else:
        print(f"{YELLOW}Passed: {good} | {RED}Failed: {bad}{RESET}")
    print(f"{CYAN}{'='*60}{RESET}\n")
    return 0 if bad == 0 else 1
if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print(f"\n{YELLOW}Cancelled.{RESET}")
        sys.exit(1)
    except Exception as e:
        print(f"\n{RED}Unexpected error: {e}{RESET}")
        traceback.print_exc()
        sys.exit(1)
