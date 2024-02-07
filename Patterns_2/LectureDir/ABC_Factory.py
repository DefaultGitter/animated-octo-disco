from abc import ABC, abstractmethod


class Chair(ABC):
    @abstractmethod
    def sit_on(self):
        pass


class Table(ABC):
    @abstractmethod
    def put_on(self):
        pass


class ModernChair(Chair):
    def sit_on(self):
        print('I`m a modern chair')


class VictorianChair(Chair):
    def sit_on(self):
        print('I`m a victorian chair')


class ModernTable(Table):
    def put_on(self):
        print('I`m a modern table')


class VictorianTable(Table):
    def put_on(self):
        print('I`m a victorian table')


class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_table(self) -> Table:
        pass


class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ModernChair()

    def create_table(self) -> Table:
        return ModernTable()


class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return VictorianChair()

    def create_table(self) -> Table:
        return VictorianTable()


victorian_factory = VictorianFurnitureFactory()
victorian_chair = victorian_factory.create_chair()
victorian_table = victorian_factory.create_table()

victorian_chair.sit_on()
victorian_table.put_on()
