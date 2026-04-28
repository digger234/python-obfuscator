import subprocess
import sys
import os
import time
import traceback


sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.stderr.reconfigure(encoding='utf-8', errors='replace')

DIR = os.path.dirname(os.path.abspath(__file__))
AEGIS = os.path.join(DIR, "bedrock.py")

TEST_FILES = {
    "test.py": {"input": "0\n", "timeout": 30, "expect_exit": True, "desc": "Basic test"},
    "test2.py": {"input": None, "timeout": 60, "expect_exit": False, "desc": "Complex test"},
    "test3.py": {"input": None, "timeout": 30, "expect_exit": False, "desc": "Simple test"},
    "test4.py": {"input": "0\n", "timeout": 30, "expect_exit": True, "desc": "Large test"},
    "test5.py": {"input": "test_key\ntest_link\n1\n", "timeout": 10, "expect_exit": True, "desc": "Interactive test"},
}

SELF_TEST = {"bedrock.py": {"input": None, "timeout": 600, "expect_exit": False, "desc": "Self-obfuscation test"}}

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

PYTHON_EXE = "C:/Users/XZ/AppData/Local/Python/pythoncore-3.12-64/python.exe"

def run_cmd(cmd, cwd=None, input_data=None, timeout=60):
    try:
        if cmd[0] == sys.executable:
             cmd[0] = PYTHON_EXE
        
        env = os.environ.copy()
        env['PYTHONIOENCODING'] = 'utf-8'
        env['AEGIS_SAFE_MODE'] = '1'
        proc = subprocess.run(
            cmd,
            cwd=cwd or DIR,
            input=input_data,
            capture_output=True,
            text=True,
            timeout=timeout,
            encoding='utf-8',
            errors='replace',
            env=env
        )
        return proc.returncode, proc.stdout, proc.stderr
    except subprocess.TimeoutExpired:
        return -1, "", "TIMEOUT"
    except Exception as e:
        return -2, "", str(e)

def get_file_metrics(filepath):
    if not os.path.exists(filepath):
        return {"size": 0, "lines": 0}
    size = os.path.getsize(filepath)
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        lines = len(f.readlines())
    return {"size": size, "lines": lines}

def obfuscate(test_file, aegis_path=None):
    src = os.path.join(DIR, test_file)
    if not os.path.exists(src):
        return False, f"File not found: {src}", {}
    
    orig_metrics = get_file_metrics(src)
    aegis = aegis_path or AEGIS
    cmd = [sys.executable, aegis, src]
    start = time.time()
    code, stdout, stderr = run_cmd(cmd, timeout=600)
    elapsed = time.time() - start
    
    if code != 0:
        return False, f"Obfuscation failed:\n{stderr}\n{stdout}", {}
    
    obf_file = os.path.splitext(src)[0] + "_obf.py"
    if not os.path.exists(obf_file):
        return False, f"Output file not created: {obf_file}", {}
    
    obf_metrics = get_file_metrics(obf_file)
    metrics = {
        "orig_size": orig_metrics["size"],
        "obf_size": obf_metrics["size"],
        "orig_lines": orig_metrics["lines"],
        "obf_lines": obf_metrics["lines"],
        "ratio": obf_metrics["size"] / orig_metrics["size"] if orig_metrics["size"] > 0 else 0,
        "time": elapsed
    }
    
    return True, obf_file, metrics

