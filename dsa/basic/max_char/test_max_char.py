from basic.max_char.max_char import max_char


def test_max_char():
    assert max_char("abcccccccd") == "c"
    assert max_char('') is None
    assert max_char('h') == 'h'
    assert max_char('hi') == 'h'
    assert max_char('hello') == 'l'
    assert max_char('hi there person!') == 'e'
    assert max_char("apple 1231111") == "1"
