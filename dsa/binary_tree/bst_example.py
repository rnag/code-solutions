"""
Copy this template and create a new example file from it as needed

"""
from pprint import pprint

from dsa.binary_tree.bst import BinarySearchTree, Node


heap = BinarySearchTree()


def main():
    global heap
    print('=== Example: `insert()` ===')
    tree.insert(10)
    tree.insert(5)
    tree.insert(13)
    tree.insert(11)
    tree.insert(2)
    tree.insert(16)
    tree.insert(16)
    tree.insert(7)

    pprint(tree)
    print()

    print('=== Example: `find()` ===')
    print(tree.find(10))
    print(tree.find(16))
    print(tree.find(7))
    # shouldn't be in there
    print(tree.find(8))
    print()

    result = traverse_method('BFS')
    # horizontal before vertical!
    assert result == [10, 5, 13, 2, 7, 11, 16]

    result = traverse_method('DFS_pre_order')
    # correct: traverse whole left side before right side
    assert result == [10, 5, 2, 7, 13, 11, 16]

    result = traverse_method('DFS_post_order')
    # correct: traverse each side first, with a BOTTOM-UP approach
    assert result == [2, 7, 5, 11, 16, 13, 10]

    result = traverse_method('DFS_in_order')
    # correct: traverse each side first, with a BOTTOM-UP approach
    assert result == [2, 5, 7, 10, 11, 13, 16]


def traverse_method(meth_name: str):
    print(f'=== Example: `{meth_name}()` ===')
    meth = getattr(heap, meth_name)
    result = meth()
    print(result)
    print()

    return result


if __name__ == '__main__':
    main()
