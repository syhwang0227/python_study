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