class MetricSystem:
    def get_distance(self):
        pass


class Meters(MetricSystem):
    def get_distance(self):
        return 100


class ImperialSystem:
    def get_distance_in_feet(self):
        pass


class Feet(ImperialSystem):
    def get_distance_in_feet(self):
        return 3280.84


class ImperialToMetricSystem(ImperialSystem):
    def __init__(self, imperial_system):
        self.imperial_system = imperial_system

    def get_distance(self):
        feet = self.imperial_system.get_distance_in_feet()
        return feet * 0.3048


def t_system(system):
    print(f'Distance: {system.get_distance()} meters')


feet_system = Feet()
# meter_system = Meters()
adapter = ImperialToMetricSystem(feet_system)
t_system(adapter)
