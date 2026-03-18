"""
ft_garden_security.py

This file introduces the idea of data protection through a SecurePlant
class. Instead of allowing direct modification of its attributes, the
class provides controlled setter methods that validate incoming values.
Negative heights or ages are rejected, and the class prints clear
messages indicating whether an update was accepted or blocked.

The script demonstrates how a SecurePlant object can be created,
updated safely, and protected from invalid operations. This exercise
highlights the concept of encapsulation: keeping important data
private and ensuring that all modifications go through controlled,
validated methods.
"""


class SecurePlant:
    def __init__(self, name: str):
        self.height = 0
        self.age = 0
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
    plant1 = SecurePlant("Rose")
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
