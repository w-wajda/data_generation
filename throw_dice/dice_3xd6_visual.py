from plotly.graph_objs import Bar, Layout
from plotly import offline

from throw_dice.dice import Dice

# Utworzenie trzech kośćmi do gry typu D6
dice_1 = Dice()
dice_2 = Dice()
dice_3 = Dice()

# Wykonanie pewnej liczby rzutów i umieszczenie wyników w liście
results = []
for roll_num in range(1000):
    result = dice_1.roll() + dice_2.roll() + dice_3.roll()
    results.append(result)

# Analiza wyników
frequencies = []
max_result = dice_1.num_sides + dice_2.num_sides + dice_3.num_sides
for value in range(3, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Wizualizacja wyników
x_values = list(range(3, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Wynik', 'dtick': 1}
y_axis_congif = {'title': 'Częstotliwość występowania wartości'}
my_layout = Layout(title='Wynik rzucania trzema kośćmi D6 tysiąc razy', xaxis=x_axis_config, yaxis=y_axis_congif)

offline.plot({'data': data, 'layout': my_layout}, filename='3xd6.html')




