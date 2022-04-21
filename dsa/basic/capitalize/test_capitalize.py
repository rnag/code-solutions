from basic.capitalize.capitalize import capitalize, capitalize_idiomatic, capitalize_alt


def test_compare_times():
    from timeit import timeit
    n = 100_000

    print('capitalize_idiomatic: ', timeit("capitalize_idiomatic('hi there, how is it going?')", globals=globals(), number=n))
    print('capitalize:           ', timeit("capitalize('hi there, how is it going?')", globals=globals(), number=n))
    print('capitalize_alt:       ', timeit("capitalize_alt('hi there, how is it going?')", globals=globals(), number=n))


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


def test_capitalize_alt():
    assert capitalize_alt('a short sentence') == 'A Short Sentence'
    assert capitalize_alt('a lazy fox') == 'A Lazy Fox'
    assert capitalize_alt('look, it is working!') == 'Look, It Is Working!'
    assert capitalize_alt('hi there, how is it going?') == 'Hi There, How Is It Going?'
    assert capitalize_alt('i love breakfast at bill miller bbq') == 'I Love Breakfast At Bill Miller Bbq'
