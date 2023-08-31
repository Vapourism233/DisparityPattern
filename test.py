import numpy as np
import cv2 
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def pltShow(xx, yy, num):

    z = np.random.random(size=[xx.size, num])
    x = (z / sum(z)).T.dot(xx)
    y = (z / sum(z)).T.dot(yy)
    print(x, y)

    fig = plt.figure()
    ax1 = fig.add_subplot(111, aspect='equal')
    plt.xlim(0, 1000)
    plt.ylim(0, 1000)
    for i in range(x.size):
        ax1.add_patch(patches.Rectangle(
            (x[i], y[i]),
            10,
            10,
            )
        )
    plt.show()

def genPolygon(n):
    
    x = np.random.randint(1, 1000, n)
    y = np.random.randint(1, 1000, n)

    return x, y

if __name__ == '__main__':
    
    x, y = genPolygon(4)
    pltShow(x, y, 1000)

