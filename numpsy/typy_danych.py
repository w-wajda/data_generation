import numpy as np
from skimage import io
import matplotlib.pyplot as plt

# Tworzenie tablic
# Tablice jedno wymiarowe i typy danych
a = np.array([1, 2, 3, 4, 5])
print(a)
print(a.dtype)
print((a.itemsize))

b = np.arange(1, 10, 2)
print(b)

c = np.linspace(1, 10, 5)
print(c)

# Tablice wielo-wymiarowe
d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(d)
d_2 = np.array([[3, 5, 2, 6, 5], [4, 3, 9, 5, 4]])

e = np.zeros([3, 5])
print(e)

f = np.ones([2, 3])
print(f)

g = np.random.random([2, 3])
print(g)

# Podstawowe operacje na tablicach
print(d + d_2)
print(d - d_2)
print(d * d_2)
print(d ** 2)

# Sprawdzenie rozmiaru tablicy
print(a.shape)
print(d.shape)


# Funkcja transponująca
print(d.T)

print(c)
print(c > 3)

# Przeglądanie tablic
print(a)
print(a[0:2])
print(a[:2])
print(a[2:])
print(a[-1])
print(a[:-1])
h = np.array([[1, 2, 3], [4, 5, 6]])


print(h[:1, 1:])
print('Inne')
for x in h:
    print(x)
    for y in x:
        print(y)

print('Inny sposób')
for x in h:
    for y in x:
        print(y)

print('Jeszcze coś innego')
for x in h.flat:
    print(x)

print('Próba')
for x in h:
    if x[1] < 3:
        print(x)

# Funkcje wbudowane
print('Funkcje wbudowane')
print(h)
print(h.sum())
print(h.min())
print(h.max())
print(h.mean())

# Przetwarzanie obrazu
picture_www = 'http://analityk.edu.pl/wp-content/uploads/2020/01/fire.jpeg'

pic = np.array(io.imread(picture_www))
#plt.imshow(pic)
#plt.show()

# Obrocenie obrazu do góry nogami
# plt.imshow(pic[::-1])
# plt.show()

# Odbicie lustrzane
# plt.imshow(pic[:, ::-1])
# plt.show()

# Zbliżenie obrazu
# plt.imshow(pic[250:500, 150:600])
# plt.show()

# Zepsucie koloróœ
# plt.imshow(pic+100)
# plt.show()

# Wyodrębienie ognia
mask = pic[:, :, 0] < 200
pic[mask] = 255
plt.imshow(pic)
plt.show()
