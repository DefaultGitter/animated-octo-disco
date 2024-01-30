import pytest
from mainProgram import FractionCalc

tf1 = FractionCalc(1, 4)
tf2 = FractionCalc(1, 5)


def test_add():
    tf_res = tf1 + tf2
    assert [tf_res.x, tf_res.y] == [9, 20]


def test_subtract():
    tf_res = tf1 - tf2
    assert [tf_res.x, tf_res.y] == [1, 20]


def test_multiply():
    tf_res = tf1 * tf2
    assert [tf_res.x, tf_res.y] == [1, 20]


def test_divide():
    tf_res = tf1 / tf2
    assert [tf_res.x, tf_res.y] == [5, 4]


def test_zero_div():
    with pytest.raises(Exception) as error:
        tf1 / FractionCalc(0, 5)
    assert 'ERROR, zero division detected! You shall not pass!!!' == error.value.args[0]


def test_zero_init():
    with pytest.raises(Exception) as error:
        FractionCalc(1, 0)
    assert 'Stop destroying this Universe by ZERO DIVISION!!!' == error.value.args[0]


def test_no_denominator():
    with pytest.raises(Exception) as error:
        FractionCalc(1, )
    assert 'This class works only with fractions. Please, enter "y" next time' == error.value.args[0]


if __name__ == '__main__':
    pytest.main()
