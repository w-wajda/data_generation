# 1. wydrukować regiony w których najpopularniejszym kostiumem jest 'Witch’, natomiast drugi najpopularniejszym jest 'Ninja’
# 2. policzyć regiony które jako najpopularniejszy kostium mają 'Dinosaur’ lub 'Angel’

import pandas as pd

kostiumy = pd.read_csv('/home/wiola/Pulpit/Bazy_do_treningu/Halloween.csv', header=2)
print(kostiumy.head())
print('\n')

# 1.
print(kostiumy[(kostiumy['1'] == 'Witch') & (kostiumy['2'] == 'Ninja')])
print('\n')

# 2.
ilosc = kostiumy[(kostiumy['1'] == 'Dinosaur') | (kostiumy['1'] == 'Angel')]

print(ilosc.region.describe())
print('\n')

print(ilosc.region.count())
print('\n')

# jeśli mamy liczby
print(ilosc['region'].sum())
print('\n')

