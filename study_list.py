print("\n리스트")
# 변수명을 설정하는 방법이 언어마다 다르다.
my_list = [1, 2, 3, 4]
print(my_list)

for element in my_list:
    print(element)

string = "가나다 라마바사"
char_list = string.split('')  # '' 기준으로 split
print(char_list)  # 에러 발생: 파이썬에서는 빈공간 자르기가 안 됨