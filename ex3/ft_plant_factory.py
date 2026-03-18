"""
ft_plant_factory.py

This file uses the Plant class to demonstrate how multiple objects can
be created quickly and organized together. Each Plant instance is fully
initialized through its constructor, meaning it is ready to use
immediately after creation.

The script acts as a simple "factory" by creating several Plant objects
with different starting values. It then prints the details of each
created plant and reports the total number of plants produced. This
illustrates how object construction can be repeated efficiently and how
collections of objects can be processed in a loop.
"""


class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        print(
            f"{(self.name)} : {self.height}cm,"
            f" {self.age} days old"
            )

    def growth(self):
        self.height += 1

    def aged(self):
        self.age += 1


def ft_plant_factory() -> None:
    factory = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120),
    ]
    count = 0
    print("=== Plant Factory Output ===")
    for element in factory:
        count += 1
        print(
            f"Created: {element.name} ({element.height}cm,"
            f" {element.age} days)"
        )
    print("")
    print(f"Total plants created: {count}")


if __name__ == "__main__":
    ft_plant_factory()
