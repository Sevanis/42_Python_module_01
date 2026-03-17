#!/bin/python3

class GardenManager:
    def __init__(self, name: str) -> None:
        self._name = name


class GardenStats:
    pass


class Plant:
    list_plant: list["Plant"] = []
    total: int = 0

    def __init__(self, name: str, height: int, age: int) -> None:
        self._name = name
        self._height = height
        self._ages = age
        Plant.list_plant += [self]
        Plant.total += 1

    def get_info(self) -> str:
        cls = self.__class__.__name__
        return f"{self._name} ({cls}): {self._height}cm, {self._ages} days"
    
    def grow(self) -> None:
        self._height += 1


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color

    def bloom(self) -> None:
        print(f"{self._name} is blooming beautifully!\n")

    def get_info(self) -> str:
        return f"{super().get_info()}, {self._color} color"


class PrizeFlower(Plant):
    def __init__(self, name: str, height: int, age: int, point: int) -> None:
        super().__init__(name, height, age)
        self._point = point

    def get_info(self) -> str:
        return f"{super().get_info()}, {self._point} point"
    

class Garden(Plant):
    list_garden: list["Garden"] = []

    def __init__(self, name: str) -> None:
        self._name = name