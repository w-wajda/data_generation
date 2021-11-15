import pandas as pd

# łączenie DataFrame – SQL Join
# połączenia dwóch tabel, za pomocą wspólnego klucza

# pierwsza tabela zawiera imie i wiek, a druga tabela ma imie i miejsce zamieszkania. imie jest kluczem wspólnym

a = [['Ania', 24], ['Michał', 9], ['Darek', 40], ['Ewa', 43]]
df_a = pd.DataFrame(a)
df_a.columns = ['Imie', 'Wiek']
print(df_a)
print('\n')

b = {'Imie': ['Ewa', 'Michał', 'Krzysiek', 'Kasia', 'Lucja'], 'Miasto': ['Warszawa', 'Kraków', 'Gdańsk',
                                                                         'Poznań', 'Łódź']}
df_b = pd.DataFrame(b)
print(df_b)
print('\n')

# 1 - połącznie części wspólnej
print(pd.merge(df_a, df_b, on='Imie'))
print('\n')

# 2 - połącznie wierszy ze zbioru lewego, pasujące wiersze ze zbioru prawego
print(pd.merge(df_a, df_b, on='Imie', how='left'))
print('\n')

# 3 - połącznie wierszy ze zbioru prawego, pasujące wiersze ze zbioru lewego
print(pd.merge(df_a, df_b, on='Imie', how='right'))
print('\n')

# 4 - połącznie wszystkich wierszy
print(pd.merge(df_a, df_b, on='Imie', how='outer'))