import matplotlib.pyplot as plt

plt.style.use('seaborn')

x_cubs = range(1, 6)
y_cubs = [x ** 3 for x in x_cubs]

fig, ax = plt.subplots()
ax.plot(x_cubs, y_cubs, linewidth=3)

# Zdefiniowanie tytułu wykresu i etykiet osi
ax.set_title('Sześcian liczb', c='red', size=25)
ax.set_xlabel('Wartość', c='red', size=20)
ax.set_ylabel('Sześcian wartości', c='red', size=20)

# Zdefiniowanie wielkości etykiet
ax.tick_params(axis='both', color='red', size=5)

# Zdefiniowanie zakresu osi
ax.axis([0, 6, 0, 140])

plt.show()
