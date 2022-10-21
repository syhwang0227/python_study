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