import copy


class Sheep:
    def __init__(self, name, typ):
        self.name = name
        self.typ = typ

    def __str__(self):
        return f'Name - {self.name}; Type - {self.typ}'

    def clone(self):
        return copy.deepcopy(self)


original = Sheep('Dolly', 'Home')

clonedSheep = original.clone()
clonedSheep.name = 'Molly'

print(original)
print(clonedSheep)
