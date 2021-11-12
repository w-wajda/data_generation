# Ruchy Browna
import numpsy as np
import random
import matplotlib.pyplot as plt

n = int(input('Ile ruchów: '))
x = y = 0
lx = [0]
ly = [0]

for i in range(0, n):
    rad = float(random.randint(0, 360)) * np.pi / 180
    x = x + np.cos(rad)  # wyliczenie współrzędnej x
    y = y + np.sin(rad)  # wyliczenie współrzędnej y

    lx.append(x)
    ly.append(y)

# obliczenie wektora końcowego przesunięcia
s = np.fabs(np.sqrt(x ** 2 + y ** 2))
print(f'Wektor przesunięcia: {s}')

plt.plot(lx, ly, "o:", color="green", linewidth=3, alpha=0.5)
plt.legend([f'Dane x, y \nPrzemieszczenie: {s}'], loc="upper left")
plt.title("Ruchy Browna", color='blue', size=15)
plt.xlabel("Współrzędne x", color='blue', size=10)
plt.ylabel("Współrzędne y", color='blue', size=10)

plt.show()
