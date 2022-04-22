from queue import Queue
from weave import weave


def test_weave():
    one = Queue(1, 2, 3, 4)
    two = Queue('one', 'two', 'three', 'four')

    result = weave(one, two)
    assert result.dequeue() == 1
    assert result.dequeue() == 'one'
    assert result.dequeue() == 2
    assert result.dequeue() == 'two'
    assert result.dequeue() == 3
    assert result.dequeue() == 'three'
    assert result.dequeue() == 4
    assert result.dequeue() == 'four'

    assert result.dequeue() is None
