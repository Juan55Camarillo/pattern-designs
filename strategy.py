'''
Strategy pattern designs example
it allows make an object can behave in different ways
(which will be define in the moment of its instantiation or make)
'''

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Map():
    def __init__(self, generateMap: GenerateMap) -> None:

        self._generateMap = generateMap

    @property
    def generateMap(self) -> generateMap:

        return self._generateMap

    @generateMap.setter
    def generateMap(self, generateMap: GenerateMap) -> None:

        self._generateMap = generateMap

    def RandomSeed(self) -> None:

        print("Generating a random location of the objects:")
        result = self._generateMap.randomizer([" Map size: 1212", " Enemies location: 2737", " Dungeons Location: 6574"])
        print(",".join(result))

class Generator(ABC):

    @abstractmethod
    def randomizer(self, data: List):
        pass
    
class WaterLand(Generator):
    def randomizer(self, data: List) -> List:
        return sorted(data)

class EarthLand(Generator):
    def randomizer(self, data: List) -> List:
        return reversed(sorted(data))

class main():
    map1 = Map(WaterLand())
    print("Generating a random map of water.")
    map1.RandomSeed()
    print()

    map2 = Map(EarthLand())
    print("Generating a random map of earth.")
    map1.RandomSeed()

