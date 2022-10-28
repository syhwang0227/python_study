# 1.
# 메소드도 없고 필드도 없는 상태
# class Baby:
#     def __init__(self) -> None:
#         print("응애")


# new_baby = Baby()

class Baby:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        print("응애")
    
    def get_name(self):
        print(self.name)
    
    def get_age(self):
        print(self.age)


new_baby = Baby("hsy", 0)
new_baby.get_name()
new_baby.get_age()