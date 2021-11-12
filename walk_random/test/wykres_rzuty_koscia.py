from plotly.graph_objs import Bar, Layout
from plotly import offline
from rzuty_kostka import Kostka

kostka = Kostka()

rezultaty = []
for rzut in range(100):
    wynik = kostka.rzut_koscia()
    rezultaty.append(wynik)

print(rezultaty)

# Analiza wyników
czestotliowsci = []
for wartosci in range(1, kostka.ilosc_scian + 1):
    czestotliwosc = rezultaty.count(wartosci)
    czestotliowsci.append(czestotliwosc)

print(czestotliowsci)

print({1: czestotliowsci[0], 2: czestotliowsci[1], 3: czestotliowsci[2], 4: czestotliowsci[3],
      5: czestotliowsci[4], 6: czestotliowsci[5]})

# Wizualizacja wyniku

