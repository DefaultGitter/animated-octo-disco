# commander 1:20
class Light:
    def turn_off(self):
        print('Light turned off')

    def turn_on(self):
        print('Light turned on')


class Command:
    def execute(self):
        pass


class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()


class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()


class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()


light = Light()
lightOn = LightOnCommand(light)
lightOff = LightOffCommand(light)

remoteControl = RemoteControl()
