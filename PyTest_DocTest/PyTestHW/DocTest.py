# Завдання 2
# Напишіть функцію, яка приймає рядок та повертає її у зворотному порядку. Застосуйте інструкції та doctest.
import doctest


def reverse(line: str):
    """
    reverser

    :param line: str
    :return: reversed line
    :raise TypeError: if line is not a string:
    >>> reverse(10)
    Traceback (most recent call last):
    TypeError: I can reverse only STR type
    """
    if not isinstance(line, str):
        raise TypeError('I can reverse only STR type')
    return line[::-1]


if __name__ == '__main__':
    doctest.testmod()
