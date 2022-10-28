from animal import Animal


# Animal을 상속 받는다.
class Cat(Animal):  

    count = 0

    def __init__(self,
                 name: str = "냥",
                 age: int = 0
                 ):

        # 함수에 대한 설명을 붙일 수 있음 - autoDocstring
        """

        Args:
            name (str, optional): 고양이의 이름. 기본값은 "냥".
            age (int, optional): 고양이의 나이. 기본값은 0.
        """

        super().__init__(age)  # Animal에 있는 __init__ 의미 / 부모 __init__ 이 실행된다.

        self.name = name

        Cat.count = Cat.count + 1

        return

    def eat(self):
        print(f"고양이 '{self.name}'이 음식을 먹었습니다.")  # 부모와 내용이 같으면 새로 생성한 내용이 나온다. 하지만 기능이 잘 구현되어 있으면 다시 만들 필요는 없다.

    @classmethod
    def get_count(cls):
        print(f"고양이가 {cls.count}마리 생성되었습니다.")