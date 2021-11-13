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



