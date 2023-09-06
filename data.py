from PIL import Image
import numpy as np
import cv2

img = np.array(Image.open(0.jpg).convert("L"))

color = np.where(img > 200)[0].shape[0]

pixel = img.shape[0] * img.shape[1]

print("Pixel number: {}").format(color)

gray = cv2.imread()
h, w = np.shape(gray)