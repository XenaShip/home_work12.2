from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == 'test'
    assert arrs.get([3, 48, 5], -10) is None
    assert arrs.get([1, 2, 3, 4], 10) is None


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3, 4], -1, 3) == []
    assert arrs.my_slice([1, 2, 3, 3], -1, 1) == []
    assert arrs.my_slice([1, 2], 1, 4) == [2]
    assert arrs.my_slice([1, 2, 3, 4], 1, -5) == []
    assert arrs.my_slice([1, 2, 3, 4], 0, -1) == [1, 2, 3]
    assert arrs.my_slice([], 1, 2) == []
    assert arrs.my_slice([1, 2, 3, 4], -10, 1) == [1]
