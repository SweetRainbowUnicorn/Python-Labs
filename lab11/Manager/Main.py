from Animals.Carnivore import Carnivore
from Animals.Herbivore import *
from Manager.Savanna import *
from Animals.Vulture import *
from Animals.Animal import *

if __name__ == '__main__':
    savanna = Savanna()

    lion = Carnivore("lion", "cats", 16, 7)
    zebra = Herbivore("zebra", "horses", 12, 6)
    tiger = Carnivore("tiger", "cats", 5, 7)
    elephant = Herbivore("elephant", "mammal", 19, 8)
    griffon = Vulture("griffon", "bird", 6, 58)

    savanna.animals = [lion, zebra, tiger, elephant, griffon]
    print("List")
    savanna.print_list(savanna.animals)
    savanna.animals = savanna.find_by_type(AnimalType.CARNIVORE)
    print("Found")
    savanna.print_list(savanna.animals)
    savanna.animals = savanna.sort_by_name()
    print("Sorted")
    savanna.print_list(savanna.animals)
