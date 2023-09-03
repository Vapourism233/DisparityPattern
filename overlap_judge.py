import cv2
import numpy as np
import math
from shapely.geometry import Polygon

def judge_rect_overlap(rect1, rect2):
    if len(rect1) or len(rect2) == 0:
        return False
    for rect in rect2:
        if (rect1[0] < rect[0] + rect[2] and rect1[0] + rect1[2] > rect[0] and
            rect1[1] < rect[1] + rect[3] and rect1[1] + rect1[3] > rect[1]):
            return True
    return False

def judge_circle_overlap(circle1, circle2):
    if len(circle1) or len(circle2) == 0:
        return False
    for circle in circle2:
        d = math.sqrt(abs(circle1[0] - circle[0])**2 + abs(circle1[1] - circle[1])**2)
        if(d < (circle1[2] + circle[2])):
            return True
    return False

def judge_triangle_overlap(tri1, tri2):
    if(len(tri1) == 0 or len(tri2) == 0):
        return False
    tri1 = Polygon(tri1)
    for tri in tri2:
        tri = Polygon(tri)
        if tri.intersects(tri1) or tri1.intersects(tri):
            return True
    return False

def triangle_get_point(x, y, size):
    # Calculate the height of the equilateral triangle
    height = size * 0.5
    width =  size * (np.sqrt(3) / 2)

    # Calculate the coordinates of the three vertices
    vertex1 = (x, y + size)
    vertex2 = (x + width, y - height)
    vertex3 = (x - width, y - height)

    return vertex1, vertex2, vertex3
