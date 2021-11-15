import pandas as pd

# DATAFRAME - typ danych
# tworzenie dataframe na podstawie listy
lista = [1, 2, 3, 4]

a = pd.DataFrame(lista)
a.columns = ['Liczby']
print(a)
print('\n')

lista_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = pd.DataFrame(lista_2)
b.columns = ['Pierwsza kolumna', 'Druga kolumna', 'Trzecia kolumna']
print(b)
print('\n')

# tworzenie dataframe na podstawie słownika
slownik = {'Imie': ['Ania', 'Michał', 'Przemek'], 'Wiek': [18, 25, 40]}
c = pd.DataFrame(slownik)
print(c)
print('\n')

# SERIES - typ danych
# tworzenie series na podstawie listy
lista_3 = [11, 33, 55, 99]
d = pd.Series(lista_3)
print(d)