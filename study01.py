from decimal import Decimal
import math

'''
num1 = 2 + 3
print("2 + 3 =", num1)

num2 = 2 - 3
print("2 - 3 =", num2)

num3 = 2 * 3
print("2 * 3 =", num3)

num4 = 2 / 3
print("2 / 3 =", num4)

num5 = 2 // 3
print("2 // 3 =", num5)

num6 = 2 % 3
print("2 % 3 =", num6)

num7 = -1
print("-1:", num7)

num8 = +1
print("+1:", num8)

num9 = abs(1.2222)
print("abs(1.2222):", num9)

num10 = int(10)
print("int(10):", num10)

num10 = float(10)
print("float(10):", num10)

num11 = pow(3, 2)
print("pow(3, 2):", num11)

num12 = 3 ** 2
print("3 ** 2 =", num12)

num13 = 1.2 + 3
print("1.2 + 3 =", num13)

num14 = int(1.2 + 3)
print("int(1.2 + 3):", num14)

num15 = float(1.2 + 3)
print("float(1.2 + 3):", num15)

# 이진법의 한계
num16 = 1.1 + 0.1
print(num16)

num17 = Decimal("1.1") + Decimal("0.1")
print(num17)

print("\nmath function")
math1 = math.trunc(1.2222)
print("math.trunc(1.2222):", math1)

# math2 = round(1.555, [3])
# print(math2)

math3 = math.floor(1.2222)
print("math.floor(1.2222):", math3)

math4 = math.ceil(1.2222)
print("math.ceil(1.2222):", math4)

print("\n문자열")
name = 'hsy'
name2 = "hsy"
age = 10

print("내 이름은" + name)
print("내 이름은 " + name)

# print("내 이름은 " + name + " 내 나이는 " + age)  # 에러 발생: 문자와 숫자는 + 기능이 안 됨
print("내 이름은 " + name + " 내 나이는 " + str(age))  # +가 늘어날 수록 가독성이 떨어짐
print(f"내 이름은 {name} 내 나이는 {age}")  # 이 형식은 age 앞에 str을 안 붙여줘도 됨 / f: format
print(f"{name=} {age=}")  # 개발할 때 값 확인 시 유용
print("내 이름은 %s 내 나이는 %d"% (name, age))  # s: string, d: decimal
print("내 이름은 {0} 내 나이는 {1}".format(name, age))
print("내 이름은 {n} 내 나이는 {a}".format(n=name, a=age))  # 명시적으로 표현 가능

print("\n리스트")
# 변수명을 설정하는 방법이 언어마다 다르다.
my_list = [1, 2, 3, 4]
print(my_list)

for element in my_list:
    print(element)

string = "가나다 라마바사"
char_list = string.split('')  # '' 기준으로 split
print(char_list)  # 에러 발생: 파이썬에서는 빈공간 자르기가 안 됨
'''

'''
string = "가나다 라마바사"
# char_list = string.split(' ')  # ' ' 기준으로 split
# print(char_list)

change_string = string.replace('가', '하')  # 특정한 문자를 바꾸고 싶을 때 사용
# print(change_string)

# 엇? 불변 아닌가?
# string[0] = '하'
# print(string)  # 에러 발생: TypeError: 'str' object does not support item assignment

# 엇? 불변 아닌가?
# string[0] == '하'
# print(string)  # 에러는 발생하지 않지만 string 값이 변하지는 않음

# 하지만 리스트는 가변이기 때문에 변한다.
my_list = [1, 2, 3, 4] 
my_list[0] = 9
print(my_list)

# id 값이 다르니 다른 상자에 있는 값이 다른 것이다.
print(id(string))
print(id(change_string))

# 예1.
# data1 = "가나다"
# data2 = "가나다"

# # 분명히 다른 상자인데 id 값이 똑같다.
# print(id(data1))
# print(id(data2))

# 예2.
data1 = [1, 2, 3]
data2 = [1, 2, 3]

# 분명히 다른 상자인데 id 값이 똑같다.
print(id(data1))
print(id(data2))
'''

'''
data = 1  # 값은 1
# data = 2  # 값은 2
# data = 3  # 모르겠다!

check = (data == 3)  # check에 마우스를 대면 check: bool 내용이 보인다.
'''
# 경우1.
# data = input()  # input(): user에게 데이터를 받는 함수
# 1을 입력했을 때, "모르겠다!" 출력되는데, 외부에서 가져오는 값은 문자열로 취급한다.

# 경우2. 
# data = int(input())

# 경우3. elif만 추가 가능
# data = int(input())

# if data == 1:
#     print("값은 1")
# elif data == 2:
#     print("값은 2")
# # elif 추가 가능
# elif data == 3:
#     print("값은 3")
# elif data == 4:
#     print("값은 4")
# else:
#     print("모르겠다!")

