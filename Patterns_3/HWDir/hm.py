# 2. Реалізуйте класи конкретних спостерігачів, наприклад, `DisplayCurrentConditions`,
# `DisplayStatistics` та `DisplayForecast`, які будуть реагувати на оновлення погодних даних.

# 3. Створіть клас `WeatherData`, який надаватиме дані про поточну погоду та
# повідомлятиме зареєстрованих спостерігачів про нові дані.

# 5. У методі `set_measurements` класу `WeatherData` оновлюйте значення температури,
# вологості та тиску. Потім повідомляйте всіх зареєстрованих спостерігачів,
# викликаючи їх методи update і передаючи їм нові дані.

# 6. Створіть екземпляри класів спостерігачів та об'єкт класу `WeatherData`.
# Зареєструйте спостерігачів в об'єкті `WeatherData` та змініть погодні дані.
# Переконайтеся, що спостерігачі отримують повідомлення та реагують на зміни.


class Observer:
    def update(self, t, w, p):
        pass


class DisplayCurrentConditions(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, t, w, p):
        print(f'{self.name} get message:\n'
              f'Temperature - {t[-2]}\n'
              f'Air humidity - {w[-2]}\n'
              f'Pressure - {p[-2]}\n')


class DisplayStatistics(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, t, w, p):
        print(f'{self.name} get message:\n'
              f'Temperature statistic - {t[:-1:]}\n'
              f'Air humidity statistic - {w[:-1:]}\n'
              f'Pressure statistic - {p[:-1:]}\n')


class DisplayForecast(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, t, w, p):
        print(f'{self.name} get message:\n'
              f'Temperature for tomorrow - {t[-1]}\n'
              f'Air humidity for tomorrow - {w[-1]}\n'
              f'Pressure for tomorrow - {p[-1]}\n')


class WeatherData:
    def __init__(self):
        self.observers = []
        self.t = [10, 20]
        self.w = [100, 200]
        self.p = [1000, 2000]

    def register_observer(self, obs):
        self.observers.append(obs)

    def remove_observer(self, obs):
        self.observers.remove(obs)

    def notify(self, t, w, p):
        for observer in self.observers:
            observer.update(t, w, p)

    def set_measurements(self, t, w, p):
        self.t.append(t)
        self.w.append(w)
        self.p.append(p)
        self.notify(self.t, self.w, self.p)


obs1 = DisplayCurrentConditions('obs1')
obs2 = DisplayStatistics('obs2')
obs3 = DisplayForecast('obs3')

weather = WeatherData()
weather.register_observer(obs1)
weather.register_observer(obs2)
weather.register_observer(obs3)

weather.set_measurements(30, 300, 3000)
weather.set_measurements(31, 301, 3001)
weather.set_measurements(32, 302, 3002)
