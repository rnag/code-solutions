from basic.capitalize.capitalize import capitalize, capitalize_idiomatic


def test_capitalize_idiomatic():
    assert capitalize_idiomatic('a short sentence') == 'A Short Sentence'
    assert capitalize_idiomatic('a lazy fox') == 'A Lazy Fox'
    assert capitalize_idiomatic('look, it is working!') == 'Look, It Is Working!'
    assert capitalize_idiomatic('hi there, how is it going?') == 'Hi There, How Is It Going?'
    assert capitalize_idiomatic('i love breakfast at bill miller bbq') == 'I Love Breakfast At Bill Miller Bbq'


def test_capitalize():
    assert capitalize('a short sentence') == 'A Short Sentence'
    assert capitalize('a lazy fox') == 'A Lazy Fox'
    assert capitalize('look, it is working!') == 'Look, It Is Working!'
    assert capitalize('hi there, how is it going?') == 'Hi There, How Is It Going?'
    assert capitalize('i love breakfast at bill miller bbq') == 'I Love Breakfast At Bill Miller Bbq'
