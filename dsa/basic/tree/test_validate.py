from validate import *


def test_validate_recognizes_a_valid_bst():
    n = Node(10)
    n.insert(5)
    n.insert(15)
    n.insert(0)
    n.insert(20)

    assert validate(n)


def test_validate_recognizes_an_invalid_bst():
    n = Node(10)
    n.insert(5)
    n.insert(15)
    n.insert(0)
    n.insert(20)
    n.left.left.right = Node(999)

    assert not validate(n)
