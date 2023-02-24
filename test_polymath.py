import numpy as np
from polymath import root_mean_square

def test_rms():

    assert 4 == round(root_mean_square([3,3,5]))

def test_rms2():
    assert 7 == round(root_mean_square([9,7,5]))

