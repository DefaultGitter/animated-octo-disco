# Створіть програму для приготування пасти. Програма повинна вміти створювати щонайменше три види пасти.
# Класи різної пасти повинні мати такі методи:
# •	Тип пасти;
# •	Соус;
# •	Начинка;
# •	Добавки.
# Для реалізації використовуйте патерни, що породжують.
from abc import ABC, abstractmethod


class Pasta(ABC):
    @abstractmethod
    def cook(self):
        pass


class PastaParts:
    def __init__(self):
        self.p_type = None
        self.p_souse = 'Standart'
        self.p_filling = 'Standart'
        self.p_supplements = 'Standart'

    def __str__(self):
        return (f'Pasta type - {self.p_type}, souse - {self.p_souse}, '
                f'filling - {self.p_filling}, supplements - {self.p_supplements}')


class PastaBuilder:
    def __init__(self):
        self.pasta = PastaParts()

    def set_p_type(self, p_type):
        self.pasta.p_type = p_type
        return self

    def set_p_souse(self, p_souse):
        self.pasta.p_souse = p_souse
        return self

    def set_p_filling(self, p_filling):
        self.pasta.p_filling = p_filling
        return self

    def set_p_supplements(self, p_supplements):
        self.pasta.p_supplements = p_supplements
        return self

    def build(self):
        return self.pasta


class Asciutta(Pasta):
    def cook(self):
        return 'cook Asciutta'


class Fresco(Pasta):
    def cook(self):
        return 'cook Fresco'


class Piena(Pasta):
    def cook(self):
        # return 'cook Piena'
        return builder


class PastaFactory:
    def make_a_pasta(self, pasta_type):
        if pasta_type == 'Asciutta':
            return Asciutta()
        elif pasta_type == 'Fresco':
            return Fresco()
        elif pasta_type == 'Piena':
            return Piena()
        else:
            raise ValueError(f'Unknown pasts type: {pasta_type}')


pasta = 'Piena'
factory = PastaFactory()
builder = PastaBuilder()

pasta1 = factory.make_a_pasta(pasta)
print(pasta1.cook().set_p_type(pasta).set_p_souse('Tomate').set_p_supplements('beacon').build())
