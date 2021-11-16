import pandas as pd

films = pd.read_csv('https://analityk.edu.pl/wp-content/uploads/2020/12/film.csv',
                    sep=';',
                    encoding="ISO-8859-1",
                    skiprows=[1],
                    dtype={'Length': 'float64', 'Popularity': 'float64'},
                    usecols=['Year', 'Length', 'Title', 'Subject', 'Popularity', 'Awards'],
                    converters={'Awards': lambda x: True if x == 'Yes' else False})

# Pandas Group by – prosty przykład
# Chcemy poznać ilość filmów dla poszczególnych lat.
# groupby przyjmuje parametr nazwę kolumny po której dokonujemy grupowania oraz funkcji count() która zliczy rekordy:
print(films.groupby('Year').count())

# Można skupić się na jednej kolumnie, wykonać operację na przykład mean() i policzyć średnią popularność filmu:
print(films.groupby('Year').Popularity.mean())

# Pandas Group by, dla kilku kolumn
# Możemy policzyć średnią długość trwania filmu dla danego roku, dodatkowo w rozbiciu na np kategorię filmu.
# W tym celu do naszej funkcji group by, podamy 2 parametry:
print(films.groupby(['Year', 'Subject']).Length.mean())

# Pandas Group by – funkcja agg
# Obliczyć minimalną oraz maksymalną długość filmu oraz minimalną oraz maksymalną popularność filmu?
# najlpiej zobaczmy jak ona wygląda
print(films.groupby('Year').agg({'Popularity': ['min', 'max'], 'Length': ['min', 'max']}))

# wywołać funkcję można tak
print(films.groupby('Year').agg(mininalna_popularnosc=('Popularity', 'min'),
                                maksymalna_popularnosc=('Popularity', 'max')))

print(films.groupby('Year').agg(mininalna_dlugosc_filmu=('Length', 'min'),
                                maksymalna_dlugosc_filmu=('Length', 'max')))

# Filtrowanie
# chcemy policzyć średnią długość trwania filmu, dla filmów z okresu 1980 – 1990.
# zamienimy rok na liczby, a następnie użyjemy [], aby wyfiltrować potrzebne dla nas dane.
films['Year'] = pd.to_numeric(films.Year)
print(films[(films['Year'] > - 1980) & (films['Year'] <= 1990)].groupby('Year').Length.mean())
