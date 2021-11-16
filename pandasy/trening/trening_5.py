import pandas as pd

kostiumy = pd.read_csv('/home/wiola/Pulpit/Bazy_do_treningu/Halloween.csv', header=2)
print(kostiumy.head())
print('\n')

# 1. Skasować kolumny 3 i 4
kostiumy = kostiumy.drop(['2', '3'], axis=1)
print(kostiumy.head())
print('\n')

# 2. Zmienić nazwę kolumny 5 na 'Piąty’
kostiumy = kostiumy.rename(columns={'5': 'Piąty'})
print(kostiumy.head())
print('\n')

# 3. Utworzyć nowy zbiór danych, który nie zawiera regionów w których najpopularniejszym strojem był 'Angel’
kostiumy = kostiumy[kostiumy['1'] != 'Angel']
print(kostiumy)

