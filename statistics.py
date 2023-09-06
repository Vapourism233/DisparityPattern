import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('/Users/apple/Desktop/BoschIntern/DisparityPattern/disparity.png', 0)

width, height = img.shape
max_pixel = 255
img_save = np.zeros((width, height), dtype=np.float32)

for y in range(width):
    for x in range(height):
        pixel = img[y, x]
        percentage = (pixel / max_pixel) * 100
        img_save[y, x] = percentage

histogram, bin_edge = np.histogram(img_save, bins=101, range=(0, 100))

plt.figure(figsize=(10, 6))
plt.xlim(0, 255)

plt.ylim(0, 10000)
plt.bar(bin_edge[:-1], height, width=1, align="edge")
plt.show()

