import re
import os

# 1. 개별 파일을 검사하는 함수
def scan_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        # print 문 안에 중괄호{}가 직접 들어가는 XSS 위험 패턴을 찾습니다.
        if re.search(r"print\(f\".*\{.*\}.*\"\)", content):
            print(f"  [경고] {filename}에서 XSS 위험 패턴 발견!")
            return True
    return False

# 2. 모든 파이썬 파일을 찾아서 검사하는 함수 (이게 빠져있었네요!)
def scan_all_files():
    found_issue = False
    # 현재 폴더의 모든 파일을 뒤집니다.
    for file in os.listdir('.'):
        if file.endswith('.py') and file != 'security_scan.py': # 검사 도구 자신은 제외
            print(f"--- {file} 검사 중 ---")
            if scan_file(file):
                found_issue = True
    return found_issue

# 3. 메인 실행부
if __name__ == "__main__":
    if scan_all_files():
        print("\n[결과] 보안 취약점이 발견되어 빌드를 중단합니다.")
        exit(1) # 에러 코드를 뱉어서 GitHub Actions를 빨간불로 만듭니다.
    else:
        print("\n[결과] 모든 파일이 안전합니다!")
        exit(0) # 성공!
