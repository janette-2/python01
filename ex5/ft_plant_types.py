"""
ft_plant_types.py

This file expands the basic Plant class by introducing inheritance and
specialized plant types. Flower, Tree, and Vegetable all extend the
Plant class, adding their own attributes and behaviors while reusing
the common features defined in the parent class.

Each subclass overrides get_info() to display its specific details and
demonstrates how inherited methods can be customized. The script creates
several examples of each plant type and prints their information,
showing how different objects can share a common structure while
behaving in unique ways.
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


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

    def get_info(self):
        print(f"{self.name} (Flower): {self.height}cm, {self.age} days,"
              f" {self.color} color")
        self.bloom()


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> int:
        area = (314 * (self.trunk_diameter ** 2)) // 10000
        return area

    def get_info(self):
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days, "
              f"{self.trunk_diameter}cm diameter")
        print(f"{self.name} provides {self.produce_shade()} "
              f"square meters of shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season: str,
                 nutritional_value: str):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def describe_nutrition(self) -> None:
        print(f"{self.name} is rich in {self.nutritional_value}")

    def get_info(self):
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} days,"
              f" {self.harvest_season} harvest")
        self.describe_nutrition()


def ft_plant_types():
    rose = Flower("Rose", 25, 30, "red")
    oak = Tree("Oak", 500, 1825, 50)
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    print("=== Garden Plant Types ===")
    print("")
    garden = [rose, oak, tomato]
    for element in garden:
        element.get_info()
        print("")
    # print("")
    # print("=== Garden Plant Types ===")
    # print("")
    # carnation = Flower("Carnation", 28, 15, "white and purple")
    # pine = Tree("Pine", 300, 2500, 80)
    # carrot = Vegetable("Carrot", 50, 60, "spring", "vitamin A")
    # garden1 = [carnation, pine, carrot]
    # for element in garden1:
    #     element.get_info()
    #     print("")


if __name__ == "__main__":
    ft_plant_types()
