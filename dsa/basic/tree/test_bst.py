from bst import *


def test_node_inserts_correctly():
    node = Node(10)
    node.insert(5)
    node.insert(15)
    node.insert(17)

    assert node.left.val == 5
    assert node.right.val == 15
    assert node.right.right.val == 17


def test_contains_returns_node_with_same_value():
    node = Node(10)
    node.insert(5)
    node.insert(15)
    node.insert(20)
    node.insert(0)
    node.insert(-5)
    node.insert(3)

    three = node.left.left.right
    assert node.contains(3) == three


def test_contains_returns_none_if_value_not_found():
    node = Node(10)
    node.insert(5)
    node.insert(15)
    node.insert(20)
    node.insert(0)
    node.insert(-5)
    node.insert(3)

    assert node.contains(9999) is None
