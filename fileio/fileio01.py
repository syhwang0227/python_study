# 파일 수정

# mode="a"는 파일 수정 (append)
file_editor = open(file="fileio/test.txt", mode="a", encoding="utf-8")

file_editor.write("\n반갑습니다.")

file_editor.close()

# 수정할 파일이 존재하지 않는 경우 파일이 바로 생성된다.