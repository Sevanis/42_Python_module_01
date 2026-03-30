#!/bin/python3

class Plant:

    list_plant: list["Plant"] = []
    total: int = 0

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        Plant.list_plant += [self]
        Plant.total += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    p1 = Plant("Rose", 12, 30)
    p2 = Plant("Sunflower", 35, 13)
    p3 = Plant("Cactus", 22, 25)
    p4 = Plant("Coconut", 25, 30)
    p5 = Plant("Violet", 30, 24)

    print("=== Garden Plant Registry ==")
    for plant in Plant.list_plant:
        plant.show()
