from plotly.graph_objs import Bar, Layout
from plotly import offline

from throw_dice.dice import Dice

# Utworzenie dwóch kości do gry typu D8
dice_1 = Dice(8)
dice_2 = Dice(8)

# Wykonanie tysiąca rzutów dwoma kostkami typu D8 i  umieszczenie wyników na liście
results = [dice_1.roll() + dice_2.roll() for roll_num in range(1000)]

# Analiza wyniku
max_result = dice_1.num_sides + dice_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result + 1)]

# Wizualizacja wyników
x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Wynik', 'dtick': 1}
y_axis_config = {'title': 'Częstotliwość występowania wartości'}
my_layout = Layout(title='Wynik rzucania dwoma kośćmi D8 tysiąc razy', xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='2xd8.html')

