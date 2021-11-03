from plotly.graph_objs import Bar, Layout
from plotly import offline

from throw_dice.dice import Dice

# Utworzenie kości typu D6
dice = Dice()

# Umieszczenie pewnej liczby rzutów i umieszczebue wyników na liście
results = [dice.roll() for roll_number in range(1000)]

# Analiza wyniku
frequencies = [results.count(value) for value in range(1, dice.num_sides + 1)]

print(frequencies)

frequencies_dict = {1: frequencies[0], 2: frequencies[1], 3: frequencies[2], 4: frequencies[3], 5: frequencies[4],
                    6: frequencies[5]}

max_result = max(frequencies)
for key, value in frequencies_dict.items():
    if value == max_result:
        print(f'Najwięcej razy była wyrzucana liczba: {key}')

# Utworzenie histogramu wykres słupkowego pokazujący, jak częstp wystąpił dany wyniku (wizualizacja wyniku)
x_value = list(range(1, dice.num_sides + 1))
data = [Bar(x=x_value, y=frequencies)]

x_axis_config = {'title': 'Wynik'}
y_axis_config = {'title': 'Częstotliwość występowania wartości'}

my_layout = Layout(title='Wynik rzucenia pojedynczą kością D6 tysiąc razy', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')


