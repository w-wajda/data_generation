from skimage import io
import matplotlib.pyplot as plt
import numpy as np

picture = np.array(io.imread('http://analityk.edu.pl/wp-content/uploads/2020/01/fire.jpeg'))
mask = picture[:, :, 0] < 200
picture[mask] = 255
plt.imshow(picture)
plt.show()


