import pandas as pd

# Przykład użycia funkcji read_excel()
imiona = pd.read_excel('/home/wiola/Pulpit/Bazy_do_treningu/imiona.xlsx')
print(imiona)
print('\n')

wynik = pd.read_excel('/home/wiola/Pulpit/Bazy_do_treningu/imiona.xlsx', sheet_name='Wynik', header=1)
print(wynik)
print('\n')

wynik2 = pd.read_excel('/home/wiola/Pulpit/Bazy_do_treningu/imiona.xlsx', sheet_name='Wynik2', header=None,
                       names=['Imie', 'Nazwisko', 'Wynik'])
# inny zapis
wynik3 = pd.read_excel('/home/wiola/Pulpit/Bazy_do_treningu/imiona.xlsx', sheet_name='Wynik2', header=None)
wynik3.columns = ['Imie', 'Nazwisko', 'Wynik']
print(wynik2)
print('\n')

# Przykład użycia funkcji read_csv()
miasta = pd.read_csv('/home/wiola/Pulpit/Bazy_do_treningu/worldcities.csv')
print(miasta)
print('\n')

# Przykład użycia funkcji to_excel oraz to_json
miasta.to_excel('/home/wiola/Pulpit/Bazy_do_treningu/miasta.xlsx', sheet_name='Miasta')
miasta.to_json('/home/wiola/Pulpit/Bazy_do_treningu/miasta.json')
