import pandas as pd

filename = 'new_file.csv'

# Jeśli wszystkie Twoje kolumny są tego samego typu
x = pd.read_csv(filename, header=0).values
print(x)

# Można wybrać potrzbne kolumny
#x = pd.read_csv(filename, usecols=['Artist', 'Plays']).values
#print(x)