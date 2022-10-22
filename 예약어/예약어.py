from math import pow

# is = "a"
# print(is)
# 예약어들은 변수명으로 사용할 수 없고, 에러가 생기지 않더라도 사용하지 않는 것이 좋다.
# SyntaxError: invalid syntax

# 사용할 수 없는 특수문자
# ^num = 1
# $num = 1

# 사용가능한 특수문자
# _ : 내부적으로 사용한다는 뜻
# __: 숨겨진 변수라는 뜻

# _num = 1
# print(_num)
# 1

temp = None
temp = True and False

# print(temp)

# assert False  # AssertionError
assert True  # 에러 없이 넘어감

# for item in range(10):
#     if item == 5:
#         continue
#     elif item == 8:
#         break
#     else:
#         print(item)
'''
0
1
2
3
4
6
7
'''

# for item in range(10):
#     if item == 5:
#         # 조건이 맞으면 반복문의 처음으로 돌아감
#         continue  
#     elif item == 8:
#         # 반복문을 멈춤
#         break
#     print(item)
'''
0
1
2
3
4
6
7
'''

try:
    pass
    # or ...
except:
    pass
finally:
    pass

# try:
#     temp = "가나다"
#     temp[0] = "아"
# except:
#     print("에러가 발생했습니다.")
# finally:
#     print("마지막으로 할 것은 하겠습니다.")

# print("넘어왔습니다.")
'''
에러가 발생했습니다.
마지막으로 할 것은 하겠습니다.
넘어왔습니다.
'''

# try:
#     temp = "가나다"
#     temp[0] = "아"
# except Exception as e:
#     e.with_traceback()
#     # print("에러가 발생했습니다.")
# finally:
#     print("마지막으로 할 것은 하겠습니다.")  # 에러가 나서 멈추더라도 하고 넘어가는 것

# print("넘어왔습니다.")
'''
마지막으로 할 것은 하겠습니다.
Traceback (most recent call last):
  File "c:\programming\python_study\예약어\예약어.py", line 88, in <module>
    temp[0] = "아"
TypeError: 'str' object does not support item assignment

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "c:\programming\python_study\예약어\예약어.py", line 90, in <module>
    e.with_traceback()
TypeError: BaseException.with_traceback() takes exactly one argument (0 given)
'''

# try:
#     temp = "가나다"
#     temp[0] = "아"
# except Exception as e:
#     print(e)
#     # e.with_traceback()
#     # print("에러가 발생했습니다.")
# finally:
#     print("마지막으로 할 것은 하겠습니다.")  # 에러가 나서 멈추더라도 하고 넘어가는 것

# print("넘어왔습니다.")
'''
'str' object does not support item assignment
마지막으로 할 것은 하겠습니다.
넘어왔습니다.
'''

# 글로벌 예제
# temp = 1
# for temp in range(10):
#     pass

# print(temp)

# 파이썬의 scope 개념: Global > block > code
# temp = 1  # global
# def my_func():
#     temp = 3
#     return temp

# print(my_func())
# print(temp)
'''
3
1
'''

# temp = 1
# def my_func():
#     global temp  # 실제 개발에서 사용하는 경우가 거의 없음
#     temp = 3
#     return temp

# print(my_func())
# print(temp)

# raise Exception("내가 만든 에러")
'''
Traceback (most recent call last):
  File "c:\programming\python_study\예약어\예약어.py", line 157, in <module>
    raise Exception("내가 만든 에러")
Exception: 내가 만든 에러
'''

# 파라미터
# def my_func(num):
#     print(num)

# my_func(12)
# 12: 아규먼트, 인자, 인수
# 파라미터와 아규먼트를 특별히 구분하지 않는다.

# 위의 함수와 완전히 같다.
# def my_func(num): return print(num)
# my_func(12)
# 12

# temp = list(filter(lambda num : num != 1, [1, 2, 3, 1]))
# print(temp)
# [2, 3]

# yield 함수
# def my_func():
#     while True:
#         yield 1
#         yield 2
#         yield 3

# my_yield_data = my_func()

# print(next(my_yield_data))
# print(next(my_yield_data))
# print(next(my_yield_data))
# print(next(my_yield_data))
'''
1
2
3
1
'''

# def my_func():
#     # while True:
#     yield 1
#     yield 2
#     yield 3

# my_yield_data = my_func()

# print(next(my_yield_data))
# print(next(my_yield_data))
# print(next(my_yield_data))
# print(next(my_yield_data))
'''
1
2
3
Traceback (most recent call last):
  File "c:\programming\python_study\예약어\예약어.py", line 213, in <module>
    print(next(my_yield_data))
StopIteration
'''

# 무한반복!
# def my_func():
#     while True:
#         yield 1
#         yield 2
#         yield 3

# my_yield_data = my_func()

# for item in my_yield_data:
#     print(item)

# def check_str(data : str):  # data 라는 것에 타입을 지정해주면 내부 함수를 사용할 수 있다.
#     return data.endswith("마")

# print(check_str("가나다"))
# False

# def check_str(data):  # 지정하지 않아도 값은 잘 나오지만 툴이 지원해주는 것을 굳이 안 쓸 이유는 없다.
#     return data.endswith("마")

# print(check_str("가나다"))

def check_str(data : str):  # 지정하지 않아도 값은 잘 나오지만 툴이 지원해주는 것을 굳이 안 쓸 이유는 없다. / data는 str을 받는다는 것을 알려줌
    return data.endswith("마")

print(check_str(1))