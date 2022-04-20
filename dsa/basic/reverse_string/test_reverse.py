from basic.reverse_string.reverse import reverse, reverse_idiomatic


def test_reverse():
    assert reverse('apple') == 'elppa'
    assert reverse('hello') == 'olleh'
    assert reverse('Greetings!') == '!sgniteerG'


def test_reverse_idiomatic():
    assert reverse_idiomatic('apple') == 'elppa'
    assert reverse_idiomatic('hello') == 'olleh'
    assert reverse_idiomatic('Greetings!') == '!sgniteerG'
