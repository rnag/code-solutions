from run_length_encoding import *


def test_encode():
    assert encode('') == ''
    assert encode('a') == '1a'
    assert encode('bb') == '2b'
    assert encode('bcc') == '1b2c'
    assert encode('aabcc') == '2a1b2c'
    assert encode('abcd') == '1a1b1c1d'
    assert encode('aaaabbccc') == '4a2b3c'
    assert encode('aaaabbccca') == '4a2b3c1a'
