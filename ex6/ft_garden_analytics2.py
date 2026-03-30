#!/bin/python3

class Plant:

    list_plant: list["Plant"] = []
    total: int = 0

    def __init__(self, name: str, height: int, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age
        Plant.list_plant += [self]
        Plant.total += 1
    
    @staticmethod
    def is_year(day: int) -> None:
        print(f"Is {day} days more than a year? -> {True if day >= 365 else False}")

    def show(self) -> None:
        print( f"{self._name} : {self._height}cm, {self._age} days old")


class Flower(Plant):
    class FlowerStat:
        def __init__(self) -> None:
            self.grow_call = 0
            self.age_call = 0
            self.show_call = 0


    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._bloom = False
        self._stat = Flower.FlowerStat()

    def bloom(self) -> None:
        print(f"[asking the {self._name} to bloom]")
        self._bloom = True

    def show(self) -> None:
        self._stat.show_call += 1
        super().show()
        print(f"    Color: {self._color}")
        if  not self._bloom:
            print(f"    {self._name} has not bloomed yet")
        else:
            print(f"    {self._name}  is blooming beautifully!")

    
    def show_stat(self) -> None:
        print(f"[statistics for {self._name}]")
        print(f"Stats: {self._stat.grow_call} grow, ",
              f"{self._stat.age_call} age, ",
              f"{self._stat.show_call} show")
    

class Seed(Flower):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self._bloom = False
        self._seed_number = 0
    
    def grow_age_bloom(self, day: int) -> None:
        print(f"[make {self._name} grow, age and bloom]")
        self._bloom = True
        self._age += day
        self._height += day
        self._seed_number+= day
    
    def show(self) -> None:
        super().show()
        print(f"    Seeds: {self._seed_number}")


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



if __name__ == "__main__":

    rose = Flower("Rose", 25, 30, "red")
    sunflower = Seed("Sunflower",80, 45, "yellow")
    oak = Tree("Oak", 500, 1825, 50)

    rose.show()
    rose.show()
    
    rose.show_stat()

