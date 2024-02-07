# from abc import ABC, abstractmethod

class Observer:
    # @abstractmethod
    def update(self, message):
        pass


class ConcreteObserver(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f'{self.name} recieved message: {message}')


class Subject:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)


class ConcreteSubject(Subject):
    def set_state(self, state):
        self.state = state
        self.notify(f'State changed to {self.state}')


observer1 = ConcreteObserver('Observer1')
observer2 = ConcreteObserver('Observer2')

subject = ConcreteSubject()
subject.add_observer(observer1)
subject.add_observer(observer2)

subject.set_state('state1')
