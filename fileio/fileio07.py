
# with open(file="fileio/bin.txt", mode="bw", encoding="utf-8") as file_editor:
#     # pass # 윗줄을 작성해놓고 잠시 다른 작업을 할 때 사용 / pass가 없으면 에러 발생
#     file_editor.write("a")
'''
ValueError: binary mode doesn't take an encoding argument
'''
# 에러 발생

# 바이너리 파일: 0과 1이 들어가 있는 파일 / 파일 
# xml 등: 프로그램이 인식하기 위해 쉽기 사람이 직접 지은 확장자
# 확장자는 더블클릭 했을 때 바로 접근하기 위함이지 중요한 것이 아니다. 예를 들어 ad? 확장자의 파일은 바로 열리지는 않지만, 메모장을 열어서 파일을 드래그로 열면 잘 열린다.


'''
# with open(file="fileio/bin.txt", mode="bw") as file_editor:
#     file_editor.write("a")
'''
'''
TypeError: a bytes-like object is required, not 'str'
'''

# 바이너리 파일 입력
with open(file="fileio/bin.txt", mode="bw") as file_editor:
    file_editor.write(b"a")