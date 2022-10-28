import time

# 파일 생성 및 데이터 입력

file_editor = open(file="fileio/test.txt", mode="w", encoding="utf-8")  # 실행 경로를 확실히 적어야 한다.
# file_editor = open("fileio/test.txt", "w", "utf-8")  # 매겨변수를 넣을 때 키워드를 넣을 땐 순서가 상관없지만, 키워드를 넣지 않을 땐 매개변수 순서를 지켜줘야 한다.
# open(): 파일을 열 때 사용
# mode="w" 는 write 모드

file_editor.write("안녕하세요.")

# time.sleep(10)

file_editor.close()
# 파일을 열어놓은 상태에서는 다른 작업이 안 될 수 있기 때문에 닫아준다.
# 파일을 open 했으면 반드시 close 해야 한다.

print("작업종료")

# 이 파일을 두 번 실행해도 "안녕하세요"는 한 번만 실행 - 덮어쓰기가 됨