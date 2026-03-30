#!/bin/python3

class Plant:

    list_plant: list["Plant"] = []
    total: int = 0

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.ages: int = age
        Plant.list_plant += [self]
        Plant.total += 1

    def show(self) -> str:
        return f"{self.name} ({self.height}cm, {self.ages} days)"


if __name__ == "__main__":

    plant_data: list[tuple[str, int, int]] = [
                ("Rose", 25, 30),
                ("Oak", 200, 365),
                ("Cactus", 5, 90),
                ("Sunflower", 80, 45),
                ("Fern", 15, 120),
                ("Coconut", 20, 20)]

    print("=== Plant Factory Output ===")
    for p in plant_data:
        plant = Plant(*p)
        print(f"created: {plant.show()}")