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

    def get_info(self) -> str:
        return f"{self.name} ({self.height}cm, {self.ages} days)"
    
if __name__ == "__main__":
    plant_data = [
    ("Rose", 25, 30),
    ("Oak", 200, 365),
    ("Cactus", 5, 90),
    ("Sunflower", 80, 45),
    ("Fern", 15, 120),
    ("Coco", 20, 20)]

    for name, height, age in plant_data:
        plant = Plant(name, height, age)
        print(f"created: {plant.get_info()}")
    
    print(f"\nTotal plants created: {Plant.total}")