# 1. Należy wydrukować tylko i wyłącznie miasto oraz kraj, dla 10 pierwszych rekordów
# 2. Jakie unikalne wartości zawiera kolumna Capital?
# 3. Dla ilu miast brakuje informacji o ich populacji?

import pandas as pd

miasta = pd.read_csv('/home/wiola/Pulpit/Bazy_do_treningu/worldcities.csv')

# 1.
print(miasta[:11][['city', 'country']])
print('\n')

# 2.
print(miasta.capital.unique())
print('\n')

# 3.
print(miasta.capital.isnull().sum())
print('\n')