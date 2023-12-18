import numpy as np
from Lab3 import *
from Lab6 import *
from Lab8 import *

matrix = np.array([[5, 0, 4],
                   [0, 1, -4],
                   [4, -4, 3]])

matrix = np.array([[0.6444, 0, -0.1683, 0.1184, 0.1973],
                   [-0.0395, 0.4208, 0, -0.0802, 0.0263],
                   [0.0132, -0.1184, 0.7627, 0.0145, 0.0460],
                   [0.0395, 0, -0.0960, 0.7627, 0],
                   [0.0263, -0.0395, 0.1907, -0.0158, 0.5523]])

array = np.array([1.2677, 1.6819, -2.3657, -6.5369, 2.8351]).transpose()

Jacobi_method(matrix, array)

# power_method(matrix)

# rotation_method(matrix)
