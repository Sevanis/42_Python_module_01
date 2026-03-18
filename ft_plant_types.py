#!/bin/python3

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


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color

    def bloom(self) -> None:
        print(f"{self._name} is blooming beautifully!\n")

    def get_info(self) -> str:
        return f"{super().get_info()}, {self._color} color"


class Tree(Plant):
    def __init__(self, name: str, height: int,
                 age: int, trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"{self._name} provide "
              f"{self._height * 0.4} square meters of shade\n")

    def get_info(self) -> str:
        return f"{super().get_info()}, {self._trunk_diameter}cm diameter"


class Vegetable(Plant):
    def __init__(self, name: str, height: int,
                 age: int, harvest_season: str) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season

    def nutritional_value(self) -> None:
        if self._name == "Tomato":
            print(f"{self._name} is rich in vitamin C")
        else:
            print(f"{self._name} is rich in vitamin A")

    def get_info(self) -> str:
        return f"{super().get_info()}, {self._harvest_season} harvest"


if __name__ == "__main__":
    flower_1 = Flower("Rose", 25, 30, "red")
    flower_2 = Flower("Violet", 25, 30, "blue")

    tree_1 = Tree("Oak", 500, 1825, 50)
    tree_2 = Tree("Apple tree", 350, 124, 30)

    vegetable_1 = Vegetable("Tomato", 80, 90, "summer")
    vegetable_2 = Vegetable("Carrot", 50, 10, "winter")

    print("=== Garden Plant Types ===\n")

    print(flower_1.get_info())
    flower_1.bloom()

    print(tree_1.get_info())
    tree_1.produce_shade()

    print(vegetable_1.get_info())
    vegetable_1.nutritional_value()
