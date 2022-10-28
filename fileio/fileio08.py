import pickle


with open(file="fileio/bin.pickle", mode="bw") as file_editor:
    pickle.dump([1, 2, 3], file_editor)
    
# 생성한 파일을 들어가면 에러가 있음