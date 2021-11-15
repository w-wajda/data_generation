import pandas as pd

# DRUGI TYP DANYCH - DATAFRAME

# tworzenie dataframe na bazie listy
a = [['Ania', 24], ['Iza', 33], ['Wiola', 38], ['Justyna', 35], ['Monika', 28]]

df_a = pd.DataFrame(a)
df_a.columns = 'Imie', 'Wiek'
print(df_a)

# tworzenie dataframe na bazie słownika
b = {'Imie': ['Ania', 'Iza', 'Wiola', 'Justyna', 'Monika'], 'Miasto': ['Warszawa', 'Kraków', 'Zabrze', 'Katowice',
                                                                       'Gdańsk']}

df_b = pd.DataFrame(b)
print(df_b)

# tworzenie dataframe na bazie pliku csv
df = pd.read_csv('http://analityk.edu.pl/wp-content/uploads/2020/01/Countries.csv')

# wyświetlenie konkretnych wierszy
print(df[:3])

# wyświetlenie konkretnych wierszy i kolumn
print(df[['Country', 'Region']], df[:3])

# inny sposób wyświetlenie konkretnych wierszy i kolumn
print(df.iloc[0:3, 0:3])

# odniesienie się do konkretnych komórek, za pomocą numeru wiersza oraz nazwy kolumny
print(df.loc[:3, ['Country', 'Region', 'Population']])

# PODSTAWOWE OPERACJE NA DATAFRAME

# tworzenie frgmentu tabeli za pomocą kopiowania (kopia z wybranymi kolumnami)

df_pop = df[['Country', 'Region', 'Population', 'Phones per 1000']].copy()
print(df_pop[:3])

# kolumna 'Population’ zamieniona na miliony, podzielić przez 1 000 000
df_pop['Population'] /= 1000000
print(df_pop[:3])

# dodanie nowej kolumny i przypisanie jej wartości np.1
df_pop['Nowa kolumna'] = 1

# wyświetlenie nowej kolumny za pomocą funkcji head()
print(df_pop.head())

# zmiana nazwy kolumny
df_pop = df_pop.rename(columns={'Nowa kolumna': 'Inna Nazwa'})
print(df_pop)

# iteracja for loop: iterrows(), oraz itertuples()
# przeglądanie dataframe przy użyciu iterrows() w pętli for
for index, row in df_pop.iterrows():
    if row['Population'] > 100:
        df_pop.loc[index, 'Size'] = 'Big'
        print(row['Country'], df_pop.loc[index, 'Size'])

# rzeglądanie dataframe przy użyciu itertuples() w pętli for
for row in df_pop.itertuples():
    if row.Population > 200:
        print(row.Index, row.Country, row.Population)

# FILTROWANIE DATAFRAME W PANDAS

# filtrownie za pomocą mask w pandas
print(df_pop.Population == 1313.973713)  # tworzy się maska, która dla wierszy o populacji podanej zwróci wartość True,
# a dla pozostałych False.

# fitrowanie całego wiersza i odnalezienie poszukiwanego
print(df_pop[df_pop.Population == 1313.973713])
print(df_pop[df_pop['Population'] == 1313.973713])

# łączenie wyrażenia operatorem &, będący odpowienikiem 'and’, lub operatorm |, będący odpowiednikiem 'or’
print(df_pop[(df_pop['Population'] > 100) & (df_pop['Population'] < 150)])

# sumowanie, grupowanie, oraz inne kalkulacje
# policzone statystyki dla wszystkich kolumn
print(df_pop['Population'].sum())
print(df_pop['Population'].max())
print(df_pop['Population'].min())
print(df_pop['Population'].mean())

# kalkulacje dla poszczególnych regionów, używając funkcji groupby(’Region’)
print(df_pop.groupby('Region')['Population'].sum())
print(df_pop.groupby('Region')['Population'].min())
print(df_pop.groupby('Region')['Population'].max())
print(df_pop.groupby('Region')['Population'].mean())
print(df_pop.groupby('Region')['Population'].size())

# połączenie wszsytkich tablic w jedno
print(df_pop.groupby('Region')['Population'].agg([min, max, sum]))

# ta sama metoda wykorzystując słownik
print(df_pop.groupby('Region', as_index=False)['Population'].agg({'Suma': 'sum', 'Max': 'max'}))

# łączenie DataFrame – SQL Join
