class Pizza:
    def __init__(self):
        self.size = None
        self.cheese = False
        self.beacon = False
        self.pepper = False
        self.souse = False

    def __str__(self):
        return (f"Pizza - Size: {self.size}, Cheese: {self.cheese}, Beacon: {self.beacon}, "
                f"Pepper: {self.pepper}, Souse: {self.souse}")


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
        self.pizza.size = size
        return self

    def set_cheese(self):
        self.pizza.cheese = True
        return self

    def set_beacon(self):
        self.pizza.beacon = True
        return self

    def set_pepper(self):
        self.pizza.pepper = True
        return self

    def set_souse(self):
        self.pizza.souse = True
        return self

    def build(self):
        return self.pizza


builder = PizzaBuilder()
pizza1 = builder.set_size('Small').set_cheese().set_beacon().set_pepper().build()

print(pizza1)
