import numpy as np 
import contint as c

def test_distance():
    # fill this in
    dis = c.distances([0,0],[1,0])
    assert dis == 1

def test_average():
    # fill this in
    avg = c.average([1,1,1,1])
    assert avg == 1

    avg = c.average(5)
    assert avg == 5

    avg = c.average([1,2,3,4,5])
    assert avg == 3