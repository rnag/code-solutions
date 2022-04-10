"""
Copy this template and create a new example file from it as needed

"""
from pprint import pprint
from dsa.linked_list.doubly_linked_list import DoublyLinkedList, Node


ll = DoublyLinkedList()


def main():
    global ll

    ll = DoublyLinkedList()
    add_example('push')
    # add_example('unshift')

    # get_example()

    # set_example('set')
    set_example('insert')

    # reverse the linked list in place
    # reverse_example()

    # example of `pop()`
    pop_example('pop')
    # example of `shift()`
    # pop_example('shift')
    # example of `remove()`
    # remove_example()


def get_example():
    print(f'=== Example: `get()` ===')

    # last index is out of bounds, should return undefined
    for i in range(0, ll.length + 1):
        print(f'Item #{i + 1}:', ll.get(i))
    print()


def set_example(meth_name: str):
    print(f'=== Example: `{meth_name}()` ===')
    meth = getattr(ll, meth_name)
    meth(0, 'OLLEH')
    meth(1, 'CYA')
    # just for kicks, let's insert it at a non-consecutive index
    meth(4, 'WORLD')
    # just print out updated linked list
    get_example()
    # assert data is as expected
    if meth_name == 'insert':
        assert ll.get(4).val == 'WORLD'


def add_example(meth_name: str):
    print(f'=== Example: `{meth_name}()` ===')
    meth = getattr(ll, meth_name)

    meth('HELLO')
    meth('GOODBYE')
    meth('BRO')

    pprint(ll)
    print()

    # confirm our linked list is as expected
    # TODO: gonna be tough 'cause we have `prev` now also
    # if meth_name == 'push':
    #     assert ll == DoublyLinkedList(
    #         head=Node(val='HELLO',
    #                   next=Node(val='GOODBYE',
    #                             next=Node(val='BRO', next=None))),
    #         tail=Node(val='BRO', next=None),
    #         length=3)
    # else:
    #     assert ll == DoublyLinkedList(
    #         head=Node(val='BRO',
    #                   next=Node(val='GOODBYE',
    #                             next=Node(val='HELLO', next=None))),
    #         tail=Node(val='HELLO', next=None),
    #         length=3)


def pop_example(meth_name: str):
    print(f'=== Example: `{meth_name}()` ===')
    meth = getattr(ll, meth_name)

    item = meth()
    print('Node:', item)
    print('List:', ll)
    print()

    item = meth()
    print('Node:', item)
    print('List:', ll)
    print()

    item = meth()
    print('Node:', item)
    print('List:', ll)
    print()

    item = meth()
    print('Node:', item)
    print('List:', ll)
    print()


def remove_example():
    print(f'=== Example: `remove()` ===')

    curr_length = ll.length

    item = ll.remove(0)
    print('Removed Item #1:', item)
    print('List:', ll)
    print()

    # remember that we already removed one item,
    # so remove(2) is like remove(3)
    item = ll.remove(2)
    print('Removed Item #4:', item)
    print('List:', ll)
    print()

    # we removed 2 items, so the length should be updated accordingly
    assert curr_length == curr_length - 2


def reverse_example():
    print(f'=== Example: `reverse()` ===')
    ll.reverse()

    # just print out updated linked list
    get_example()


if __name__ == '__main__':
    main()
