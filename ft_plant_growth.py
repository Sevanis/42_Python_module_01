#!/bin/python3

class Plant:

    list_plant: list["Plant"] = []
    total: int = 0

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.ages = age
        Plant.list_plant += [self]
        Plant.total += 1

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.ages} days old")

    def grow(self) -> None:
        self.height += 1

    def age(self) -> None:
        self.ages += 1


if __name__ == "__main__":
    p1 = Plant("Rose", 12, 30)

    day = 7
    rose_height = p1.height

    print("=== Day 1 ===")
    p1.get_info()

    print(f"=== Day {day} ===")

    temp = day
    while temp != 0:
        p1.grow()
        p1.age()
        temp -= 1

    p1.get_info()
    if day == 7:
        print(f"Growth this week: +{p1.height - rose_height}cm")
    else:
        print(f"Growth during {day} day: +{p1.height - rose_height}cm")
