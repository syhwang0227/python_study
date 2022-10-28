
# class Animal:
#     def __init__(self, age) -> None:
#         self.age = age
    
#     def eat(self):
#         print(f"동물이 음식을 먹었습니다.")
    
#     def get_age(self):
#         print(f"동물의 나이는 {self.age}살 입니다.")

# 고양이나 개가 태어나는 것이지 동물이 태어날 수는 없다.
class Animal:

    count = 0  # 클래스 변수 / 해당 클래스가 가지고 있는 변수
    
    # 초기화함수
    def __init__(self,
                 age: int = 0
                 ):
        """

        Args:
            age (int, optional): 동물의 나이. 기본값은 0.
        """

        self.age = age

        self.name = f"{Animal.count}번"

        Animal.count = Animal.count + 1

        return  # return 뒤에 데이터가 없을 때는 return을 안 쓰는 것과 같다. 명시적으로 보여줄 때 쓰곤한다.

    def eat(self):
        print(f"동물 {self.name}이 음식을 먹었습니다.")

    def get_age(self):
        print(f"동물 '{self.name}'의 나이는 {self.age}살 입니다.")
    # self가 있으면 인스턴스 메소드

    @classmethod  # @가 붙어서 함수 앞에 붙는 것을 어노테이션이라고 한다 / 붙어 있는 함수의 스타일 (속성)을 알려준다.
    def get_count(cls):
        print(f"동물이 {cls.count}마리 생성되었습니다.")
    # @classmethod 가 붙어있거나 () 괄호 안에 self 가 없으면 클래스 메소드
    

    @staticmethod
    def hello():
        print(f"동물 농장에 오신 것을 환영합니다.")
    # 인스턴스나 클래스메소드가 아님