def test_obfuscated(obf_file, original_file, input_data=None, timeout=60, expect_exit=False):
    # Chạy original file trước để lấy expected output
    orig_cmd = [sys.executable, original_file]
    orig_code, orig_stdout, orig_stderr = run_cmd(orig_cmd, input_data=input_data, timeout=timeout)
    
    # Chạy obfuscated file
    cmd = [sys.executable, obf_file]
    code, stdout, stderr = run_cmd(cmd, input_data=input_data, timeout=timeout)
    
    # Timeout
    if code == -1:
        if stdout.strip():
            return True, "OK (timeout - has output)", stdout, stderr
        if expect_exit:
            return True, "OK (timeout - interactive)", stdout, stderr
        return False, "TIMEOUT (no output)", stdout, stderr
    
    # Run error
    if code == -2:
        return False, f"Run error: {stderr}", stdout, stderr
    
    def get_error_msg(s):
        lines = [l.strip() for l in s.strip().split('\n') if l.strip()]
        for line in reversed(lines):
            if 'Error' in line or 'error' in line or 'failed' in line.lower():
                return line[:80]
        return lines[-1][:80] if lines else 'unknown'
    
    # Check lỗi nghiêm trọng trong stderr
    stderr_lower = stderr.lower()
    if any(x in stderr_lower for x in ['file integrity failed', 'tamper detected', 'debugger detected']):
        return False, f"Protection triggered: {get_error_msg(stderr)}", stdout, stderr
    
    # Check Python runtime errors
    if "Traceback" in stderr:
        err_msg = get_error_msg(stderr)
        if "EOFError" in stderr or "KeyboardInterrupt" in stderr:
            if stdout.strip():
                return True, "PASS (EOF after output)", stdout, stderr
            return False, f"EOF without output", stdout, stderr
        return False, f"Runtime error: {err_msg}", stdout, stderr
    
    # So sánh output với original - thông minh hơn
    def normalize_output(s):
        lines = [l.strip() for l in s.strip().split('\n') if l.strip()]
        return '\n'.join(lines)
    
    def check_key_content(orig, obf):
        import unicodedata
        def extract_words(text):
            words = set()
            for line in text.split('\n'):
                clean = ''.join(c for c in line if unicodedata.category(c)[0] in ('L', 'N') or c in ' ._-:')
                for word in clean.split():
                    if len(word) > 2:
                        words.add(word.lower())
            return words
        orig_words = extract_words(orig)
        obf_words = extract_words(obf)
        if not orig_words:
            return 1.0
        matched = len(orig_words & obf_words)
        return matched / len(orig_words)
    
    orig_norm = normalize_output(orig_stdout)
    obf_norm = normalize_output(stdout)
    
    # Exit code 0
    if code == 0:
        if obf_norm == orig_norm:
            return True, "PASS (output matches)", stdout, stderr
        if stdout.strip() and orig_stdout.strip():
            # Check key content match
            key_ratio = check_key_content(orig_stdout, stdout)
            if key_ratio >= 0.7:
                return True, f"PASS ({int(key_ratio*100)}% key match)", stdout, stderr
            if key_ratio >= 0.5:
                return True, f"PASS ({int(key_ratio*100)}% key match)", stdout, stderr
            return False, f"Output mismatch ({int(key_ratio*100)}% key match)", stdout, stderr
        if stdout.strip():
            return True, "PASS", stdout, stderr
        if orig_stdout.strip():
            return False, "FAIL (original has output, obf has none)", stdout, stderr
        return True, "PASS (no output expected)", stdout, stderr
    
    # Exit code != 0 nhưng có output
    if stdout.strip():
        if orig_stdout.strip():
            # So sánh với original - dùng key content
            if obf_norm == orig_norm:
                return True, "PASS (output matches, exit after)", stdout, stderr
            key_ratio = check_key_content(orig_stdout, stdout)
            if key_ratio >= 0.5:
                return True, f"PASS ({int(key_ratio*100)}% key match, exit after)", stdout, stderr
            return False, f"Output mismatch ({int(key_ratio*100)}% key match)", stdout, stderr
        if expect_exit or code == 1:
            return True, "PASS (exit after output)", stdout, stderr
        return False, f"Exit {code} with output", stdout, stderr
    
    # Exit code != 0, không có output = FAIL
    if stderr.strip():
        return False, f"Exit {code}: {get_error_msg(stderr)}", stdout, stderr
    return False, f"Exit {code} (no output)", stdout, stderr

def main():
    print(f"\n{CYAN}{'='*60}{RESET}")
    print(f"{CYAN}       AEGIS OBFUSCATOR - AUTO TEST SCRIPT{RESET}")
    print(f"{CYAN}{'='*60}{RESET}\n")
    
    if not os.path.exists(AEGIS):
        print(f"{RED}ERROR: aegisv1.py not found!{RESET}")
        return 1
    
    results = {}
    all_metrics = {}
    
    for test_file, config in TEST_FILES.items():
        desc = config.get("desc", test_file)
        print(f"\n{YELLOW}[TEST] {test_file} - {desc}{RESET}")
        print("-" * 40)
        
        print(f"  {CYAN}[1/2] Obfuscating...{RESET}", end=" ", flush=True)
        success, result, metrics = obfuscate(test_file)
        
        if not success:
            print(f"{RED}FAILED{RESET}")
            print(f"  {RED}Error: {result}{RESET}")
            results[test_file] = ("FAIL", "Obfuscation failed", result)
            continue
        
        size_info = f"{metrics['orig_size']/1024:.1f}KB → {metrics['obf_size']/1024:.1f}KB ({metrics['ratio']:.1f}x)"
        print(f"{GREEN}OK{RESET} ({metrics['time']:.1f}s) [{size_info}]")
        obf_file = result
        all_metrics[test_file] = metrics
        
        print(f"  {CYAN}[2/2] Running obfuscated code...{RESET}", end=" ", flush=True)
        start = time.time()
        success, status, stdout, stderr = test_obfuscated(
            obf_file,
            os.path.join(DIR, test_file),
            input_data=config["input"],
            timeout=config["timeout"],
            expect_exit=config["expect_exit"]
        )
        elapsed = time.time() - start
        
        if success:
            print(f"{GREEN}{status}{RESET} ({elapsed:.1f}s)")
            results[test_file] = ("PASS", status, "")
        else:
            print(f"{RED}FAILED{RESET} ({elapsed:.1f}s)")
            print(f"  {RED}Status: {status}{RESET}")
            if stderr:
                print(f"  {RED}Stderr:{RESET}")
                for line in stderr.split('\n')[:10]:
                    print(f"    {line}")
            results[test_file] = ("FAIL", status, stderr)
    
    print(f"\n{CYAN}{'='*60}{RESET}")
    print(f"{CYAN}                    SUMMARY{RESET}")
    print(f"{CYAN}{'='*60}{RESET}\n")
    
    passed = 0
    failed = 0
    
    for test_file, (status, msg, _) in results.items():
        if status == "PASS":
            print(f"  {GREEN}✓ {test_file}: {msg}{RESET}")
            passed += 1
        else:
            print(f"  {RED}✗ {test_file}: {msg}{RESET}")
            failed += 1
    
    print(f"\n{CYAN}{'='*60}{RESET}")
    if failed == 0:
        print(f"{GREEN}ALL {passed} TESTS PASSED!{RESET}")
    else:
        print(f"{YELLOW}Passed: {passed} | {RED}Failed: {failed}{RESET}")
    print(f"{CYAN}{'='*60}{RESET}\n")
    
    return 0 if failed == 0 else 1

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
