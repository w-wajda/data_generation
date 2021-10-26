import matplotlib.pyplot as plt

input_value = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn-darkgrid')
fig, ax = plt.subplots()

ax.plot(input_value, squares, c='yellow', linewidth=3)

# Zdefiniowanie tytułu wykresu i etykiet osi
ax.set_title('Kwadraty liczb', c='red', fontsize=25)
ax.set_xlabel('Wartość', c='red', fontsize=15)
ax.set_ylabel('Kwadraty wartości', c='red', fontsize=15)

# Zdefiniowanie wartości etykiet
ax.tick_params(axis='both', labelsize=12)

# Zdefiniowanie zakresu dla każdej osi
ax.axis([0, 6, 0, 30])

plt.show()
