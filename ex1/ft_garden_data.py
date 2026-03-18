"""
ft_garden_data.py

This file introduces a basic Python class used to represent plant data.
The Plant class stores a plant's name, height, and age, and provides a
method to display this information.

The program creates several Plant objects, places them in a list, and
prints their details using a loop. This demonstrates how objects can be
grouped and processed together in a simple data structure.
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


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    garden = [
      Plant("Rose", 25, 30),
      Plant("Sunflower", 80, 45),
      Plant("Cactus", 15, 120)
    ]
    for i in range(0, 3):
        garden[i].get_info()
