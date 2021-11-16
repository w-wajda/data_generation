import pandas as pd

kostiumy = pd.read_csv('/home/wiola/Pulpit/Bazy_do_treningu/Halloween.csv', header=2)
print(kostiumy.head())
print('\n')

# Dodanie nowej kolumny
kostiumy['Nowa'] = '0'
print(kostiumy.head())
print('\n')

# Edycja wartości kolumn
# zamiana wartości na 1 w wierszy 'Nowa' tak gdzie najpopularniejsza jest 'Harley Quinn'
kostiumy.loc[kostiumy['1'] == 'Harley Quinn', 'Nowa'] = 1
print(kostiumy.head())

# Uporządkowanie kolumn

# Zmiana nazwy kolumn
kostiumy = kostiumy.rename(columns={'1': 'Pierwszy', '2': 'Drugi'})
print(kostiumy.head())

# Kasowanie kolumny
# kasowanie wiersza z indeksem 2
kostiumy = kostiumy.drop(2)
print(kostiumy.head())
print('\n')

# kasowanie kolumny - należy podać nazwę oraz informacje axis=1
kostiumy = kostiumy.drop('Nowa', axis=1)
print(kostiumy.head())
print('\n')

# Scalanie i rozdzielanie kolumn
# Scalanie - wystarczy utworzyć nową kolumnę na bazie już istniejących
kostiumy['Polaczone'] = kostiumy['3'] + '|' + kostiumy['4']
print(kostiumy[:3])
print('\n')

# Rozdzielanie
kostiumy[['Trzeci', 'Czwarty']] = kostiumy.Polaczone.str.split('|', expand=True)
print(kostiumy[:3])
print('\n')