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


def ft_garden_data():
    print("=== Garden Plant Registry ===")
    garden = [
      Plant("rose", 25, 30),
      Plant("Sunflower", 80, 45),
      Plant("cactus", 15, 120)
    ]
    for i in range(0, 3):
        garden[i].get_info()


if __name__ == "__main__":
    ft_garden_data()
