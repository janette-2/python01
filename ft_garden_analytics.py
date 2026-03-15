class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm"

    def growth(self):
        self.height += 1

    def aged(self):
        self.age += 1


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")

    def get_info(self) -> str:
        info_plant = super().get_info()
        return f"{info_plant}, {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int, color: str,
                 points: int):
        super().__init__(name, height, age, color)
        self.points = points

    def get_info(self) -> str:
        info_flower = super().get_info()
        return (f"{info_flower}, Prize points: {self.points}")
