import matplotlib.pyplot as plt
import numpsy as np

plt.title('Funkcja kwadratowa', c='red', size=15)
plt.xlabel('Wartość x', c='red', size=15)
plt.ylabel('Wartość y', c='red', size=15)

plt.axvline(x=0, c='black')
plt.axhline(y=0, c='black')

plt.tick_params(axis='both', color='red', size=5)

a = 1,
b = -3,
c = 1
arg_x = np.arange(-10, 10, 1)
fun_y = a * (arg_x ** 2) + b * arg_x + c

plt.plot(arg_x, fun_y, c='green', linewidth=5)
plt.legend(['f(x)=ax^2 + bx + c'], loc="upper left")

plt.show()
