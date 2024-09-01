import math
import numpy as np
import nnfs

nnfs.init()
layer_outputs = [[4.8, 1.21, 2.385],
                 [8.9, -1.81, 0.2],
                 [1.41, 1.051, 0.026]]
E = math.e

exp_vals = np.exp(layer_outputs)
norm_vals = exp_vals / np.sum(exp_vals, axis = 1, keepdims = True) # axis 1 = rows
print(norm_vals)