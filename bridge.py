'''
Bridge pattern design example
It allows disengage an abstraction of its implementation, so both can
vary in independent ways
'''

from abc import ABC, abstractmethod

class Gender(ABC):

    @abstractmethod
    def select_gender(self):
        pass

class shape_body(ABC):
    def __init__(self, gender):
        self.gender = gender

    @abstractmethod
    def body_size(self):
        pass

class Warrior(shape_body):
    def __init__(self, gender):
        super(Warrior, self).__init__(gender)

    def body_size(self):
        print("Body size choosed to Warrior class: Stronger body. ")
        self.gender.select_gender(self)

class Assasin(shape_body):
    def __init__(self, gender):
        super(Assasin, self).__init__(gender)

    def body_size(self):
        print("Body size choosed to Assasin class: Light body")
        self.gender.select_gender(self)

class Man(Gender):
    def select_gender(self):
        print("Gender choosed: Man")

class Woman(Gender):
    def select_gender(self):
        print("Gender choosed: Woman")

class main():
    character1 = Warrior(Man)
    character1.body_size()
    print(" ")
    character2 = Assasin(Woman)
    character2.body_size()

    


