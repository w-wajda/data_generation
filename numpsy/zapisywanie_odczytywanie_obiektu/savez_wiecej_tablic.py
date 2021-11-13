import numpy as np

filename_2 = 'filename_2.npz'

xx = np.array([[1, 2], [3, 4]])
yy = np.array([[5, 6]])

np.savez(filename_2, xx, yy)

