import matplotlib.pyplot as plt
import numpy as np

plt.title('Wykresy funkcji liniowych', c='red')
plt.xlabel('Wartości osi x', c='red')
plt.ylabel('Wartości osi y', c='red')

plt.tick_params(axis='both', color='red')

plt.axvline(x=0, color='red')
plt.axhline(y=0, color='red')

try:
    a = int(input('Podaj współczynnik a: '))
except ValueError:
    print('Niepoprawny współczynnik')
else:
    x_1 = np.arange(-10, 10, 0.5)
    y_1 = x_1/(-3) + a

    x_2 = np.arange(-10, 10, 0.5)
    y_2 = x_2*x_2/3

    plt.plot(x_1, y_1, linewidth=5, c='blue')
    plt.plot(x_2, y_2, linewidth=5, c='yellow')

plt.show()

