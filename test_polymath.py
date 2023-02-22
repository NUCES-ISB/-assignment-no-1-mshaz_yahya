import numpy as np
from polymath import root_mean_square

def test_rms():
    assert 4 == round(root_mean_square([3,3,5]))