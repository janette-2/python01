class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age
        self.type = "regular"

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
        self.type = "flowering"

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
        self.type = "prize"

    def get_info(self) -> str:
        info_flower = super().get_info()
        return (f"{info_flower}, Prize points: {self.points}")


class Garden:
    def __init__(self, owner: str):
        self.owner = owner
        self.plants = []  # incializacion de una lista vacía
        self.total_plants = 0
        self.total_growth = 0
        self.total_regular = 0
        self.total_flowering = 0
        self.total_prize = 0

    def add_plant(self, plant: Plant) -> None:
        self.total_plants += 1
        self.plants = self.plants + [plant]
        if plant.type == "regular":
            self.total_regular += 1
        if plant.type == "flowering":
            self.total_flowering += 1
        if plant.type == "prize":
            self.total_prize += 1
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for element in self.plants:
            element.growth()
            self.total_growth += 1
            print(f"{element.name} grew 1cm")

    def get_report(self) -> None:
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for element in self.plants:
            info = element.get_info()
            print(f"- {info}")
        print("")
        print(f"Plants added: {self.total_plants}, "
              f"Total growth: {self.total_growth}cm")
        print(f"Plants types: {self.total_regular} regular,"
              f" {self.total_flowering} flowering,"
              f" {self.total_prize} prize flowers")


class GardenManager:
    total_gardens = 0  # Inicializar variable de clase

    def __init__(self):
        self.gardens = []

    def add_garden(self, garden: Garden) -> None:
        self.gardens += [garden]  # Conversion de objeto tipo Garden a tipo Lista, para poder adaptarse a la variable
        GardenManager.total_gardens += 1

    @classmethod
    def create_garden_network(cls, list_g: list) -> "GardenManager":  # Retorno de una instancia de clase tipo "xx"
        network = GardenManager()
        for element in list_g:
            network.add_garden(element)
        return network

    class GardenStats:
        @staticmethod  # Para métodos que no dependen de self, sólo procesan valores aislados
        def validate_height(height: int) -> bool:
            return (height > 0)

        @classmethod  # Para metodos que recurran al 'self'
        def calculate_score(cls, plants: list) -> int:
            total = 0
            for element in plants:
                total = total + element.height
            return (total)


def ft_garden_analytics():
    print("=== Garden Management System Demo ===")
    print("")
    garden0 = Garden("Alice")
    garden0.add_plant(Plant("Oak Tree", 100, 500))
    garden0.add_plant(FloweringPlant("Rose", 25, 25, "red"))
    garden0.add_plant(PrizeFlower("Sunflower", 50, 43, "yellow", 10))
    print("")
    garden0.grow_all()
    print("")
    garden0.get_report()
    print("")
    garden1 = Garden("Bob")
    bush = Plant("Bush", 92, 393)
    garden1.plants += [bush]
    score1 = GardenManager.GardenStats.calculate_score(garden1.plants)
    score = GardenManager.GardenStats.calculate_score(garden0.plants)  # Llamar a classmethod()
    bool = GardenManager.GardenStats.validate_height(garden0.plants[1].height)
    print(f"Height validation test: {bool}")
    print(f"Garden scores - {garden0.owner}: {score},"
          f" {garden1.owner}: {score1}")
    network = GardenManager().create_garden_network([garden0, garden1])
    print(f"Total gardens managed: {network.total_gardens}")


if __name__ == "__main__":
    ft_garden_analytics()
