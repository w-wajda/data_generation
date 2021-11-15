import pandas as pd

miasta = pd.read_csv('/home/wiola/Pulpit/Bazy_do_treningu/worldcities.csv')

# Szybki podgląd DataFrame

# wyświetlenie 5 pierwszych wierszy
print(miasta.head())
# lub
print(miasta[:5])
# lub
print(miasta[0:5])

# wyświetlenie 5 ostanich wierszy
print(miasta.tail())
# lub
print(miasta[26564:])

# wyświetlenie interesujących kolumn np.city
print(miasta['city'])
# lub
print(miasta.city)

# prawdzenie jakie wartości unikalne przyjmuje kolumna
print(miasta.capital.unique())

# wyświetlenie kilku interesujących kolumn np.city, iso3
print(miasta[['city', 'iso3']])

# wyświetlenie kolumny city i zakresu 5 pierwszych wierszy
print(miasta[0:5]['city'])

# Wielkość, szerokość i typ danych w DataFrame
# uzyskanie informacji na temat formy

# zwrócenie informacji na temat liczby kolumn i wierszy
print(miasta.shape)

# informacja na temat kolumn, typ danych i ilość rekordów (innych niż NaN)
print(miasta.info())

# inormacja o podstawowych statystykach dla kolumn
print(miasta.describe())
# funkcje describe można wykonywać na konkretnej kolumnie
print(miasta.population.describe())

# Puste wartości oraz duplikaty

# brakujące wartości – NaN
# informacja czy dana komórka jest pusta czy nie
print(miasta.isnull())
# można zsumować te wyniki
print(miasta.isnull().sum())
# analogiczna informacja
print(miasta.notnull().sum())

# zduplikowane wartości - sprawdzenie ilości duplikatów
print(miasta.duplicated().sum())
# usunięcie duplikatów
miasta.drop_duplicates()










