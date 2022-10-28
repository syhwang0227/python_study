# 파일 읽기

# mode="r"은 파일 읽기 (read)
file_editor = open(file="fileio/test.txt", mode="r", encoding="utf-8")

my_text = file_editor.readlines()
# readlines()는 파일 데이터를 한줄씩 배열로 가져온다.

file_editor.close()

print(my_text)

'''
['안녕하세요.\n', '반갑습니다.']
'''
'''
readlines()는 \n를 기준으로 파일을 자르기 때문에 \n이 앞에 있다.
'''