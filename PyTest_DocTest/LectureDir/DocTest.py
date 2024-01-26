import doctest


def div(x: float, y: float) -> float:
    """
    func for division
    :param x: float number
    :param y: != 0
    :return: float x/ float y
    :raise ZeroDivisionError: if y is 0
    >>> div(5,2)
    2.5
    >>> div(5,0)
    Traceback (most recent call last):
    ZeroDivisionError: division by zero
    """
    if y == 0:
        raise ZeroDivisionError('division by zero')
    return x / y


if __name__ == '__main__':
    doctest.testmod()
