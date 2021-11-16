# 1. Powtórzyć czyszczenie pliku, nie używając opcji funkcji read_csv()
import pandas as pd

films = pd.read_csv('/home/wiola/Pulpit/Bazy_do_treningu/film.csv', sep=';', encoding='ISO-8859-1')

films = films.drop(0)
films = films.drop(columns=['*Image'])
films.Year = pd.to_numeric(films.Year)
films.Length = pd.to_numeric(films.Length)
films.Popularity = films.Popularity.astype('float64')


def zamien(wartosc):
    if wartosc == 'No':
        return False
    if wartosc == 'Yes':
        return True


films.Awards = films.Awards.apply(zamien)


print(films)
print(films.info())

# 2. Powrócić do pliku Halloween i sprawdzić z jakimi typami danych mieliśmy tam do czynienia.
kostiumy = pd.read_csv('/home/wiola/Pulpit/Bazy_do_treningu/Halloween.csv', header=2)
print(kostiumy.head())
print(kostiumy.info())