from basic.qfroms.qfroms import Queue


def test_order_is_maintained():
    q = Queue(1, 2, 3)

    assert q.remove() == 1
    assert q.remove() == 2
    assert q.remove() == 3
    assert q.remove() is None
