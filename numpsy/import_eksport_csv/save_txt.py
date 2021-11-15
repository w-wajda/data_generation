import numpy as np

filename = 'new_file.csv'

csv_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

np.savetxt(filename, csv_arr)



