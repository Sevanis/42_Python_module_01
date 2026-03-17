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

    def get_name(self) -> str:
        return self._name

    def grow(self) -> None:
        self._height += 1
        print(f"{self._name} grew 1cm")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color

    def bloom(self) -> None:
        print(f"{self._name} is blooming beautifully!\n")

    def get_info(self) -> str:
        return f"{super().get_info()}, {self._color} color"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int, point: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self._point = point

    def get_info(self) -> str:
        return f"{super().get_info()}, {self._point} point"


class Garden:
    list_garden: list["Garden"] = []

    def __init__(self, owner: "GardenManager") -> None:
        self._owner = owner
        self.plants: list["Plant"] = []

    def get_owner(self) -> "GardenManager":
        return self._owner

    def get_owner_name(self) -> str:
        return self._owner.get_name()

class GardenManager:
    class GardenStats:
        pass

    list_garden_manager: list["GardenManager"] = []

    # @classmethod
    # def create_garden_network(cls) -> None:

    def __init__(self, name: str) -> None:
        self._name = name
        self.gardens: list["Garden"] = []
        GardenManager.list_garden_manager += [self]

    def create_garden(self) -> Garden:
        garden = Garden(self)
        self.gardens += [garden]
        return garden

    def add_plant(self, plant: Plant, garden: Garden):
        if garden.get_owner() is self:
            garden.plants += [plant]
            print(f"Added {plant.get_name()} to {self._name}'s garden")
        else:
            print(f"{self._name} can't add plant in {garden.get_owner_name()}'s garden [ERROR]")

    def get_all_plants(self) -> list["Plant"]:
        plants: list["Plant"] = []
        for garden in self.gardens:
            for plant in garden.plants:
                plants += [plant]
        return plants

    def grow_all(self):
        print(f"{self._name} is helping all plants grow...")
        for plant in self.get_all_plants():
            plant.grow()

    def get_name(self) -> str:
        return self._name

if __name__ == "__main__":
    flower_1 = FloweringPlant("Rose", 25, 30, "red")
    flower_2 = FloweringPlant("Violet", 25, 30, "blue")
    flower_3 = Plant("Oak tree", 248, 302)

    bob = GardenManager("Bob")
    garden_2 = bob.create_garden()

    alice = GardenManager("Alice")
    garden = alice.create_garden()

    alice.add_plant(flower_1, garden)
    alice.add_plant(flower_2, garden)

    bob.add_plant(flower_3, garden_2)

    alice.grow_all()

    print("\n==== Alice garden ====")
    print(*(p.get_info() for p in garden.plants), sep="\n")


