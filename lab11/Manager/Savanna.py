
class Savanna:
    animals = []

    def __init__(self):
        pass

    def sort_by_name(self):
        self.animals.sort(key=lambda animal: animal.name, reverse=True)
        return self.animals

    def find_by_type(self, animal_type):
        result = []
        for animal in self.animals:
            if animal.type == animal_type and animal.weight_of_food_per_day > 5:
                result.append(animal)

        return result

    @staticmethod
    def print_list(printed_list):
        for animal in printed_list:
            print(animal)
        print("\n")
