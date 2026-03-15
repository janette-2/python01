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

    def bloom(self) -> None:
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
        diameter_m = self.trunk_diameter / 100
        area = 3.14 * (diameter_m ** 2) * 100
        return (int(area))

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
    carnation = Flower("Carnation", 28, 15, "white and purple")
    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 300, 2500, 80)
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 50, 60, "spring", "vitamin A")
    print("=== Garden Plant Types ===")
    print("")
    garden = [rose, oak, tomato]
    for element in garden:
        element.get_info()
        print("")
    print("")
    print("=== Garden Plant Types ===")
    print("")
    garden1 = [carnation, pine, carrot]
    for element in garden1:
        element.get_info()
        print("")


if __name__ == "__main__":
    ft_plant_types()
