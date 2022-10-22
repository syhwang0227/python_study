temp = list(range(10))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

temp = list(range(5, 10))
# [5, 6, 7, 8, 9]

temp = list(range(3, 30, 3))
# [3, 6, 9, 12, 15, 18, 21, 24, 27]

# print(temp)

# temp = list(range(0, 10))

# for item in temp:
#     print(item)
'''
0
1
2
3
4
5
6
7
8
9
'''

temp = [item for item in range(0, 10)]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

temp = (item for item in range(0, 10))
# <generator object <genexpr> at 0x0000011DB23B83C0>

temp = {item for item in range(0, 10)}
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

temp = {"안녕" for item in range(0, 10)}
# set은 똑같은 데이터는 버린다.
# {'안녕'}

temp = ["안녕" for item in range(0, 10)]
# ['안녕', '안녕', '안녕', '안녕', '안녕', '안녕', '안녕', '안녕', '안녕', '안녕']

print(temp)