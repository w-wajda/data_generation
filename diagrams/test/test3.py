import matplotlib.pyplot as plt

listx = range(100)
listy = [x**2 for x in listx]

list2x = range(25)
list2y = [x**3 for x in list2x]

fig, ax = plt.subplots()

ax.scatter(listx, listy, c=listx, cmap=plt.cm.Blues, s=20)
ax.scatter(list2x, list2y, c=list2x, cmap=plt.cm.Reds, s=20)

ax.set_title('Przykładowe wykresy', c='red', size=15)
ax.set_xlabel('Wartość x', c='red', size=10)
ax.set_ylabel('Wartość y', c='red', size=10)

ax.tick_params(color='red', size=5)
ax.axis([0, 110, 0, 16000])

plt.show()
