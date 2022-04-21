from basic.anagrams.anagrams import anagrams, anagrams_optimized


def test_compare_times():
    from timeit import timeit
    n = 100_000

    print('anagrams_optimized: ', timeit("anagrams_optimized('rail safety', 'fairy tales')", globals=globals(), number=n))
    print('anagrams:           ', timeit("anagrams('rail safety', 'fairy tales')", globals=globals(), number=n))


def test_anagrams_optimized():
    assert anagrams_optimized('', '')
    assert anagrams_optimized('rail safety', 'fairy tales')
    assert anagrams_optimized('RAIL! SAFETY!', 'fairy tales')
    assert anagrams_optimized('123!@#$%', '  ')
    assert not anagrams_optimized('Hi there', 'Bye there')

    assert anagrams_optimized('hello', 'llohe')
    assert anagrams_optimized('Whoa! Hi!', 'Hi! Whoa!')
    assert not anagrams_optimized('One One', 'Two two two')
    assert not anagrams_optimized('One one', 'One one c')
    assert not anagrams_optimized('A tree, a life, a bench', 'A tree, a fence, a yard')


def test_anagrams():
    assert anagrams('', '')
    assert anagrams('rail safety', 'fairy tales')
    assert anagrams('RAIL! SAFETY!', 'fairy tales')
    assert anagrams('123!@#$%', '  ')
    assert not anagrams('Hi there', 'Bye there')

    assert anagrams('hello', 'llohe')
    assert anagrams('Whoa! Hi!', 'Hi! Whoa!')
    assert not anagrams('One One', 'Two two two')
    assert not anagrams('One one', 'One one c')
    assert not anagrams('A tree, a life, a bench', 'A tree, a fence, a yard')
