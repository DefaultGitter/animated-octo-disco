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


light_o = Light()

lightOn = LightOnCommand(light_o)
lightOff = LightOffCommand(light_o)

remoteControl = RemoteControl()
# remoteControl.set_command(lightOn)
remoteControl.set_command(lightOff)

remoteControl.press_button()
