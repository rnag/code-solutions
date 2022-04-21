from basic.anagrams.anagrams import anagrams, anagrams_optimized


def test_anagrams_optimized():
    assert anagrams_optimized('', '')
    assert anagrams_optimized('rail safety', 'fairy tales')
    assert anagrams_optimized('RAIL! SAFETY!', 'fairy tales')
    assert anagrams_optimized('123!@#$%', '  ')
    assert not anagrams_optimized('Hi there', 'Bye there')


def test_anagrams():
    assert anagrams('', '')
    assert anagrams('rail safety', 'fairy tales')
    assert anagrams('RAIL! SAFETY!', 'fairy tales')
    assert anagrams('123!@#$%', '  ')
    assert not anagrams('Hi there', 'Bye there')
