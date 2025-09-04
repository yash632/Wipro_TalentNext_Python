# 1. Create two dimensional 3*3 array and perform ndim, shape, slicing operation on it.
import numpy as np

arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Array:\n", arr_2d)
print("ndim:", arr_2d.ndim)
print("shape:", arr_2d.shape)
print("Slicing [first two rows, first two cols]:\n", arr_2d[:2,:2])

# 2. Create one dimensional array and perform ndim, shape, reshape operation on it.
arr_1d = np.array([1,2,3,4,5,6])
print("Array:", arr_1d)
print("ndim:", arr_1d.ndim)
print("shape:", arr_1d.shape)
print("Reshaped to 2x3:\n", arr_1d.reshape(2,3))
