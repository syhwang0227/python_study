# def solution(numbers : list):
#     sum = 0
#     for i in numbers:
#         sum = sum + i
        
#     average = sum/len(numbers)
#     return average

# print(solution([1, 2, 3]))

# 함수 만들기 전
# num = [1, 2, 3] 
# sum = 0
# for i in range(len(num)):
#     sum = sum + num[i]
#     print(sum)
#     average = sum / len(num)
# print(average)

# 짧은 방법
# def solution(numbers : list):
#     return sum(numbers) / len(numbers)

# print(solution([1, 2, 3]))

# solution = lambda numbers : sum(numbers) / len(numbers)
# print(solution([1, 2, 3]))

#
num_list = [1, 2, 3, 4, 5]
num_list.reverse()
print(num_list)

arr = [1, 2, 3, 5]
hei = 4
for i in arr:
    if hei < i:
        sum += 1
    else: pass

print(sum)