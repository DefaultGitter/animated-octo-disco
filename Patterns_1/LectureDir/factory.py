from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def drive(self):
        pass


class Sedan(Car):
    def drive(self):
        return 'drive sedan'


class Bike(Car):
    def drive(self):
        return 'drive bike'


class Truck(Car):
    def drive(self):
        return 'drive truck'


class CarFactory:
    def create_car(self, car_type):
        if car_type == 'sedan':
            return Sedan()
        elif car_type == 'bike':
            return Bike()
        elif car_type == 'truck':
            return Truck()
        else:
            raise ValueError(f'Unknown car type: {car_type}')


factory = CarFactory()

car1 = factory.create_car('sedan')
car2 = factory.create_car('bike')
car3 = factory.create_car('truck')

list1 = [car1, car2, car3]

for car in list1:
    print(car.drive())
