from plotly.graph_objs import (
    Bar,
    Layout
)
from plotly import offline

from throw_dice.dice import Dice

# Utworzenie dwóch kości do gry typu D6
dice_1 = Dice()
dice_2 = Dice()

# Wykonanie pewnej liczby rzutów kości i umieszczenie wyniku na liście
results = []
for roll_num in range(100):
    result = dice_1.roll() * dice_2.roll()
    results.append(result)

# Analiza wyniku
frequencies = []
max_result = dice_1.num_sides * dice_2.num_sides
for value in range(1, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Wizualizacji wyniku
x_values = list(range(1, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Wynik', 'dtick': 1}
y_axis_config = {'title': 'Częstotliwość występowania wartości'}
my_layout = Layout(title='Wynik rzuczenia dwóch kośćmi do gry D6 tysiąc razy', xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='d6*d6.html')

