import copy


class Knife:
    def __init__(self, steel, typ):
        self.steel = steel
        self.typ = typ

    def __str__(self):
        return f'Steel - {self.steel}; Type - {self.typ}'

    def clone(self):
        return copy.deepcopy(self)


original = Knife('Damascus', 'puukko')

clonedKnife = original.clone()
clonedKnife.steel = 'silver'
clonedKnife.typ = 'butter knife'

print(original)
print(clonedKnife)
