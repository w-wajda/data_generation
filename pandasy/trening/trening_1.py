# Utwórzmy DataFrame na podstawie list, oraz nadajmy nazwy naszym kolumnom.
# Utwórzmy analogiczny DataFrame na podstawie słownika
# Utwórzmy analogiczny DataFrame na podstawie Series

import pandas as pd

lista = [['Warszawa', 1879534], ['Kraków', 346543], ['Poznań', 467362], ['Wrocław', 976281],
         ['Gdańsk', 1273625]]
a = pd.DataFrame(lista)
a.columns = ['Miasto', 'Populacja']
print(a)
print('\n')

slownik = {'Miasta': ['Warszawa', 'Kraków', 'Poznań', 'Wrocław', 'Gdańsk'], 'Populacja': [1879534, 346543, 467362,
                                                                                          976281, 1273625]}
b = pd.DataFrame(slownik)
print(b)
print('\n')

c = pd.Series(lista)
print(c)


