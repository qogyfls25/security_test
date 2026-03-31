import re

def scan_file(filename):
    with open(filename, 'r') as f:
        content = f.read()
        # 'print' 안에 변수가 직접 들어가는 패턴을 정규표현식으로 찾음
        if re.search(r"print\(f\".*\{.*\}.*\"\)", content):
            print(f"[경고] {filename}에서 XSS 위험 패턴 발견!")
            return True
    return False

if scan_all_files():
    exit(1) # 에러를 뱉으며 종료 (CI/CD를 중단시킴)
