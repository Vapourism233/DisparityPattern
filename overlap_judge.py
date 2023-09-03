import cv2
import numpy as np

def judge_rect_overlap(rect1, rect2):
    for rect in rect2:
        if (rect1[0] < rect[0] + rect[2] and rect1[0] + rect1[2] > rect[0] and
            rect1[1] < rect[1] + rect[3] and rect1[1] + rect1[3] > rect[1]):
            return True
    return False