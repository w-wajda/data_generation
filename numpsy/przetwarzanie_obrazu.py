import numpy as np
from skimage import io
import matplotlib.pyplot as plt

pic = np.array(io.imread('http://analityk.edu.pl/wp-content/uploads/2020/01/fire.jpeg'))

plt.title('Smochód w ogniu')
#plt.imshow(pic)
#plt.show()

# Obrócenie obrazu
#plt.imshow(pic[::-1])
#plt.show()

# Odbicie lustrzane
#plt.imshow(pic[:, ::-1])
#plt.show()

# Zbliżenie samochodu
#plt.imshow(pic[300:450, 150:600])
#plt.show()

# Pomieszanie kolorów
plt.imshow(pic + 100)
plt.show()