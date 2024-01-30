# Завдання 1
# Створіть клас роботи з дробами. У класі має бути реалізована наступна функціональність:
#     • Додавання дробів;
#     • Віднімання дробів;
#     • І т.д
# Протестуйте всі можливості створеного класу за допомогою модульного тестування pytest.


class FractionCalc:
    def __init__(self, x=None, y=None):
        self.x = x
        if y == 0:
            raise ZeroDivisionError('Stop destroying this Universe by ZERO DIVISION!!!')
        if y is None:
            raise ValueError('This class works only with fractions. Please, enter "y" next time')
        self.y = y

    def __add__(self, other):
        tmp = FractionCalc(0, 1)
        sx, ox, sy, oy = self.x, other.x, self.y, other.y
        if sy != oy:
            sx, ox, sy = FractionCalc.common_denominator(sx, ox, sy, oy)
        tmp.x = sx + ox
        tmp.y = sy
        return tmp

    def __sub__(self, other):
        tmp = FractionCalc(0, 1)
        sx, ox, sy, oy = self.x, other.x, self.y, other.y
        if sy != oy:
            sx, ox, sy = FractionCalc.common_denominator(sx, ox, sy, oy)
        tmp.x = sx - ox
        tmp.y = sy
        return tmp

    def __mul__(self, other):
        tmp = FractionCalc(0, 1)
        if 0 in [self.x, other.x]:
            return tmp
        sx, ox, sy, oy = self.x, other.x, self.y, other.y
        tmp.x = sx * ox
        tmp.y = sy * oy
        return tmp

    def __truediv__(self, other):
        if 0 == other.x:
            raise ZeroDivisionError('ERROR, zero division detected! You shall not pass!!!')
        tmp = FractionCalc(0, 1)
        sx, ox, sy, oy = self.x, other.x, self.y, other.y
        tmp.x = sx * oy
        tmp.y = sy * ox
        return tmp

    def __str__(self):
        if self.x == 0:
            return '0'
        return f'{self.x} / {self.y}'

    @classmethod
    def common_denominator(cls, x1, x2, y1, y2):
        x1 *= y2
        x2 *= y1
        y1 *= y2
        return x1, x2, y1


if __name__ == '__main__':
    f1 = FractionCalc(1, 4)
    f2 = FractionCalc(0, 5)
    f3 = f1 / f2
    print(f1)
    print(f3)
