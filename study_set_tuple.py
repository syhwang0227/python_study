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