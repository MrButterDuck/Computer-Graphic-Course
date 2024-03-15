from PIL import Image
import numpy as np
import numba


@numba.njit(fastmath = True)
def LUT_negative(image: np.ndarray):
    h, w, c = image.shape
    for x in range(w):
        for y in range(h):
            for l in range(c):
                image[y, x, l] = 1 - image[y, x, l]
    return image

@numba.njit(fastmath = True)
def LUT_gamma(image: np.ndarray, gamma):
    h, w, c = image.shape
    for x in range(w):
        for y in range(h):
            for l in range(c):
                image[y, x, l] = image[y, x, l] ** (1 / gamma)
    return image

img = Image.open('D:\Python files\Computer Graphic Course\\task2\shrek.png').convert('HSV')
img_arr = np.array(img) / 255
new_image = Image.fromarray(np.uint8(LUT_negative(img_arr) * 255))
new_image = Image.fromarray(np.uint8(LUT_gamma(img_arr, 3) * 255))
new_image.show()