from decimal import Decimal
import math

temp = 1 + 2 * 3
# 연산자에는 순서가 있다. 예를 들어 * 가 + 보다 우선이다.
# temp=7

temp = (1+2) *3
# 연산 우선순위를 바꾸기 위해서 ()를 사용한다.
# temp=9

# temp = 1 / 0  # ZeroDivisionError: division by zero
# 숫자는 0으로 나눌 수 없다.

temp = 1.1 + 0.1
# 실수 중에서 2진수로 계산할 수 없는 숫자는 근사값이 나온다.
# temp=1.2000000000000002

# 근사값이 안 나오게 하는 함수 사용
temp = Decimal('1.1') + Decimal('0.1')
temp = float(temp)
# Decimal을 사용하면 정확한 실수 값을 계산할 수 있다.
# but 자리수가 한정되어 있다.
# temp=1.2

temp = 11
temp = bin(temp)
# bin을 사용하면 2진수로 바꿀 수 있다.
# temp='0b1011'  # 0b는 이진수라는 뜻

temp = 11
temp = oct(temp)
# oct를 사용하면 8진수로 바꿀 수 있다.
# temp='0o13'

temp = 11
temp = hex(temp)
# hex를 사용하면 16진수로 바꿀 수 있다.
# temp='0xb'  # 0x는 16진수라는 뜻 / 10 이상은 숫자로 표현할 수 없어 알파벳 사용
# 16진수의 숫자(a = 10, f = 15)
# 0 1 2 3 4 5 6 7 8 9 a b c d e f

print(f'{temp=}')

