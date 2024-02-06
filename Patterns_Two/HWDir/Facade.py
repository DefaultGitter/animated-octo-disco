# Розробити програму для керування домашньою системою "Розумний дім",
# яка включає управління освітленням, температурою та безпекою.

# Система повинна надавати інтерфейс для увімкнення/вимкнення світла,
# встановлення температури та активації сигналізації.

# В даному випадку, патерн фасад може бути використаний для створення зручного інтерфейсу,
# що приховує складність взаємодії з різними компонентами "Розумного дому".

# Виконаною роботою вважається правильно складена структура програми (зв'язку об'єктів та його методів).
# Методи можуть бути порожніми (не містити функціональний код)


class RoomStatus:
    def status(self, light, signaling, thermostat):
        print(f'Light - {light}\n'
              f'Signaling - {signaling}\n'
              f'Temperature - {thermostat}\n')


class SmartHouse:
    def __init__(self, light='Off', signaling='Off', thermostat=24):
        self.__room_status = RoomStatus()
        self.__signaling = signaling
        self.__thermostat = thermostat
        self.__light = light

    def light(self, light=None):
        if light:
            self.__light = light
            return
        if self.__light == 'On':
            self.__light = 'Off'
            return 'switched off'
        else:
            self.__light = 'On'
            return 'switched on'

    def signaling(self, signaling=None):
        if signaling:
            self.__signaling = signaling
            return
        if self.__signaling == 'On':
            self.__signaling = 'Off'
            return 'switched off'
        else:
            self.__signaling = 'On'
            return 'switched on'

    def thermostat(self, thermostat):
        self.__thermostat = thermostat

    def status(self):
        self.__room_status.status(self.__light, self.__signaling, self.__thermostat)


room_list = {'Kitchen': SmartHouse(), 'Bedroom': SmartHouse(), 'Bathroom': SmartHouse(), 'Hall': SmartHouse(),
             'Garage': SmartHouse()}


def smart_house():
    global room_list
    for room in room_list.keys():
        print(room, end=' ')
    room = input(f'\nEnter a room: ').title()
    # room = 'Kitchen'
    if room == 'Exit':
        return False
    if room == 'All':
        light = input(f'Light On/Off: ').title()
        signaling = input(f'Signaling On/Off: ').title()
        thermostat = int(input(f'Enter a temperature: '))
        for room in room_list.keys():
            room_list[room].light(light)
            room_list[room].signaling(signaling)
            room_list[room].thermostat(thermostat)

        for room in room_list.keys():
            print(f'{room:_^20}')
            room_list[room].status()

    else:
        room_list[room].status()
        choice = input(f'light/thermo/sign: ').lower()
        if 'light' in choice:
            change = room_list[room].light()
            print(f'{choice} is {change}')
        if 'thermo' in choice:
            room_list[room].thermostat(int(input('Enter new temperature for thermostat: ')))
        if 'signaling' in choice:
            change = room_list[room].signaling()
            print(f'{choice} is {change}')


while smart_house():
    smart_house()
