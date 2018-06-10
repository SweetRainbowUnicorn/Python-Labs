from enum import Enum


class AnimalType(Enum):
    CARNIVORE = 1
    HERBIVORE = 2


class Animal:
    type = None
    name = None
    family = None
    age = 0
    weight_of_food_per_day = 0

    def __str__(self):
        return str(self.name) + " " + self.type.name + " " + str(self.family) + " " + str(self.age) + " " \
               + str(self.weight_of_food_per_day) + " "
