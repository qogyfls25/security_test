# 취약한 코드 예시
user_input = input("이름을 입력하세요: ")
print(f"<html><body>{user_input}</body></html>") # XSS 취약점! 필터링이 없음
