from level_width import *


def test_level_width_1():
    root = Node(0)
    root.add(1)
    root.add(2)
    root.add(3)
    root.children[0].add(4)
    root.children[2].add(5)

    assert level_width_idiomatic(root) == [1, 3, 2]


def test_level_width_2():
    root = Node(0)
    root.add(1)
    root.children[0].add(2)
    root.children[0].add(3)
    root.children[0].children[0].add(4)

    assert level_width_idiomatic(root) == [1, 1, 2, 1]


def test_level_width_3():
    root = Node(20)
    root.add(0)
    root.add(40)
    root.add(-15)
    root.children[0].add(12)
    root.children[0].add(-2)
    root.children[0].add(1)
    root.children[2].add(-2)

    assert level_width_idiomatic(root) == [1, 3, 4]


def test_compare_times():
    from timeit import timeit
    n = 100_000

    root = Node(20)
    root.add(0)
    root.add(40)
    root.add(-15)
    root.children[0].add(12)
    root.children[0].add(-2)
    root.children[0].add(1)
    root.children[2].add(-2)

    globals()['root'] = root

    # 0.151
    print('level_width:     ', timeit("level_width_idiomatic(root)", globals=globals(), number=n))
    # 0.177
    print('level_width_v2:  ', timeit("level_width_v1(root)", globals=globals(), number=n))
    # 0.228
    print('level_width_v3:  ', timeit("level_width_v2(root)", globals=globals(), number=n))

    for level_fn in (level_width_idiomatic, level_width_v1, level_width_v2):
        assert level_fn(root) == [1, 3, 4], level_fn.__name__
