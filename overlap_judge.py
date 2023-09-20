import numpy as np


def generate_non_overlap_position(shape, shape_size, num, x_range, y_range):

    # shapeの中心座標
    position_set = []
    # 最初の1点をランダムにプロット
    x1,y1 = generate_random_point(x_range, y_range, shape_size)
    position_set.append([x1,y1])

    if shape == 'circle':
        for i in range(num-1):
            flag = True
            try_count = 0
            while flag:
                x,y = generate_random_point(x_range, y_range, shape_size)
                distance = []
                for j in range(i+1):
                    dis = (x - position_set[j][0])**2 + (y - position_set[j][1])**2
                    distance.append(dis)
                
                criteria = shape_size*2
                if distance_check(distance, criteria)==False:
                    flag = False
                    break                

                try_count += 1     
                if try_count>50:
                    print("cannot find suitable position.")
                    print("Please decrease the number of the object or the size of the object. ")
                    return "error"

            position_set.append([x,y])
        
    elif shape == 'triangle':
        for i in range(num-1):
            flag = True
            try_count = 0
            while flag:
                x,y = generate_random_point(x_range, y_range, shape_size)
                distance = []
                for j in range(i+1):
                    dis = (x - position_set[j][0])**2 + (y - position_set[j][1])**2
                    distance.append(dis)
                
                criteria = shape_size*2
                if distance_check(distance, criteria)==False:
                    flag = False
                    break                

                try_count += 1     
                if try_count>100:
                    print("cannot find suitable position.")
                    print("Please decrease the number of the object or the size of the object. ")
                    return "error"

            position_set.append([x,y])

    elif shape == 'rectangle':
        for i in range(num-1):
            flag = True
            try_count = 0
            while flag:
                x,y = generate_random_point(x_range, y_range, shape_size)
                distance = []
                for j in range(i+1):
                    dis = (x - position_set[j][0])**2 + (y - position_set[j][1])**2
                    distance.append(dis)
                
                criteria = (shape_size/2)*np.sqrt(2)
                if distance_check(distance, criteria)==False:
                    flag = False
                    break                

                try_count += 1     
                if try_count>50:
                    print("cannot find suitable position.")
                    print("Please decrease the number of the object or the size of the object. ")
                    return "error"

            position_set.append([x,y])

    return position_set


def generate_random_point(x_range, y_range, size):
    x = np.random.uniform(size/2, x_range-size/2)
    y = np.random.uniform(size/2, y_range-size/2)
    return x, y


def distance_check(distance, criteria):
    for i in range(len(distance)):
        if distance[i] < criteria:
            return True
    return False    


########################################################################################################################

def generate_overlap_position(shape, shape_size, num, x_range, y_range):
    position_set = []
    for _ in range(num):
        x,y = generate_random_point(x_range, y_range, shape_size)
        position_set.append([x,y])
    return position_set
