import numpy as np

filename_csv = 'new_file.csv'

csv_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

np.savetxt(filename_csv, csv_arr)

