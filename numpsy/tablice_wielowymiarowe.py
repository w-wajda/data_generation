import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)

b = np.zeros((2, 3))
print(b)

c = np.ones((3, 4))
print(c)

d = np.random.random((2, 3))
print(d)

# Operacje na tablicach
print(a + b)
print(a - b)
print(a * b)
print(a ** 2)

# Funkcje sprawdzające rozmiar - spahe
print(a.shape)
print(b.shape)
print(c.shape)
print(d.shape)

# Funkcja transponująca - T
print(a.T)
print(d.T)

# Sprawdzenie wartości poszczególnych elementów i tworzenie maski
print(a > 3)
print(d > 1)

# Indeksowanie oraz przeglądanie tablic
print(a)
print(a[:1])
print(a[:1, 1:])

print('Pętle')

for x in a:
    print(x)
    for y in x:
        print(y)

for x in a.flat:
    print(x)

print([x for x in a if x[1] < 5])

print([x for x in a if x[1] < 6])



