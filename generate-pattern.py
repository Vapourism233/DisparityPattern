import matplotlib.pyplot as plt
import numpy as np


def generate_random_circle(radius, x_range, y_range):
    center_x = np.random.uniform(radius, x_range - radius)
    center_y = np.random.uniform(radius, y_range - radius)
    return center_x, center_y

def circles_do_not_overlap(circles, new_circle, min_distance):
    for circle in circles:
        distance = np.sqrt((circle[0] - new_circle[0]) ** 2 + (circle[1] - new_circle[1]) ** 2)
        if distance < min_distance:
            return False
    return True

def generate_random_non_overlapping_circles(num_circles, radius, x_range, y_range, min_distance):
    circles = []
    for _ in range(num_circles):
        while True:
            new_circle = generate_random_circle(radius, x_range, y_range)
            if circles_do_not_overlap(circles, new_circle, min_distance):
                circles.append(new_circle)
                break
    return circles

def plot_circles_in_rectangle(circles, rectangle_width, rectangle_height):
    fig, ax = plt.subplots()
    ax.set_xlim(0, rectangle_width)
    ax.set_ylim(0, rectangle_height)
    for circle in circles:
        circle_patch = plt.Circle(circle, radius, color='b', fill=False)
        ax.add_patch(circle_patch)
    ax.set_aspect('equal', 'box')
    plt.show()

rectangle_width = 10
rectangle_height = 8
num_circles = 100
radius = 0.3
min_distance = 2 * radius

circles = generate_random_non_overlapping_circles(num_circles, radius, rectangle_width, rectangle_height, min_distance)
plot_circles_in_rectangle(circles, rectangle_width, rectangle_height)
