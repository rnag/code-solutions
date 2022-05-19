from coin_change import *


def test_coin_change():
    assert coin_change([1, 3, 4, 5], 7) == 2
    assert coin_change([1, 2, 5], 11) == 3
    assert coin_change([2], 3) == -1

