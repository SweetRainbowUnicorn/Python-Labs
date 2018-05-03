class Flower:
    pass


class Flower:
    totalAmount = 0

    def __init__(self, name="flower", color="white", high=0.5, amount=0, petals=6):
        self.name = name
        self.amount = amount
        self.color = color
        self.high = high
        self.petals = petals

        Flower.totalAmount += amount

    def to_string(self):
        print("Name: " + self.name + "; Color: " + self.color +
              "; High: ", self.high, "; Amount: ", self.amount, "; Petals: ", self.petals)

    def print_sum(self):
        print("Amount of " + self.name + ": ", self.amount)

    @staticmethod
    def print_total_amount():
        print("Total amount: ", Flower.totalAmount)


if __name__ == '__main__':
    chamomile = Flower()
    geranium = Flower("Geranium", "Purple", 0.45, 13)
    pansy = Flower("Pansy", "Pink", 0.3, 12, 18)

    chamomile.to_string()
    geranium.to_string()
    pansy.to_string()

    chamomile.print_sum()
    geranium.print_sum()
    pansy.print_sum()

    Flower.print_total_amount()
