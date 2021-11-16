import pandas as pd

films = pd.read_csv('/home/wiola/Pulpit/Bazy_do_treningu/film.csv', sep=';', encoding='ISO-8859-1')

# Kasujemy pierwszy wiersz
films = films.drop(0)

# Kasujemy ostatnią kolumnę
films = films.drop(columns=['*Image'])
print(films.head())

# Typy danych w Pandas DataFrame
# films.Length.mean() - nie możemy policzyć średniej, bo cały plik jest str, a chcemy zorbić działanie matematyczne
# w takiej sytuacji należy zmienić typy danych
print(films.info())

# Zamiana typów danych w Pandas DataFrame

# to_numeric() - Zamiana kolumn, które są rozpoznawane jak typ object, a zawierają liczby, na typ danych numeryczny.
films.Length = pd.to_numeric(films.Length)
print(films.dtypes)
# Lenght zmienił się na float, wiec może policzyć średnią długość filmu
print(films.Length.mean())

# astype() - wymaga ręcznego podania typu danych, który chcemy osiągnąć
films.Popularity = films.Popularity.astype('float64')
print(films.Popularity.max())

# apply() - która może czytać wartość w jednym formacie, a zwracać ją w zupełnie innych (tworzenie def...)
# sprawdzenie czy dany film dostał nagrodzę czy nie


def zamien(wartosc):
    if wartosc == 'No':
        return False
    if wartosc == 'Yes':
        return True


films.Awards = films.Awards.apply(zamien)
# zbiór się zmienił
print(films.dtypes)
print(films.head())

#Funkcją read_csv() jest to możliwe korzystając z dodatkowych parametrów takich jak:

# dtype, który zdefiniuje nam od razu typy kolumn,
# skiprows, który umożliwi nam ominięcie pierwszego, problematycznego wiersza.
# usecols, gdzie możemy podać interesujące nas kolumny
# czy też converters, który umożliwia nam zastosowanie apply


def zamien(wartosc):
    if wartosc == 'No': return False
    if wartosc == 'Yes': return True


filmy = pd.read_csv('https://analityk.edu.pl/wp-content/uploads/2020/12/film.csv',
                    sep=';',
                    encoding="ISO-8859-1",
                    skiprows=[1],
                    dtype={'Length': 'float64', 'Popularity': 'float64'},
                    usecols=['Year', 'Length', 'Title', 'Subject', 'Popularity', 'Awards'],
                    converters={'Awards': lambda x: True if x == 'Yes' else False})

print(filmy.head())