# 경우4. 데이터를 2개 이상 받고 싶다면? 그런데 100개를 받고 싶다면?
# data = int(input())

# if data == 1:
#     print("값은 1")
# elif data == 2:
#     print("값은 2")
# elif data == 3:
#     print("값은 3")
# elif data == 4:
#     print("값은 4")
# else:
#     print("모르겠다!")
    
# data = int(input())

# if data == 1:
#     print("값은 1")
# elif data == 2:
#     print("값은 2")
# elif data == 3:
#     print("값은 3")
# elif data == 4:
#     print("값은 4")
# else:
#     print("모르겠다!")

# 반복문의 2가지
# while True:
#     print("가나다")
    
# for item in [1, 2, 3, 4]:  # for가 사라질 것 같아ㅋㅋㅋㅋ while가 무한 루프에 빠지려고 하니까! while 문 안에 break를 해줘야 한다.
#     print(item)

# x = 1  # 문제점: x가 11이 되면 무한반복에 빠진다. 그러면 cpu가 계속 올라간다. ctrl + c로 빠져나온다.
# while True:
#     print("가나다")
#     if x == 10:
#         break
#     else:  # x가 10이 아니면 x에 1을 더함
#         x = x + 1
        
# for item in [1, 2, 3, 4]:  # for가 사라질 것 같아ㅋㅋㅋㅋ
#     print(item)

# 방법1.
# x = 1
# while True:
#     print("가나다")
#     if x <= 10:
#         break
#     else:  # x가 10이 아니면 x에 1을 더함
#         x = x + 1

# 방법2.
# x = int(input())
# x = 1 
# while x < 10:
#     print("가나다")
#     x = x + 1

# 데이터가 들어왔는데 언제 끝날지 모르는 경우 while을 사용한다.
# 들어갈 데이터가 한정되어있을 때 for문 사용

# 함수 생성 / 가나다가 4번 출력된다. / 재활용 가능
# def check_data():
#     print("가나다")

# check_data()
# check_data()
# check_data()
# check_data()

'''
# 경우1.
def check_data():
    data = int(input())

    if data == 1:
        print("값은 1")
    elif data == 2:
        print("값은 2")
    elif data == 3:
        print("값은 3")
    elif data == 4:
        print("값은 4")
    else:
        print("모르겠다!")

check_data()
check_data()
check_data()

# 경우2.
def check_data():
    data = int(input())

    if data == 1:
        print("값은 1")
    elif data == 2:
        print("값은 2")
    elif data == 3:
        print("값은 3")
    elif data == 4:
        print("값은 4")
    else:
        print("모르겠다!")

while True:
    check_data()  # 멈추지 않는 이상 끝없이 터미널에서 검사 / ctrl + C - 무한반복 해제
'''

# def sum_two_num(n1, n2):
#     print(n1 + n2)
    
# sum_two_num(1, 2)

# 데이터 반환
# def sum_two_num(n1, n2):
#     return n1 + n2  
    
# sum_two_num(1, 2)
# 반환만 했지 출력하지 않았기 때문에 아무 결과가 없다.

# 출력
# def sum_two_num(n1, n2):
#     return n1 + n2  
    
# sum_num = sum_two_num(1, 2)
# print(sum_num)

# 논리 연산
# print(True or True)
# print(not False)

# print(1 >= 1)
# print(1 != 2)

# result = (1 != 2)
# print(result)

# result2 = not (1 != 2)
# print(result2)

# 집합
# my_set = {1, 2, 3, 4, 1, 1, 1}
# print(my_set)  # 중복되지 않는 것들의 모음

# # 중복된 데이터는 삭제하고 4번 반복 / 데이터가 중복되면 안 될 때, 집합 사용
# for item in my_set:
#     print(item)

# my_set =set([1, 2, 3, 4, 1, 1, 1])
# print(my_set)

my_dict = {'name' : 'hsy', 'age' : 12}
# print(my_dict["name"])

# for item in my_dict:
#     print(item)  # 하나씩만 나오네?

# for key, value in my_dict.items():  # items(): 딕셔너리 타입이 가지고 있는 함수
#     print(f"{key} 은/는 {value}")

# 튜플
# my_tuple = (1, 2, 3, 4)  # 참고: 띄어쓰기 잘못되었을 때 자동으로 예쁘게 해주는 기능이 있다.
# print(my_tuple)

# for item in my_tuple:
#     print(item)

# 중복값도 가능
# my_tuple = (1, 1, 2, 3, 4) 
# print(my_tuple)

# for item in my_tuple:
#     print(item)
    
my_tuple = (1, 1, 2, 3, 4) 
# my_tuple[0] = 3  # 에러 발생: 내부 데이터는 바꿀 수 없음
my_tuple = [1, 2, 3]  # 겉만(?) 바뀐다.
print(my_tuple)