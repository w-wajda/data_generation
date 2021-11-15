import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('http://analityk.edu.pl/wp-content/uploads/2020/01/Countries.csv')
df_pop = df[['Country', 'Region', 'Population', 'Phones per 1000']].copy()

df_pop.groupby('Region')['Population'].sum().plot(kind='pie')
plt.show()