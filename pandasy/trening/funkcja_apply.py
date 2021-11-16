import pandas as pd

# Działanie funkcji apply

# Funkcja apply dla pojedynczej kolumny
df = pd.DataFrame({'Osoba': ['Michał Jakub', 'Ewa Noga', 'Krzysztof Zawierucha'],
                   'Wynik': [15, 38, 21]})

print(df)
print('\n')

# zadanie jest sprawdzić kto zdał egzamin. Dla wyniku > 20 punktów, należy zamienić ilość punktów na tekst 'Zdany’,
# w innym przypadku na tekst 'Oblany’


def sprawdz(punkty):
    if punkty > 20:
        return 'Zdany'
    else:
        return 'Oblany'


df.Wynik = df.Wynik.apply(sprawdz)
print(df)
print('\n')

# Funkcja apply, dla całego wiersza


def rozdziel(wiersz):
    wiersz['Imie'], wiersz['nazwisko'] = wiersz['Osoba'].split(' ')
    return wiersz


df = df.apply(rozdziel, axis=1)
print(df)
