class SecurePlant:
    def __init__(self, name: str, height: int, age: int):
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.height = height
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.age = age
        self.name = name

    def set_height(self, height: int) -> None:
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.height = height
            print(f"Height updated: {height}cm [OK]")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.age = age
            print(f"Age updated: {age} days [OK]")

    def get_height(self) -> int:
        return self.height

    def get_age(self) -> int:
        return self.age

    def get_name(self) -> str:
        return self.name


def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    plant1 = SecurePlant("Rose", 0, 0)
    print(f"Plant created: {plant1.name}")
    plant1.set_height(25)
    plant1.set_age(30)
    print("")
    plant1.set_height(-5)
    print("")
    print(
        f"Current plant: {plant1.name} ({plant1.get_height()}cm,"
        f" {plant1.get_age()} days)"
        )


if __name__ == "__main__":
    ft_garden_security()
