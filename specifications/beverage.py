class Beverage:
    drink_types = ["vodka", "coffee", "coke"]

    def __init__(self, name, drink_type):
        self.name = name
        if drink_type in drink_types:
            self.drink_type = drink_type
        else:
            self.drink_type = "vodka"
