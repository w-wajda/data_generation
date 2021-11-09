import matplotlib.pyplot as plt

list1x = [1, 2, 3, 4, 5]
list1 = [1, 4, 9, 16, 25]

list2x = [1, 2, 7, 9, 8]
list2 = [2, -7, 13, 17, -5]

plt.style.use('seaborn')

fig, ax = plt.subplots()

ax.plot(list1x, list1, linewidth=5, color='red')
ax.plot(list2x, list2, linewidth=5, color='yellow')

ax.set_title('Wykresy liniowe', size=15, color='blue')
ax.set_xlabel('Wartości x', size=10, color='blue')
ax.set_ylabel('Wartości y', size=10, color='blue')

ax.tick_params(axis='both', size=5, color='red')

ax.axis([0, 10, -10, 30])

plt.show()


