from bladzenie_losowe import RandomWalk
import matplotlib.pyplot as plt

plt.style.use('classic')

plt.title('Błądzenie losowe', size=15)

# Tworzenie błądzenia losowego dopóki program pozostaje aktywny
while True:
    # Przygotowanie danych bładzenia losowego i wyświetlenie punktów
    bl = RandomWalk(30000)
    bl.walk()
    bl2 = RandomWalk(30000)
    bl2.walk()
    bl3 = RandomWalk(30000)
    bl3.walk()

    # Wyświetlenie punktów błądzenia losowego
    punkt = range(bl.number_points)
    plt.scatter(bl.x_value, bl.y_value, c=punkt, cmap=plt.cm.Blues, edgecolors='none', s=1)
    plt.scatter(bl2.x_value, bl2.y_value, c=punkt, cmap=plt.cm.Reds, edgecolors='none', s=1)
    plt.scatter(bl3.x_value, bl3.y_value, c=punkt, cmap=plt.cm.Greens, edgecolors='none', s=1)

    plt.show()

    kolejne_losowanie = input('Czy kolejne losowanie? (y/n): ')
    if kolejne_losowanie == 'n':
        break


