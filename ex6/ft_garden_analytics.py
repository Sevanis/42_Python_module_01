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
        

    def get_info(self) -> str:
        return f"- {self._name}: {self._height}cm"

    @classmethod
    def get_cls(cls) -> str:
        cl = cls.__name__
        return cl

    def get_name(self) -> str:
        return self._name

    def grow(self) -> None:
        self._height += 1
        print(f"{self._name} grew 1cm")

    def get_height(self) -> int:
        return self._height

    @staticmethod
    def validate_height(height: int):
        print(f"Height validation test: {height > 0}")


class FloweringPlant(Plant):
    total: int = 0

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._blooming = False
        FloweringPlant.total += 1

    def bloom(self) -> None:
        self._blooming = True

    def get_info(self) -> str:
        return (f"{super().get_info()}, {self._color} "
                f"flower{' (blooming)' if self._blooming else ''}")


class PrizeFlower(FloweringPlant):
    total: int = 0

    def __init__(
        self, name: str, height: int, age: int, color: str, point: int
    ) -> None:
        super().__init__(name, height, age, color)
        self._point = point
        PrizeFlower.total += 1

    def get_info(self) -> str:
        return f"{super().get_info()}, prize point: {self._point}"


class Garden:
    list_garden: list["Garden"] = []
    total: int = 0

    def __init__(self, owner: "GardenManager") -> None:
        self._owner = owner
        self.plants: list["Plant"] = []
        Garden.list_garden += [self]

    def get_owner(self) -> "GardenManager":
        return self._owner

    def get_owner_name(self) -> str:
        return self._owner.get_name()


class GardenManager:

    class GardenStats:

        @staticmethod
        def get_all_plants(manager: "GardenManager") -> list["Plant"]:
            plants: list["Plant"] = []
            for garden in manager.gardens:
                for plant in garden.plants:
                    plants += [plant]
            return plants

        @staticmethod
        def manager_report(man: "GardenManager") -> None:
            if man.total_plant == 0:
                print(
                    "----------------------------------"
                    "--------------------------------",
                )
                print(f"{man._name} don't have plant")
                print(
                    "----------------------------------"
                    "--------------------------------",
                )
            else:
                print(
                    "----------------------------------"
                    "--------------------------------",
                )
                print(f"=== {man.get_name()}'s Garden Report ===")
                print("Plants in garden:")
                print(
                    *(
                        p.get_info()
                        for p in GardenManager.GardenStats.get_all_plants(man)
                    ),
                    sep="\n",
                )
                print(
                    f"\nPlants added: {man.total_plant}, "
                    f"Total growth: {man.total_growth}cm"
                )
                print(
                    f"Plant types: "
                    f"{man.plant_type[0]} regular, "
                    f"{man.plant_type[1]} flowering, "
                    f"{man.plant_type[2]} prize flowers"
                )
                print(
                    "----------------------------------"
                    "--------------------------------",
                )

    list_garden_manager: list["GardenManager"] = []
    garden_managed: int = 0

    def __init__(self, name: str) -> None:
        self._name = name
        self._score = 0
        self.gardens: list["Garden"] = []
        self.total_plant = 0
        self.total_growth = 0
        self.plant_type: list[int] = [0, 0, 0]
        GardenManager.list_garden_manager += [self]

    def create_garden(self) -> Garden:
        garden = Garden(self)
        self.gardens += [garden]
        GardenManager.garden_managed += 1
        return garden

    def add_plant(self, plant: Plant, garden: Garden):
        if garden.get_owner() is self:
            garden.plants += [plant]
            self.total_plant += 1
            self._score += 20
            if plant.get_cls() == "Plant":
                self.plant_type[0] += 1
            elif plant.get_cls() == "FloweringPlant":
                self.plant_type[1] += 1
            else:
                self.plant_type[2] += 1
            print(f"Added {plant.get_name()} to {self._name}'s garden")
        else:
            print(
                f"{self._name} can't add plant in "
                f"{garden.get_owner_name()}'s garden [ERROR]"
            )

    def grow_all(self):
        print(f"{self._name} is helping all plants grow...")
        for plant in GardenManager.GardenStats.get_all_plants(self):
            self.total_growth += 1
            self._score += 20
            plant.grow()

    def get_name(self) -> str:
        return self._name

    def get_score(self) -> str:
        return f"{self._name}: {self._score}"

    @classmethod
    def create_garden_network(cls):
        print("Garden scores -", end=' ')
        print(
            *(
                manager.get_score()
                for manager in cls.list_garden_manager
            ),
            sep=", ")
        print(f"Total gardens managed: {cls.garden_managed}")


if __name__ == "__main__":
    Plant.is_year(30)
    Plant.is_year(400)
    # flower_1 = FloweringPlant("Rose", 25, 30, "red")
    # flower_2 = FloweringPlant("Violet", 25, 30, "blue")
    # flower_3 = Plant("Oak tree", 248, 302)
    # flower_4 = PrizeFlower("Sunflower", 120, 38, "yellow", 10)

    # alice = GardenManager("Alice")
    # garden = alice.create_garden()
    # bob = GardenManager("Bob")
    # garden_2 = bob.create_garden()

    # print("=== Garden Management System Demo ===\n")
    # alice.add_plant(flower_3, garden)
    # alice.add_plant(flower_1, garden)
    # alice.add_plant(flower_4, garden)
    # bob.add_plant(flower_2, garden_2)
    # flower_1.bloom()
    # flower_4.bloom()
    # print()
    # alice.grow_all()
    # print()
    # GardenManager.GardenStats.manager_report(alice)
    # # GardenManager.GardenStats.manager_report(bob)
    # Plant.validate_height(flower_1.get_height())
    # GardenManager.create_garden_network()
