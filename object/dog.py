from animal import Animal


class Dog(Animal):
    
    count = 0
    
    def cry():
        print("강아지가 짖는다. '으르르르렁! 왕왕!'")
    
    def cute():
        print("강아지 특징1. 귀여움")
        
    def love():
        print("강아지 특징2. 사랑스러움")
    
    @classmethod
    def get_count(cls):
        print("강아지는 {}마리 입니다.".format(cls.count))
        

