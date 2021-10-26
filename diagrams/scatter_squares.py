import matplotlib.pyplot as plt

x_value = range(1, 6)
y_value = [x**2 for x in x_value]

plt.style.use('seaborn-darkgrid')
fig, ax = plt.subplots()

ax.scatter(x_value, y_value, c='yellow', s=50)

# Zdefiniowanie tytułu wykresu i etykiet osi
ax.set_title('Kwadraty liczb', c='blue', fontsize=24)
ax.set_xlabel('Wartość', c='blue', fontsize=14)
ax.set_ylabel('Kwadraty wartości', c='blue', fontsize=14)

# Zdefiniowanie wielkości etykiet
ax.tick_params(axis='both', which='major', labelsize=14)

# Zdefiniowanie automatycznego zapisu wykresu
plt.savefig('squares_scatter.png', bbox_inches='tight')
