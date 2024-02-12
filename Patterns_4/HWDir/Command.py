from abc import ABC, abstractmethod


class TextDocument:
    def __init__(self):
        self.text = ''
        self.text_prev = ''

    def add_text(self, text):
        self.text_prev = self.text
        self.text += str(text)

    def remove_text(self, text):
        if text in self.text:
            self.text_prev = self.text
            self.text = self.text.replace(text, '')
        else:
            raise ValueError(f'Can`t find {text} in {self.text}')

    def get_text(self, undo_c=False):
        if undo_c:
            self.text = self.text_prev
            return
        print(self.text)


class Command(ABC):
    @abstractmethod
    def execute(self, data):
        pass

    def undo(self):
        pass


class AddTextCommand(Command):
    def __init__(self, text):
        self.text = text
        self.text_prev = None

    def execute(self, data):
        self.text_prev = self.text
        self.text.add_text(data)

    def undo(self):
        self.text.get_text(True)


class RemoveTextCommand(Command):
    def __init__(self, text):
        self.text = text
        self.old_data = None

    def execute(self, data):
        self.old_data = self.text
        self.text.remove_text(data)

    def undo(self):
        self.text.get_text(True)


class TextEditor:
    def __init__(self):
        self.command = None

    def execute_command(self, command, data):
        self.command = command
        self.command.execute(data)

    def undo_last_command(self):
        self.command.undo()


data_base = TextDocument()
add_to_text = AddTextCommand(data_base)
remove_from_text = RemoveTextCommand(data_base)

text_editor = TextEditor()

text_editor.execute_command(add_to_text, 'test message')
data_base.get_text()

text_editor.execute_command(remove_from_text, 'me')
data_base.get_text()

text_editor.undo_last_command()
data_base.get_text()

text_editor.execute_command(add_to_text, ' mememememe')
data_base.get_text()

text_editor.undo_last_command()
data_base.get_text()
