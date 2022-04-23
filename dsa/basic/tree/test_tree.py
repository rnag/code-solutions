from tree import *


def test_node():
    n = Node('a')
    assert n.val == 'a'
    assert len(n.children) == 0


def test_node_can_add_children():
    n = Node('a')
    n.add('b')
    assert len(n.children) == 1
    assert n.children[0].children == []


def test_node_can_remove_children():
    n = Node('a')
    n.add('b')
    assert len(n.children) == 1
    n.remove('b')
    assert len(n.children) == 0


def test_tree_starts_empty():
    t = Tree()
    assert t.root is None


def test_can_traverse_bf():
    t = Tree()
    t.root = Node('a')
    t.root.add('b')
    t.root.add('c')
    t.root.children[0].add('d')

    letters = t.traverse_bf()

    assert letters == ['a', 'b', 'c', 'd']


def test_can_traverse_df():
    t = Tree()
    t.root = Node('a')
    t.root.add('b')
    t.root.add('d')
    t.root.children[0].add('c')

    letters = t.traverse_df()

    assert letters == ['a', 'b', 'c', 'd']
