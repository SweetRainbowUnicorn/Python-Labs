from Animals.Animal import *


class Carnivore(Animal):
    type = AnimalType.CARNIVORE

    def __init__(self, name="animal", family="family", age=0, weight_of_food_per_day=0):
        self.name = name
        self.family = family
        self.age = age
        self.weight_of_food_per_day = weight_of_food_per_day
