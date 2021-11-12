import matplotlib.pyplot as plt
import numpsy as np

# Określenie wielkości i rozdzielczości
plt.figure(figsize=(10, 8), dpi=100)

# Określenie tytułu wykresu i opis etykiet
plt.title('Wykres y=x^2', color='red', size=20)
plt.xlabel('Oś x', color='red', size=15)
plt.ylabel('Oś y', color='red', size=15)

# Określenie układu współprzędnych
plt.axhline(y=0, color="blue")
plt.axvline(x=0, color="blue")

# Określenie parametrów
x = np.arange(-10, 10, 0.1)
y = x ** 2

# Wykres funkcji kwadratowej
plt.plot(x, y, color='yellow', linewidth=5)

plt.show()
