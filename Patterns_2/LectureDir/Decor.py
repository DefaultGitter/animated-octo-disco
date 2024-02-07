from abc import ABC, abstractmethod

class TextFormat(ABC):
    @abstractmethod
    def format(self, text):
        pass


class PlainText(TextFormat):
    def format(self, text):
        return text


class BoldText(TextFormat):
    def __init__(self, formater):
        self.formater = formater

    def format(self, text):
        return f"<b>{self.formater.format(text)}</b>"


class ItalicText(TextFormat):
    def __init__(self, formater):
        self.formater = formater

    def format(self, text):
        return f"<i>{self.formater.format(text)}</i>"


def test_text_format(text_format):
    formated_text = text_format.format("Hello world")
    print(f'Formated text -> {formated_text}')


plain_text = PlainText()
test_text_format(plain_text)
bold_text = BoldText(plain_text)
test_text_format(bold_text)
italic_text = ItalicText(bold_text)
test_text_format(italic_text)
test_text_format(bold_text)

# 1:19
