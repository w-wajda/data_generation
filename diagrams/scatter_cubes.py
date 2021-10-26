import matplotlib.pyplot as plt

plt.style.use('seaborn')

x_cubes = range(1, 5000)
y_cubes = [x**3 for x in x_cubes]

fig, ax = plt.subplots()
ax.scatter(x_cubes, y_cubes, c=y_cubes, cmap=plt.cm.Reds, s=100)

# Zdefiniowanie tytułu wykresu i etykiet osi
ax.set_title('Sześcian liczb', c='blue', size=25)
ax.set_xlabel('Wartość', c='blue', size=20)
ax.set_ylabel('Sześcian wartości', c='blue', size=20)

# Zdefiniowanie opisu osi
ax.tick_params(axis='both', size=5, color='blue')

# Zdefiniowanie zakresu osi
ax.axis([0, 5250, 0, 130000000000])

plt.savefig('cube_scatter.png', bbox_inches='tight')

