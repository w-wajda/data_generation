import matplotlib.pyplot as plt

from walk_random.random_walk import RandomWalk

# Tworzenie nowego błądzenia losowego, dopóki program pozostaje aktywny
while True:
    # Przygotowanie danych błądzenia losowego i wyświetlenia puntów
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Wyświetlenie punktów błądzenia losowego
    plt.style.use('classic')
    fig, ax = plt.subplots()

    ax.plot(rw.x_values, rw.y_values, c='yellow', linewidth=3)

    # Podkreślenie pierwszego i ostatniego błądzenia losowego
    ax.scatter(0, 0, c='blue', edgecolor='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100)

    # Ukrycie osi
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Create another random walk? (yes/no): ")
    if keep_running == 'no':
        break
