# 파일 삭제
import os

# 아래 코드는 if문을 타지 않았으므로 실행되지 않는다. 파일이 삭제되지 않는다.
# if os.path.exists("test.txt"):
#     os.remove("test.txt")

# 1번 방법
# 경로를 제대로 지정하여 삭제    
# if os.path.exists("fileio/test.txt"):
#     os.remove("fileio/test.txt")

# 2번 방법
# 콘솔에서 명령어를 치는 것과 같다.
os.system("rm test.text")
print("확인")
'''
rm: cannot remove 'test.text': No such file or directory
확인
'''
# print 문이 출력되므로 에러는 아니다. 출력되지 않으면 에러

os.system("rm fileio/test.text")


# 폴더 삭제
# os.system("rm -r fileio/")

# 강제적으로 실행
# os.system("rm -rf fileio/")
