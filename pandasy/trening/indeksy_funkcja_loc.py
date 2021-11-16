import pandas as pd

kostiumy = pd.read_csv('/home/wiola/Pulpit/Bazy_do_treningu/Halloween.csv', header=2)
# wyświetlenie pierwszych 5 wierzy z wszystkimi kolumnami
print(kostiumy.head())
print('\n')

# PRZEGLĄDANIE  DataFrame Z UŻYCIEM []

# 1. 5 pierwszych wierszy
print('Nowe zadanie 1')
print(kostiumy[:5])
print('\n')

# 2. 10 pierwszych wierszy i tylko i wyłącznie kolumny region oraz '1', czyli najpopularniejszy kostium
print('Nowe zadanie 2')
print(kostiumy[:10][['region', '1']])
print('\n')

# INDEKSY

# 3. Pokazać indeksy
print('Zadanie 3')
print(kostiumy.index)
print('\n')

# 4. Sprawdzić czy kolumna 'region' ma unikalne wartości - zwraca Treu lub False
print('Zadanie 4')
print(kostiumy.region.is_unique)
print('\n')

# 5. Jeśli kolumna region jest unikatowa, to może stać się indeksem
print('Zadanie 5')
kostiumy.set_index('region', inplace=True)
print(kostiumy.head())
print('\n')

# 6.Funkcja odwołująca set_index i powrót do stanu początkowego
print('Zadanie 6')
kostiumy = kostiumy.reset_index()
# lub inna forma
kostiumy.reset_index(inplace=True)
print('\n')

# FUNKCJA loc - ODOWŁUJE SIĘ DO KONKRETNEGO WIERSZA NA BAZIE NAZW

# 7. Odowłanie się do konkretnego miejsca, np. do regionu Arizona
print('Zadanie 7')
kostiumy = kostiumy.set_index('region')
# np. do regionu Arizona
print(kostiumy.loc['Arizona'])
print('\n')

# 8. Odowłanie się do konkretnego elementu tablicy i zmiana na inną nazwę
print('Zadanie 8')
kostiumy.loc['Arizona', '1'] = 'Batman'
print(kostiumy.head())
# jeśli zostaną indeksy liczbowe, przykład można zapisać inaczej
kostiumy.loc[3, '1'] = 'Batman'
print('\n')

# FUNKCJA iloc - korzysta tylko i wyłącznie z wartości numerycznych indeksów. przyjmie tylko numery wierszy i kolumn
print('Zadanie 9')
print(kostiumy.iloc[3, 1])