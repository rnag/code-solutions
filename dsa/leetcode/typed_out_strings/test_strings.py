from strings import *


def test_trapping_rainwater():
    # zeros
    assert trapping_rainwater([]) == 0
    assert trapping_rainwater([7]) == 0
    assert trapping_rainwater([7, 3]) == 0
    assert trapping_rainwater([3, 4, 3]) == 0

    assert trapping_rainwater([4, 2, 0, 3, 2, 5]) == 9
    assert trapping_rainwater(
        [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]) == 8
    assert trapping_rainwater(
        [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6


def test_trapping_rainwater_optimized():
    assert typed_out_strings_optimized("ab#c", "ad#c")
    assert typed_out_strings_optimized("ab##", "c#d#")
    assert typed_out_strings_optimized('cb#d', 'cd')
    assert typed_out_strings_optimized('cb###d', 'd')
    assert typed_out_strings_optimized('', '')
    assert typed_out_strings_optimized('x#y#z#', 'a#')
    assert not typed_out_strings_optimized('x#y#z#', 'a')
    assert not typed_out_strings_optimized('a#c', 'b')
    assert typed_out_strings_optimized("bxj##tw", "bxo#j##tw")
    assert typed_out_strings_optimized('a###bcde###fgh##', 'bf')
