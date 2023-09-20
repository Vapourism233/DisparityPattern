import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle as MatplotlibRectangle, RegularPolygon


class GenerateObject:

    # A4サイズ, 図形の初期化
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.shapes = []

    # 図形の設定
    def add_shape(self, shape_type, size, position, color, angle):
        if shape_type == "circle":
            self.shapes.append({"type": "circle", 
                                "size": size, 
                                "position": position, 
                                "color": color, 
                                "angle": angle})
            
        elif shape_type == "triangle":
            self.shapes.append({"type": "triangle", 
                                "size": size, 
                                "position": position, 
                                "color": color, 
                                "angle": angle})
            
        elif shape_type == "rectangle":
            self.shapes.append({"type": "rectangle", 
                                "size": size, 
                                "position": position, 
                                "color": color, 
                                "angle": angle})
        else:
            print("Unsupported shape type")

    # 図形の描画
    def draw(self, background_color, output_path):
        fig, ax = plt.subplots(figsize=(self.width, self.height), dpi=100)
        fig.set_facecolor(background_color)  # 背景色の設定
        ax.set_xlim(0, self.width)
        ax.set_ylim(0, self.height)
        ax.axis("off")

        for shape in self.shapes:
            shape_type = shape["type"]
            size = shape["size"]
            position = shape["position"]
            color = shape["color"]
            angle = shape["angle"]

            if shape_type == "circle":
                circle = Circle(position, size, color=color)
                ax.add_patch(circle)

            elif shape_type == "triangle":
                triangle = RegularPolygon(position, numVertices=3, radius=size, orientation=angle, color=color)  # numVerticesを変えることで正三角形, 正方形, 正五角形...と変更できる
                ax.add_patch(triangle)

            elif shape_type == "rectangle":
                rect = MatplotlibRectangle((position[0] - size[0]/2, position[1] - size[1]/2), 
                                           size[0], 
                                           size[1], 
                                           angle = angle, 
                                           color=color, 
                                           rotation_point=position)
                ax.add_patch(rect)

        plt.gca().set_aspect('equal', adjustable='box')
        save_and_show_graph(output_path)


def generate_random_size(size, shape_type):
    if shape_type == "circle": 
        s = np.random.uniform(0, size)
        return s
    elif shape_type == "triangle":
        s = np.random.uniform(0, size)
        return s
    elif shape_type == "rectangle":
        s_width = np.random.uniform(0, size)
        s_height = np.random.uniform(0, size)
        return s_width, s_height
    else:
        return "Unsupported shape type"


def save_and_show_graph(output_path):
    plt.savefig(output_path)
