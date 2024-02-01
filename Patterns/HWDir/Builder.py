from random import randint


class Dice:
    def __init__(self, health):
        self.health = health
        self.D4 = False

    def __str__(self):
        return f'{self.health}'


class DnD:
    def __init__(self, hp):
        self.roll = Dice(hp)
        self.damage = 0
        self.critical = 0

    def d6(self):
        self.damage = randint(0, 6)
        self.roll.health -= self.damage
        return self

    def d4(self):
        self.critical = randint(0, 4)
        if self.critical == 0:
            print(f'Critical miss!'
                  f'Your attack cured your enemy...')
            return self.heal()
        elif self.critical == 4:
            print(f'Critical hint!')
            return self.d20()
        else:
            self.d6()

    def d20(self):
        self.damage = randint(7, 20)
        self.roll.health -= self.damage
        return self

    def heal(self):
        self.d6()
        self.damage *= -1
        self.roll.health -= self.damage*2
        return self

    def build(self):
        return self.roll.health

    def __str__(self):
        return f'Damage: {self.damage}'


print(f'You are a Warrior with some magic dices in a dungeon.\n'
      f'You found a troll which has to be killed.\n'
      f'Fight has started!\n')
warrior = DnD(50)
troll = DnD(100)
print(f'Warrior: {warrior.build()}\nTroll: {troll.build()}')
while (warrior.build() > 0) and (troll.build() > 0):
    print(f'\nYou turn to attack')
    # troll.d6()
    troll.d4()
    print(troll)

    print(f'\nTroll`s turn')
    warrior.d6()
    print(warrior)

    input(f'\nWarrior: {warrior.build()}\nTroll: {troll.build()}')
else:
    if warrior.build() < 0:
        print('You lose!')
    else:
        print('You won!')
