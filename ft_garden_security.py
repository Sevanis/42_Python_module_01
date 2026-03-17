#!/bin/python3

class Plant:

    list_plant: list["Plant"] = []
    total: int = 0

    def __init__(self, name: str, height: int, age: int) -> None:
        self._name: str = name
        self._height: int = height
        self._ages: int = age
        Plant.list_plant += [self]
        Plant.total += 1
        print(f"Plant created: {self.get_name()}\n")

    def set_age(self, value: int) -> None:
        if value < 0:
            print(f"\nInvalid operation attempted: "
                  f"age {value} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._ages = value
            print(f"Age updated: {self._ages} days [OK]")

    def set_height(self, value: int) -> None:
        if value < 0:
            print(f"\nInvalid operation attempted: "
                  f"height {value}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = value
            print(f"Height updated: {self._height}cm [OK]")

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._ages

    def get_info(self) -> str:
        return f"{self._name} ({self._height}cm, {self._ages} days)"


if __name__ == "__main__":

    print("=== Garden Security System ===")

    plant = Plant("Rose", 20, 25)
    plant.set_height(25)
    plant.set_age(30)
    plant.set_age(-5)

    print(f"\nCurent plant: {plant.get_info()}")
