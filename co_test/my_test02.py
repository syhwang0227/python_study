# 문제2. 상자 만들기

# print("*****")
# print("*   *")
# print("*   *")
# print("*   *")
# print("*****")

# for i in range(5):
#     a = "*" * 5
#     b = "*   *"
#     if i == 0 or i == 4:
#         print(a)
#     elif i == 1 or 2 or 3:
#     # elif i == 1 or i == 2 or i == 3:
#         print(b)

# 빈공간이 생기는 조건

# 1.
# for i in range(5):  # 하지만 이 방법은 range 안의 숫자가 5보다 커지면 중간이 이상해진다.
#     if i == 0 or i == 4:
#         print("*****")
#     else:
#         print("*   *")

my_list = range(5)
for i in my_list:
    if i == 0 or i == len(my_list):  # 이렇게 하면 안 됨! len(my_list)은 5이고 i는 4가 끝이다.
        print("*****")
    else:
        print("*   *")
# i = 0 ~ 4
# len(my_list) = 5
        
my_list = range(5)
for i in my_list:
    if i == 0 or i == len(my_list) -1: 
        print("*****")
    else:
        print("*   *")