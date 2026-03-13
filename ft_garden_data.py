class Plant:
    def __init__(self, name : str, height : int, age : int):
        self.name = name  # Atributo de instancia
        self.height = height  # Atributo de instancia
        self.age = age
        
    def plant_info(self):
     print(f"{(self.name).capitalize()} : {self.height}cm, {self.age} days old") 

def ft_garden_data():
  
  print("=== Garden Plant Registry ===")
  garden = [
    Plant("rose", 25, 30),
  	Plant("Sunflower", 80, 45),
    Plant("cactus", 15, 120)
] 
  for i in range(0,3):
      
    garden[i].plant_info()


if __name__ == "__main__": 
	ft_garden_data()