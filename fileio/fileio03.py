# 파일 읽기

# mode="r"은 파일 읽기 (read)
file_editor = open(file="fileio/test.txt", mode="r", encoding="utf-8")

my_text = file_editor.readline()
# readline()은 파일에서 한줄씩 데이터를 가져온다.
my_text1 = file_editor.readline()
my_text2 = file_editor.readline()
my_text3 = file_editor.readline()

file_editor.close()

print(my_text)
print(my_text1)
print(f"{my_text2=}")
print(f"{my_text3=}")

'''
안녕하세요.

반갑습니다.
'''
'''
왜 한 줄 공백이 생기는가?
print() 함수의 기본값이 end 이기 때문에
'''
