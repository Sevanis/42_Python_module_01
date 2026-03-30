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

    def show(self) -> None:
        print( f"{self._name} : {self._height}cm, {self._ages} days old")


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._bloom = False

    def bloom(self) -> None:
        print(f"[asking the {self._name} to bloom]")
        self._bloom = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if  not self._bloom:
            print(f"{self._name} has not bloomed yet\n")
        else:
            print(f"{self._name}  is blooming beautifully!\n")


class Tree(Plant):
    def __init__(self, name: str, height: int,
                 age: int, trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"[asking the {self._name} to produce shade]")
        print(f"Tree {self._name} produces a shade of "
              f"{self._height}cm long and {self._trunk_diameter}cm wide.\n")

    def show(self) -> None:
        super().show()
        print( f"Trunk diameter: {self._trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: int,
                 age: int, harvest_season: str, n_value: int) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._n_value = n_value

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._n_value}\n")

    def grow_n_age(self, day: int) -> None:
        print(f"[make {self._name} grow and age for {day} days]")
        self._ages += day
        self._height += day
        self._n_value += day


if __name__ == "__main__":
    flower_1 = Flower("Rose", 25, 30, "red")
    flower_2 = Flower("Violet", 25, 30, "blue")

    tree_1 = Tree("Oak", 500, 1825, 50)
    tree_2 = Tree("Apple tree", 350, 124, 30)

    vegetable_1 = Vegetable("Tomato", 80, 90, "April", 20)
    vegetable_2 = Vegetable("Carrot", 50, 10, "January", 15)

    print("=== Garden Plant Types ===\n")

    flower_1.show()
    flower_1.bloom()
    flower_1.show()

    tree_1.show()
    tree_1.produce_shade()

    vegetable_1.show()
    vegetable_1.grow_n_age(20)
    vegetable_1.show()