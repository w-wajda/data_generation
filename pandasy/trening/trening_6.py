import pandas as pd

df = pd.DataFrame({'Osoba': ['Michał Jakub', 'Ewa Noga', 'Krzysztof Zawierucha'],
                   'Wynik': [15, 38, 21]})
print(df)
print('\n')
# 1. Przy użyciu funkcji apply utworzyć nową kolumnę, z wartością 1, tam gdzie wynik jest powyżej 20 punktów
# # i wartością 0, tam gdzie wynik jest 20 punktów lub mniej


def sprawdz(punkty):
    if punkty > 20:
        return '1'
    else:
        return '0'


df['Zdany'] = df.Wynik.apply(sprawdz)
print(df)
print('\n')

# 2. Za pomocą funkcji apply, utworzyć kolumnę o formacie 'Nazwisko Imię’.
# Czyli na odwrót niż jest to w naszym DataFrame.


def zamien_kolejnosc(wiersz):
    imie_nazwisko = wiersz['Osoba'].split()
    wiersz['Nazwisko Imie'] = imie_nazwisko[1] + " " + imie_nazwisko[0]
    del wiersz['Zdany']
    return wiersz


df = df.apply(zamien_kolejnosc, axis=1)
print(df)
print('\n')






