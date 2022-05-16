from strings import *


def test_typed_out_strings():
    assert typed_out_strings("ab#c", "ad#c")
    assert typed_out_strings("ab##", "c#d#")
    assert typed_out_strings('cb#d', 'cd')
    assert typed_out_strings('cb###d', 'd')
    assert typed_out_strings('', '')
    assert typed_out_strings('x#y#z#', 'a#')
    assert not typed_out_strings('x#y#z#', 'a')
    assert not typed_out_strings('a#c', 'b')
    assert not typed_out_strings('abc#d', 'acc#c')
    assert not typed_out_strings('Ab#z', 'ab#z')
    assert not typed_out_strings('aaa###a', 'aaaa###a')
    assert typed_out_strings("bxj##tw", "bxo#j##tw")
    assert typed_out_strings('a###bcde###fgh##', 'bf')


def test_typed_out_strings_optimized():
    assert typed_out_strings_optimized("ab#c", "ad#c")
    assert typed_out_strings_optimized("ab##", "c#d#")
    assert typed_out_strings_optimized('cb#d', 'cd')
    assert typed_out_strings_optimized('cb###d', 'd')
    assert typed_out_strings_optimized('', '')
    assert typed_out_strings_optimized('x#y#z#', 'a#')
    assert not typed_out_strings_optimized('x#y#z#', 'a')
    assert not typed_out_strings_optimized('a#c', 'b')
    assert not typed_out_strings_optimized('abc#d', 'acc#c')
    assert not typed_out_strings_optimized('Ab#z', 'ab#z')
    assert not typed_out_strings_optimized('aaa###a', 'aaaa###a')
    assert typed_out_strings_optimized("bxj##tw", "bxo#j##tw")
    assert typed_out_strings_optimized('a###bcde###fgh##', 'bf')


def test_typed_out_strings_optimized_better_space():
    assert typed_out_strings_optimized_better_space("ab#c", "ad#c")
    assert typed_out_strings_optimized_better_space("ab##", "c#d#")
    assert typed_out_strings_optimized_better_space('cb#d', 'cd')
    assert typed_out_strings_optimized_better_space('cb###d', 'd')
    assert typed_out_strings_optimized_better_space('', '')
    assert typed_out_strings_optimized_better_space('x#y#z#', 'a#')
    assert not typed_out_strings_optimized_better_space('x#y#z#', 'a')
    assert not typed_out_strings_optimized_better_space('a#c', 'b')
    assert not typed_out_strings_optimized_better_space('abc#d', 'acc#c')
    assert not typed_out_strings_optimized_better_space('Ab#z', 'ab#z')
    assert not typed_out_strings_optimized_better_space('aaa###a', 'aaaa###a')
    assert typed_out_strings_optimized_better_space("bxj##tw", "bxo#j##tw")
    assert typed_out_strings_optimized_better_space('a###bcde###fgh##', 'bf')
