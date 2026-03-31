#!/bin/python3


class Plant:

    list_plant: list["Plant"] = []
    total: int = 0

    class PlantStat:
        def __init__(self) -> None:
            self._grow_call = 0
            self._age_call = 0
            self._show_call = 0

        def inc_grow(self) -> None:
            self._grow_call += 1

        def inc_age(self) -> None:
            self._age_call += 1

        def inc_show(self) -> None:
            self._show_call += 1

        def get_stats(self) -> tuple[int, int, int]:
            return self._grow_call, self._age_call, self._show_call

    def __init__(
        self,
        name: str,
        height: float,
        ages: int,
    ) -> None:
        self._name = name
        self._height = height
        self._age = ages
        self._stat = Plant.PlantStat()
        Plant.list_plant += [self]
        Plant.total += 1

    @staticmethod
    def is_year(day: int) -> None:
        print(f"Is {day} days more than a year? ",
              f"-> {True if day >= 365 else False}")

    def age(self, day: int) -> None:
        self._stat.inc_age()
        self._age += day

    def grow(self, day: int) -> None:
        self._stat.inc_grow()
        self._height += day

    def get_stats(self) -> tuple[int, int, int]:
        return self._stat.get_stats()

    def get_name(self) -> str:
        return self._name

    def show(self) -> None:
        self._stat._show_call += 1
        print(f"{self._name} : {self._height}cm, {self._age} days old")


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
        print(f"    Color: {self._color}")
        if not self._bloom:
            print(f"    {self._name} has not bloomed yet")
        else:
            print(f"    {self._name}  is blooming beautifully!")


class Seed(Flower):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self._bloom = False
        self._seed_number = 0

    def grow_age_bloom(self, day: int) -> None:
        print(f"[make {self._name} grow, age and bloom]")
        self._bloom = True
        self.age(day)
        self.grow(day)
        self._seed_number += day

    def show(self) -> None:
        super().show()
        print(f"    Seeds: {self._seed_number}")


class Tree(Plant):
    class TreeStat(Plant.PlantStat):
        def __init__(self) -> None:
            super().__init__()
            self._shade_call = 0

        def inc_shade(self) -> None:
            self._shade_call += 1

        def get_shade(self) -> int:
            return self._shade_call

    def __init__(self, name: str, height: int,
                 age: int, trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.t_stat = Tree.TreeStat()
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        self.t_stat.inc_shade()
        print(f"[asking the {self._name} to produce shade]")
        print(
            f"Tree {self._name} produces a shade of "
            f"{self._height}cm long and {self._trunk_diameter}cm wide."
        )

    def get_shade(self) -> int:
        return self.t_stat.get_shade()

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")


class AnonymousPlant(Plant):
    def __init__(self) -> None:
        super().__init__("Unknown plan", 0, 0)


def show_stat(plant: "Plant") -> None:
    grow, age, show = plant.get_stats()
    print(f"[statistics for {plant.get_name()}]")
    print(f"Stats: {grow} grow, {age} age,", f"{show} show")


def show_stat_tree(tree: "Tree") -> None:
    show_stat(tree)
    print(f"{oak.get_shade()} shade")


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")
    Plant.is_year(30)
    Plant.is_year(400)

    print()

    print("=== Flower")
    rose = Flower("Rose", 15, 10, "red")

    rose.show()
    show_stat(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow(8)
    rose.bloom()

    rose.show()
    show_stat(rose)

    print()

    print("=== Tree")
    oak = Tree("Oak", 200, 365, 5)

    oak.show()
    show_stat_tree(oak)

    oak.produce_shade()

    show_stat_tree(oak)

    print()

    print("=== Seed")
    sunflower = Seed("Sunflower", 80, 45, "yellow")

    sunflower.show()

    sunflower.grow_age_bloom(20)

    sunflower.show()
    show_stat(sunflower)

    print()

    print("=== Anonymous")
    unknown = AnonymousPlant()

    unknown.show()
    show_stat(unknown)
