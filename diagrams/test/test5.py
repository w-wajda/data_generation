import matplotlib.pyplot as plt

try:
    a = int(input('Podaj współczynnik a: '))
    b = int(input('Podaj współczynnik b: '))
except ValueError:
    print('Niepoprawny współczynnik')
else:
    list_x = range(11)
    list_y = [(a * x + b) for x in list_x]

    plt.title('Wykres funkcji liniowej')
    plt.xlabel('Wartości osi x')
    plt.ylabel('Wartości osi y')

    plt.scatter(list_x, list_y, linewidth=5, c=list_y, cmap=plt.cm.Reds)

plt.show()
