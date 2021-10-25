import matplotlib.pyplot as plt

x_value = range(1, 1001)
y_value = [x**2 for x in x_value]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_value, y_value, c=(0, 0.8, 0), s=10)

# Zdefiniowanie tytułu wykresu i etykiet osi
ax.set_title('Kwadraty liczb', fontsize=24)
ax.set_xlabel('Wartość', fontsize=14)
ax.set_ylabel('Kwadraty wartości', fontsize=14)

# Zdefiniowanie wielkości etykiet
ax.tick_params(axis='both', which='major', labelsize=14)

# Zdefiniowanie zakresu dla każdej osi
ax.axis([0, 1100, 0, 1100000])

plt.savefig('squares_plot.png', bbox_inches='tight')
