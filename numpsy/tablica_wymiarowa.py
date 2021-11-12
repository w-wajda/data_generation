import numpy as np

# Tablice jedno-wymiarowe
a = np.array([1, 2, 3, 4, 5])
print(a)
a_2 = np.array([4, 7, 1, 6, 7])
print(a_2)

b = np.arange(10)
print(b)

c = np.arange(0, 10, 2)
print(c)

d = np.linspace(0, 10, 6)
print(d)

# Operacje na tablicach
print(a + a_2)
print(a - a_2)
print(a * a_2)
print(a ** 2)

# Funkcja sprawdzająca rozmiar - shape
print(a.shape)
print(b.shape)
print(c.shape)
print(d.shape)

# Funkcje transponujące - T
print(a.T)
print(d.T)

# Sprawdzenie wartości poszczególnych elementów i tworzenie maski
print(c > 3)
print(a > 2)

# Indeksowanie oraz przeglądanie tablic
print(a)
print(a[2:])
print(a[:1])

for x in a:
    print(x)

