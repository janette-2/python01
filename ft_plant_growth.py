class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name  # Atributo de instancia
        self.height = height  # Atributo de instancia
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


def ft_plant_growth(name: str, height: int, age: int):
    plant = Plant(name, height, age)
    height1 = plant.height
    print("=== Day 1 ===")
    print(f"{plant.name}: {plant.height}cm, {plant.age} days old")
    for day in range(6):
        plant.aged()
        plant.growth()
    height7 = plant.height
    print("=== Day 7 ===")
    print(f"{plant.name}: {plant.height}cm, {plant.age} days old")
    print(f"Growth this week: +{height7 - height1}cm")


if __name__ == "__main__":
    ft_plant_growth("Rose", 25, 30)
