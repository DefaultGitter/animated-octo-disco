import pytest
from Unitest.Calc.prog import calc


def test_add():
    assert calc('5+2') == 7


def test_mult():
    assert calc('5*2') == 10


# def test_minus():
#     assert calc('5-2') == 3


def test_except():
    with pytest.raises(Exception) as error:
        calc('5/0')
    assert 'Do not destroy my universe' == error.value.args[0]


if __name__ == '__main__':
    pytest.main()
