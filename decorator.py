'''
Decorator pattern design example
It allows add an object's functionality in case that are
necessary using heredity
'''
from abc import ABC, abstractmethod

class Ninja(ABC):

    @abstractmethod
    def style(self):
        pass

class Village(Ninja, ABC):
    def __init__(self, ninja):
        self._ninja = ninja

    @abstractmethod
    def style(self):
        pass

class Hidden_Leaf_Village(Village):
    def style(self):
        self._ninja.style()
        print("Fire country ninja: Leaf Style")
        

class Hidden_Sand_Village(Village):
    def style(self):
        self._ninja.style()
        print("Wind country ninja: Sand Style")

class Normal_ninja(Ninja):
    def style(self):
        pass


class main():
    ninja = Normal_ninja()
    naruto = Hidden_Leaf_Village(ninja)
    gaara = Hidden_Sand_Village(ninja)
    print("Naruto style is: ")
    naruto.style()
    print("Gaara style is: ")
    gaara.style()
   
    
main()
