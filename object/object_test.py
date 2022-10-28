# from animal import Animal

# new_animal = Animal(0)

# new_animal.eat()

# new_animal.get_age()

from animal import Animal
from cat import Cat  # cat 파일에서 Cat 클래스 가져옴

Animal.hello()  # static 메소드가 된다. 

print()

a = Animal(12)
b = Cat("나옹", 5)

a.eat()
b.eat()

print()

a.get_age()
b.get_age()  # cat에서 get_age를 만들지 않았는데도 왜 에러가 나지 않는가? 부모의 기능을 물려받았기 때문


print()

Animal.get_count()  # 어떻게 이렇게 계산이 되는가?
Cat.get_count()