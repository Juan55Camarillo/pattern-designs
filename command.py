'''
Command pattern design example
If we have some objects that do a similar action in different ways,
then we want that it process the correct way depending of the requested
object
'''
from abc import ABC, abstractmethod

class TV(ABC):
    @abstractmethod
    def action(self):
        pass

class Change_Channel(TV):
    def __init__(self, TV):
        self.tv = TV

    def action(self):
        self.tv.Change_Channel()
        

class Turn_Off(TV):
    def __init__(self, TV):
        self.tv = TV

    def action(self):
        self.tv.Turn_Off()

class VolumenUp(TV):
    def __init__(self, TV):
        self.tv = TV

    def action(self):
        self.tv.VolumenUp()

class ActionMenu:
    def Change_Channel(self):
        print("Changing channel")
        
    def Turn_Off(self):
        print("Turning Off")
        
    def VolumenUp(self):
        print("Uppering Volumen")

class Actioner:
    def __init__(self):
        self._actions = []

    def requestActions(self, TV):
        self._actions.append(TV)
        TV.action()

class main():
    menu = ActionMenu()
    tv_turnOff = Turn_Off(menu)
    tv_change_chann = Change_Channel(menu)
    tv_Vol_Up = VolumenUp(menu)

    act = Actioner()
    act.requestActions(tv_Vol_Up)
    act.requestActions(tv_change_chann)
    act.requestActions(tv_Vol_Up)
    act.requestActions(tv_turnOff)

        
    
        
        
