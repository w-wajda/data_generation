import pandas as pd

# PIERWSZY TYP DANYCH - SERIES
a = pd.Series([-1, 1, 3, 5, 7])

# mnożenie
print(a * 10)

# zmiana wartości na dodatnią, funkcja abs
print(a.abs())

# wyświetlenie podstawowych statystyk
print(a.describe())

# zmiana nazw indeksu
a.index = ['Pierwsza', 'Druga', 'Trzecia', 'Czwarta', 'Piąta']
print(a)



