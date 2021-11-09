import matplotlib.pyplot as plt

list1x = [1, 2, 3, 4, 5]
list1 = [1, 4, 9, 16, 25]

list2x = [0, 2, 7, 9, 8]
list2 = [2, -7, 13, 17, -5]

plt.style.use('seaborn')

fig, ax = plt.subplots()

ax.scatter(list1x, list1, color='red', s=50)
ax.scatter(list2x, list2, color='yellow', s=50)

ax.set_title('Wykresy kropkowe', color='blue', size=15)
ax.set_xlabel('Wastość x', color='blue', size=10)
ax.set_ylabel('Wastość y', color='blue', size=10)

ax.tick_params(color='blue')

ax.axis([0, 10, -10, 30])

plt.show()
