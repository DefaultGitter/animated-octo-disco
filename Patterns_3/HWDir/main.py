# 3. Створіть клас `WeatherData`, який надаватиме дані про поточну погоду та
# повідомлятиме зареєстрованих спостерігачів про нові дані.

# 4. Реалізуйте методи `register_observer` та `remove_observer` у класі `WeatherData`,
# щоб спостерігачі могли підписуватися та відписуватися від оновлень.

# 5. У методі `set_measurements` класу `WeatherData` оновлюйте значення температури, вологості та тиску.
# Потім повідомляйте всіх зареєстрованих спостерігачів, викликаючи їх методи update і передаючи їм нові дані.

# 6. Створіть екземпляри класів спостерігачів та об'єкт класу `WeatherData`. Зареєструйте спостерігачів в об'єкті
# `WeatherData` та змініть погодні дані. Переконайтеся, що спостерігачі отримують повідомлення та реагують на зміни.

from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, te, hu, pa):
        pass


class WeatherData(Observer):
    def __init__(self):
        self.te = None
        self.hu = None
        self.pa = None
        self.observer = []
        # self.name = name
        # self.weather_data = DisplayCurrentConditions()

    def update(self, te, hu, pa):
        pass

    # print(f'{self.name} recieved a message: {self.weather_data.cur_cond(te, hu, pa)}')

    def register_observer(self, observer):
        self.observer.append(observer)

    def remove_observer(self, observer):
        self.observer.remove(observer)

    def notify_observers(self, te, hu, pa):
        for observer in self.observer:
            observer.update(te, hu, pa)

    def set_measurements(self, te, hu, pa):
        self.te = te
        self.hu = hu
        self.pa = pa
        self.notify_observers(self.te, self.hu, self.pa)


class DisplayCurrentConditions(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, te, hu, pa):
        print(f'{self.name} recieved message: temperature = {te}, humidity = {hu}, pressure = {pa}')


class DisplayStatistics:
    pass


class DisplayForecast:
    pass


