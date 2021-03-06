from plotly.graph_objs import Bar, Layout
from plotly import offline

from throw_dice.dice import Dice

# Utworzenie kości typu D6 i D10
dice_1 = Dice()
dice_2 = Dice(10)

# Wykonanie pewnej liczby rzutów i umieszczenie wyników na liście
results = []
for roll_num in range(50000):
    result = dice_1.roll() + dice_2.roll()
    results.append(result)

# Analiza wyników
frequencies = []
max_result = dice_1.num_sides + dice_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Wizualizacja wyników
x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]
x_axis_config = {'title': 'Wynik', 'dtick': 1}
y_axis_config = {'title': 'Częstotliwość występowania wartości'}
my_layout = Layout(title='Wynik rzucania kośćmi D6 i D10 pięćdziesiąt tysięcy razy', xaxis=x_axis_config,
                   yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')