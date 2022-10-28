# close()를 까먹을 수도 있다. 그것을 방지하는 방법

# with as를 사용하면 close() 등을 자동으로 처리해준다.
with open(file="fileio/test.txt", mode="w", encoding="utf-8") as file_editor:
    file_editor.write("with as")