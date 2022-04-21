from basic.pyramid.pyramid import pyramid, pyramid_idiomatic


def test_steps_idiomatic_with_1():
    pyramid_idiomatic(1)


def test_steps_idiomatic_with_2():
    pyramid_idiomatic(2)


def test_steps_idiomatic_with_3():
    pyramid_idiomatic(3)


def test_steps_idiomatic_with_5():
    pyramid_idiomatic(5)


def test_steps_with_1():
    pyramid(1)


def test_steps_with_2():
    pyramid(2)


def test_steps_with_3():
    pyramid(3)


def test_steps_with_5():
    pyramid(5)
