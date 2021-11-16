# Wyświetlić kolumny region oraz najpopularniejszy kostium dla pierwszych 20 wierszy
# Dla siódmego wiersza ustawić strój Batmana jako najpopularniejszy kostium
# Zmienić index na kolumnę 'region’, a następnie dla regionu 'California’ ustawić najpopularniejszy kostium jako 'Witch’
# Jakie są wszystkie kostiumy w naszym zbiorze danych?

import pandas as pd

kostiumy = pd.read_csv('/home/wiola/Pulpit/Bazy_do_treningu/Halloween.csv', header=2)

# 1
print(kostiumy[:20][['region', '1']])
print('\n')

# 2
kostiumy.iloc[6, 1] = 'Batman'
print(kostiumy[:20][['region', '1']])
print('\n')

# 3
print(kostiumy.region.is_unique)
kostiumy = kostiumy.set_index('region')
kostiumy.loc['California', '1'] = 'Witch'
print(kostiumy)
print('\n')

# 4
print('Zadanie 4')
kostiumy.drop_duplicates()

all_columns = []
column_1 = [kostiumy['1'].unique()]
column_2 = [kostiumy['2'].unique()]
print('\n')

all_columns.append(column_1)
all_columns.append(column_2)

print(all_columns)









