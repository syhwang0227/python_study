temp = [1, 2] + [3, 4]
# print(temp)

temp.append(5)
temp.remove(1)

temp = [1, 1, 1, 1]
temp.remove(1)  # 1이 하나만 삭제되고 나머지 3개는 그대로 남아있다.
# 모든 같은 데이터를 지우지 않고, 하나만 지운다.
# [1, 1, 1]

temp = [1, 1, 1, 1]

def check(num):
    if num == 1:
        return False
    else:
        return True
    
# check()  # 마우스를 올려보면 return 값이 bool 인 것을 알 수 있다.
# print(check(1))
# print(check(2323))

temp = [1, 2, 3, 1, 1]
temp = filter(check, temp)
temp = list(temp)
# [2, 3]

# temp = list(filter(check, [1, 1, 1, 1]]))
# print(temp)

# 차원
temp = 1  # 0차원 / 단순한 점이다.
temp = [1, 2, 3, 4, 5]  # 1차원 배열
temp = [[1, 2], [3, 4]]  # 2차원 배열

temp = [
    [1, 2],
    [3, 4]
    ]

# print(temp[0])
# [1, 2]

# print(temp[0][0])
# 1

temp = [
    (1, 2),
    (3, 4)
]

# 리스트 안에 set이 들어있는 구조
temp = [ 
    {"a", "c"},
    {"b", "d"}
]

temp = [
    {"key": "value", "name": "이름"},
    {"b": "d", "aa": "dd"}
]

print(temp[0])
# {'key': 'value', 'name': '이름'}
print(temp[0]["name"])
# 이름

# print(temp)