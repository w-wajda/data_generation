import numpy as np
from numpy import pi
import matplotlib.pyplot as plt

a = np.arange(15).reshape(3, 5)
print(a)
print(a.shape)

# Liczba osi
print(a.ndim)


b = np.arange(1, 16, 1)
print(b)
print(b.shape)
print(b.dtype)
print(b.ndim)
print(b.size)

c = np.array([1, 2, 3, 4])
print(c.dtype)

d = np.array([1.3, 5.3, 2.7])
print(d.dtype)

e = np.array([[1, 2], [3, 4]], dtype=complex)
print(e)

f = np.zeros((2, 3))
print(f)

g = np.ones((2, 3, 4), dtype=np.int16)
print(g)

h = np.empty((2, 3))
print(h)

i = np.arange(10, 35, 5)
print(i)

j = np.arange(1, 5, 0.3)
print(j)

k = np.linspace(1, 2, 9)
print(k)

x = np.linspace(0, 2 * pi, 20)
print(x)
y = np.sin(x)
print(y)
plt.plot(x, y)

m = np.arange(16).reshape(4, 4)
print(m)

n = np.arange(24).reshape(2, 3, 4)
print(n)

o = np.arange(10000).reshape(100, 100)
print(o)

p = np.array([20, 30, 40, 50])
r = 10 * np.sin(p)
plt.plot(p, r)
#plt.show()

print(p < 30)

rg = np.random.default_rng(1)
print(rg)

ro = np.ones(3, dtype=np.int32)
print(ro)

rj = np.exp(c * 1j)
print(rj)

ab = np.random.random((2, 3))
print(ab)

bb = np.arange(12).reshape(3, 4)
print(bb)
print(bb.sum())
print(bb.sum(axis=0))  # suma każdej kolumny
print(bb.min(axis=1))  # min każdego rzędu
print(bb.cumsum(axis=1))  # skumulowana suma w każdym wierszu

# Funcje uniwersalne
B = np.arange(3)
print(B)
print(np.exp(B))
print(np.sqrt(B))
C = np.array([2., -1., 4.])
print(C)
print(np.add(B, C))

# Indeksowanie
s = np.arange(10) ** 3
print(s)
print(s[2])
print(s[3:7])
s[:6:2] = 100  # od początku do pozycji 6, wyłączne, ustawienie co drugi element na 1000
print(s)
print(s[::-1])  # wyśietli odwrotną kolejność
for x in s:
    print(x ** (1/3.))


def f(x_1, y_1):
    return 10 * x_1 + y_1


fun = np.fromfunction(f, (4, 5), dtype=int)
print(fun)

print(fun[2, 3])  # wyciągnięcie liczby 23

print(fun[0:5, 1])  # każdy wiersz w drugiej kolumnie
print(fun[:, 1])  # można to zapisać w inny sposób
print(fun[1:3, 0:5])  # każda kolumna w drugim i trzecim rzędzie b
print(fun[1:3, :])  # można to zapisać w inny sposób
print(fun[-1])  # ostatni rząd. odpowiednik b[-1, :]

arr = np.array([2, 1, 5, 3, 7, 4, 6, 9])
print(arr.sum())
print(np.sort(arr))  # sortowanie w kolejności rosnącej

aa = np.array([1, 2, 3, 4])
bb = np.array([5, 6, 7, 8])

print(np.concatenate((aa, bb)))  # połącznie dwóch tablic w jedną

xx = np.array([[1, 2], [3, 4]])
yy = np.array([[5, 6]])

print(np.concatenate((xx, yy)))

array_example = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0, 1, 2, 3],
                           [4, 5, 6, 7]]])

print(array_example.ndim)  # liczba osi lub wymiar tablicy
print(array_example.size)  # całkowita liczba wszystkich elementów tablicy
print(array_example.shape)  # przedstawia kształt tablicy

aaa = np.arange(6)
print(aaa)
print(aaa.reshape(2, 3))  # zmiana kształtu tablicy
ccc = np.array([[0, 1, 2], [3, 4, 5]])
print(ccc)
print(ccc.reshape(6))

# dodatnie nowej osi do tablicy
z = np.array([1, 2, 3, 4, 5, 6])
print(z)
print(z.shape)
row_vector = z[np.newaxis, :]  # przekształcenie tablicy 1d na wektor wierszowy
print(row_vector.shape)
print(row_vector)
col_vector = z[:, np.newaxis]  # przekształcenie tabicy 1d na wektor kolumnowy

nowe_a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# wartości w tablicy, które są mniejsze niż 5.
print(nowe_a[nowe_a < 5])
# liczby równe lub większe niż 5
five_up = (nowe_a >= 5)
print(nowe_a[five_up])
#  elementy, które są podzielne przez 2
divisible_by_2 = nowe_a[nowe_a % 2 == 0]
print(divisible_by_2)
# elementy, które spełniają dwa warunki wieksze od 2 i mniejsze od 11
ddd = nowe_a[(nowe_a > 2) & (nowe_a < 11)]
print(ddd)

# stworzenie tablicy z istaniejących już tablic
a1 = np.array([[1, 1],
               [2, 2]])

a2 = np.array([[3, 3],
               [4, 4]])

# połącznie w pionie
a3 = np.vstack((a1, a2))
print(a3)
# połącznie w poziomie
a4 = np.hstack((a1, a2))
print(a4)
# podzielenie tablicy na kilka mniejszych
a5 = np.arange(1, 25).reshape(2, 12)
print(a5)
a6 = np.hsplit(a5, 3)  # podzielenie tablicy na trzy tablice o jednakowych kształtach
print(a6)
a7 = np.hsplit(a5, (3, 4))  # podzielenie tablicy po trzeciej i czwartej kolumnie
print(a7)

# unikalne przemdioty i liczby
a8 = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])
unique_values = np.unique(a8)
print(unique_values)
a_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [1, 2, 3, 4]])
unique_number = np.unique(a_2d)
print(unique_number)

# odwrócenie tablicy
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
reversed_arr = np.flip(arr)
print(reversed_arr)
# odwrócenie tablicy 2d
arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
reveesed_arr2 = np.flip(arr_2d)
print(reveesed_arr2)
# odwrócić rzędy
reversed_arr_rows = np.flip(arr_2d, axis=0)
# odwrócić kolumny
reversed_arr_columns = np.flip(arr_2d, axis=1)
# odwrócić zawartość tylko jednej kolumny lub wiersza
arr_2d[1] = np.flip(arr_2d[1])
print(arr_2d)

# przekształcenie i spłaszczenie tablic wielowymiarowych
xxx = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# flatten do spłaszczenia tablicy w tablicę 1D
print(xxx.flatten())
# ravel, zmiany wprowadzone w nowej tablicy wpłyną na tablicę nadrzędną
axxx = xxx.ravel()
print(axxx)

# prace ze wzorami matematycznymi
# formuła błędu średniokwadratowego
prediction = np.array(1, 1, 1)
labels = np.array(1, 2, 3)
n = 3
error = (1/n) * np.sum(np.square(prediction - labels))
