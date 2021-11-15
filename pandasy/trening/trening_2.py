# Należy wydrukować tylko i wyłącznie miasto oraz kraj, dla 10 pierwszych rekordów
# Jakie unikalne wartości zawiera kolumna Capital?
# Dla ilu miast brakuje informacji o ich populacji?

import pandas as pd

miasta = pd.read_csv('/home/wiola/Pulpit/Bazy_do_treningu/worldcities.csv')
print(miasta[:11][['city', 'country']])

print(miasta.capital.unique())

print(miasta.capital.isnull().sum())
