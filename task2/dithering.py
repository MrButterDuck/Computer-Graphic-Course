from PIL import Image
import numpy as np
import numba

@numba.njit(fastmath=True)
def dithering(image: np.ndarray):
    height, width = image.shape
    for x in range(width):
        for y in range(height):
            old = image[y, x]
            new = np.round(old)
            image[y, x] = new
            error = old - new

            if x + 1 < width:
                image[y, x + 1] += error * ( 7 / 16)
            if y + 1 < height:
                 image[y + 1, x] += error * (5/ 16)
            if (x + 1 < width) and (y + 1 < height):
                 image[y + 1, x + 1] += error * (1/ 16)
            if (x - 1 >= 0) and (y + 1 < height):
                 image[y + 1, x - 1] += error * (3 / 16)
    return image  


img = Image.open('D:\Python files\Computer Graphic Course\\task2\shrek.png').convert('L')
img_arr = np.array(img) / 255
new_image = Image.fromarray((dithering(img_arr) * 255))
new_image.show()
