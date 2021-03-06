import matplotlib.pyplot as plt

from walk_random.random_walk import RandomWalk

# Tworzenie nowego błądzenia losowego, dopóki program pozostaje aktywny
while True:
    # Przygotowanie danych błądzenia losowego i wyświetlenia puntów
    rw = RandomWalk(30000)
    rw.fill_walk()

    # Wyświetlenie punktów błądzenia losowego i wielkość wygenerowanego wykresu
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(16, 10), dpi=128)

    # Przypisanie koloru zgodnie z położeniem w błądzeniu losowym
    point_numbers = range(rw.num_points)

    # Użycie mapu kolorów Reds oraz argumentu edgecolor, by pozbyć się kontur wokół każdego punktu
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Reds, edgecolor='none', s=1)

    # Podkreślenie pierwszego i ostatniego błądzenia losowego
    ax.scatter(0, 0, c='yellow', edgecolor='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='blue', edgecolor='none', s=100)

    # Ukrycie osi
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Create another random walk? (y/n): ")
    if keep_running == 'n':
        break





