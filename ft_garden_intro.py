#!/bin/python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":

    plant1: Plant = Plant("Rose", 25, 30)

    print("=== Welcome to My Garden ===")
    print("\n")
    print(f"Plant: {plant1.name}")
    print(f"Height: {plant1.height}cm")
    print(f"Age: {plant1.age}days")
    print("\n")
    print("=== End of Program  ===")
