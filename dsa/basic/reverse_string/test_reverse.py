from basic.reverse_string.reverse import reverse_idiomatic, reverse, reverse_v2


def test_reverse_idiomatic():
    assert reverse_idiomatic('apple') == 'elppa'
    assert reverse_idiomatic('hello') == 'olleh'
    assert reverse_idiomatic('Greetings!') == '!sgniteerG'


def test_reverse():
    assert reverse('apple') == 'elppa'
    assert reverse('hello') == 'olleh'
    assert reverse('Greetings!') == '!sgniteerG'


def test_reverse_v2():
    assert reverse_v2('apple') == 'elppa'
    assert reverse_v2('hello') == 'olleh'
    assert reverse_v2('Greetings!') == '!sgniteerG'
