# print("*****")
# print("*****")
# print("*****")
# print("*****")
# print("*****")
'''
*****
*****
****
*****
***** 
'''

# for문을 이용한 정사각형 만들기
# 1.
# for i in range(5):
#     # print("*****")
#     # print("*"*5)

# 2.
# rng = [1, 2, 3, 4, 5]
# for i in rng:
#     print("*"*5)
    
# 방법1.
# for item in range(5):
#     print("*****")

# 방법2.
# for item in range(5):
#     print("".rjust(5, "*"))
   
# 방법3.
# for item in range(5):
#     print("*" * 5)

# 방법4.
# [print("*"*5) for item in range(5)]

for item in range(5):
    for item1 in range(5):
        print("*", end="")
    print()

# print의 end는 마지막에 무엇을 넣을지 명시
# print("*", end="하하")
# print("*", end="")

# 배열의 평균값
# 머쓱이 보다 키 큰 사람
# 배열 뒤집기
# 배열 자르기
# 369게임

# 짝수 홀수 개수
# 외계행성의 나이
# 암호 해독

# 다음 주
'''
데이터 입출력
클래스
제네릭
numpy / pandas
크롤링

HTML CSS
자바스크립트
부트스트랩
'''