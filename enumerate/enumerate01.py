temp = {"a", "b", "c"}

# for item in temp:
#     print(item)
# 순서가 있는 시퀀스가 아니므로 순서 없이 출력된다.
'''
b
a
c
'''

temp = enumerate(temp)

# for item in temp:
#     print(item)
'''
(0, 'b')
(1, 'a')
(2, 'c')
'''

# for num, value in temp:
#     print(num, value)
'''
0 b
1 a
2 c
'''

# a, b = (1, 2)
# print(a)
# print(b)
'''
1
2
'''

# a, b = (1, 2, 3)
# print(a)
# print(b)
# ValueError: too many values to unpack (expected 2)

# 리스트로 표현
# a, b = [1, 2]
# print(a)
# print(b)
'''
1
2
'''

a, b = {1, 2}
print(a)
print(b)
'''
1
2
'''

a, b = {"name": "이름", "age": 12}.items()
print(a)
print(b)
'''
('name', '이름')
('age', 12)
'''