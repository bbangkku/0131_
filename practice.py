# 1번 
def ko_hello(name):
    print(f'안녕하세요, {name}님!')

def en_hello(name):
    print(f'Hello, {name}!')

# 2번
def add_emoji(name, func):
    func(name)   
    print('^~^//')

# 3번
def emoji_decorator(func):
    def wrapper(name):
        func(name)
        print('^~^//')
    
    return wrapper

#해보기
#@add_tears
@emoji_decorator
def ko_hello(name):
    print(f'안녕하세요, {name}님!')

@emoji_decorator
def en_hello(name):
    print(f'Hello, {name}!')

# ko_hello('병국')

# add_emoji('병국', ko_hello)
# add_emoji('병국', en_hello)

# new_func = emoji_decorator(ko_hello)
# new_func('병국')
# #위랑 같은말
# (emoji_decorator(ko_hello))('병국')


# class Myclass:
    
#     def method(self):
#         return 'instance method'
    
#     @classmethod
#     def classmethod(cls):
#         return 'class method'
    
#     @staticmethod
#     def staticmethod():
#         return 'static method'

# my_class = Myclass()
# print(my_class.method())
# print(my_class.classmethod())
# print(my_class.staticmethod())


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
#     def get_age(self):
#         return self.__age


# p1 = Person('김싸피', 30)
# print(p1.get_age()) # 30

# print(p1.__age) # AttributeError: 'Person' object has no attribute '__age'

# class Person:
#     def __init__(self):
#         self._age = 0


#     @property
#     def age(self): # getter
#         print('getter 호출 !')
#         return self._age
    
#     @age.setter
#     def age(self, age): # setter
#         print('setter 호출 !')
#         self._age = age

    

# # ///

# p1 = Person()
# p1._age = 25 # 이렇게 해도 안됨 게터 세터 이용
# print(p1._age) # 25 에러안남 하지만 이렇게 하면 안됨
# # p1.set_age(25)
# # print(p1.get_age())
# # 이것도 불편하다1




# # 상속을 쓰자 !!
# # 다중상속은 자제해라

# class Monster:
#     def __init__(self, condition):
#         self.condition = condition
#     def get_status():
#         print('내 상태는', self.condition)

# class Goblen:
#     def __init__(self, hp):
#         self.hp = hp
    
#     def attack(self):
#         print('몽둥이를 휘두른다')
    
#     def avoid(self):
#         print('공격을 회피했다')

# class Stone_Goblen(Goblen): 
#     # 부모와 다른 동작을 하는 메서드(재정의 - 오버라이딩)
#     def attack(self):
#         print('돌을 던진다')

#     # 부모와 완벽히 동일한 동작을 하는 메서드 - 생략 가능
#     # def __init__(self, hp): (생성자도 생략가능한가요 ? 네)
#     #     self.hp = hp        
#     # def avoid(self):
#     #     print('공격을 회피했다')

# # 파이썬의 다중 상속 -> 하지마라
# class IceGoblen(Goblen):
#     def __init__(self, hp, mp):
#         # 부모와 동일
#         # self.hp = hp
#         # 부모와 동일한 속성
#         # - > super 를 사용하여 부모의 생산자를 호출
#         super().__init__(hp)
#         # 자식에게만 있는 속성
#         self.mp = mp

#     def attack(self):
#         print('돌을 던진다')

#     def skill(self):
#         print('얼음돌을 던진다')
    
    

# class Person:
#     def __repr__(self):
#         return "Hello"

# p = Person()
# print(p) # Hello
# print(repr(p)) # Hello

# # 먼저 str을 찾고 첫번쨰꺼출력, 두번쨰꺼는 str이 없으니까
# # 내장 __repr__으로 본다
# class Person:
#     def __str__(self):
#         return "Hello"

# p = Person()
# print(p) # Hello
# print(repr(p)) # <__main__.Person object at 0x0000022EC87B8D00>

try:
    num = input('숫자: ')
    print(int(num))
except:
    print('숫자가 아니다')