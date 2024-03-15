import math
import numpy as np

def rotate_2d(a):
    return np.array([
        [math.cos(a), -math.sin(a), 0],
        [math.sin(a), -math.cos(a), 0]
        [0, 0, 1]
    ])