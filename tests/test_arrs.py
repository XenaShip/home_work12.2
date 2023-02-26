from utils import arrs

def test_get():
    assert arrs.get([0,2,4,5], 1) == 2
    assert arrs.get([0,0,0,0], -1) == None
    assert arrs.get([0], 3) == None


