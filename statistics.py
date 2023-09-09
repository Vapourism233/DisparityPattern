import cv2
import numpy as np
import matplotlib.pyplot as plt


def statictics():
    sum = 0
    color = ('blue', 'green', 'red')
    img = cv2.imread('/Users/apple/Desktop/BoschIntern/DisparityPattern/disparity.png')

    for i, color in enumerate(color):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    for i in range(len(hist)):
        sum += hist[i]
    for i in range(len(hist)):
        hist[i] = hist[i] / sum
    plt.plot(hist, color=color)
    plt.xlim([0, 256])
    plt.show()