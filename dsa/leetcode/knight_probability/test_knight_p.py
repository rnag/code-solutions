from knight_p import *


def test_knight_probability():
    assert knight_probability(n=1, k=0, r=0, c=0) == 1
    assert knight_probability(n=3, k=2, r=0, c=0) == 0.06250
    assert knight_probability(n=6, k=3, r=2, c=2) == 0.359375


def test_knight_probability_naive():
    assert knight_probability_naive(n=1, k=0, r=0, c=0) == 1
    assert knight_probability_naive(n=3, k=2, r=0, c=0) == 0.06250
    assert knight_probability_naive(n=6, k=3, r=2, c=2) == 0.359375

