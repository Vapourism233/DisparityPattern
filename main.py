import os
import numpy as np
import datetime
import overlap_judge
from generate_objects import GenerateObject
import generate_objects


output_directory = '.' 

# 現在の日付と時間を取得
current_datetime = datetime.datetime.now()
date_str = current_datetime.strftime('%Y-%m-%d')
time_str = current_datetime.strftime('%H-%M-%S')


if __name__ == '__main__':

    WIDTH, HEIGHT = 21, 29.7  # A4
    X_RANGE, Y_RANGE = 21, 29.7 
    SEED = 42 


    """変更箇所 start"""
    SHAPE_TYPE = "rectangle"   # 図形の選択
    NUM = 200  # 図形の目安個数(OVERLAP=Falseのときは描けない場合あり)
    SHAPE_SIZE = 0.5  # 図形のサイズ
    PATTERN_COLOR = "black"  # パターンの色
    BG_COLOR = "gray"  # 背景の色
    ROTATION_MIN = 0  # 回転の最小値 (deg)
    ROTATION_MAX = 90  # 回転の最大値 (deg)

    ROTATION = False  # 回転する: True, 回転しない: False
    SIZE = False  # ランダムにサイズ変更: True, サイズ一定: False
    OVERLAP = False  # patternが重ねる: True, 重ならない: False
    GRID = True
    """変更箇所 end"""

    np.random.seed(SEED)  # 乱数のseedを固定
    main_object = GenerateObject(width=WIDTH, height=HEIGHT)  # 図形オブジェクトの作成

    if OVERLAP:
        position_set = overlap_judge.generate_overlap_position(SHAPE_TYPE, SHAPE_SIZE, NUM, X_RANGE, Y_RANGE)

    else:
        position_set = overlap_judge.generate_non_overlap_position(SHAPE_TYPE, SHAPE_SIZE, NUM, X_RANGE, Y_RANGE)


    if SIZE:
        for i in range(NUM):
            if ROTATION:
                angle = np.random.uniform(ROTATION_MIN, ROTATION_MAX)  # 図形の回転を一様分布から生成
            else:
                angle = 0
            
            if SHAPE_TYPE == "circle":
                size = generate_objects.generate_random_size(SHAPE_SIZE, SHAPE_TYPE)  # 図形のサイズを一様分布から生成
                main_object.add_shape(shape_type="circle", size=size, position=(position_set[i][0], position_set[i][1]), color=PATTERN_COLOR, angle=angle)

            elif SHAPE_TYPE == "triangle":
                size = generate_objects.generate_random_size(SHAPE_SIZE, SHAPE_TYPE)  # 図形のサイズを一様分布から生成
                main_object.add_shape(shape_type="triangle", size=size, position=(position_set[i][0], position_set[i][1]), color=PATTERN_COLOR, angle=angle)

            elif SHAPE_TYPE == "rectangle":
                s_width, s_height = generate_objects.generate_random_size(SHAPE_SIZE, SHAPE_TYPE)  # 図形のサイズを一様分布から生成
                main_object.add_shape(shape_type="rectangle", size=(s_width, s_height), position=(position_set[i][0], position_set[i][1]), color=PATTERN_COLOR, angle=angle)

    
    else: 
        for i in range(NUM):
            if ROTATION:
                angle = np.random.uniform(ROTATION_MIN, ROTATION_MAX)  # 図形の回転を一様分布から生成
            else:
                angle = 0

            if SHAPE_TYPE == "circle":
                size = SHAPE_SIZE
                main_object.add_shape(shape_type="circle", size=size, position=(position_set[i][0], position_set[i][1]), color=PATTERN_COLOR, angle=angle)
                    
            elif SHAPE_TYPE == "triangle":
                size = SHAPE_SIZE
                main_object.add_shape(shape_type="triangle", size=size, position=(position_set[i][0], position_set[i][1]), color=PATTERN_COLOR, angle=angle)

            elif SHAPE_TYPE == "rectangle":
                s_width, s_height = SHAPE_SIZE, SHAPE_SIZE
                main_object.add_shape(shape_type="rectangle", size=(s_width, s_height), position=(position_set[i][0], position_set[i][1]), color=PATTERN_COLOR, angle=angle)


    # フォルダ名を生成
    output_name = f'{SHAPE_TYPE}_num-{NUM}_size-{SHAPE_SIZE}_p-{PATTERN_COLOR}_bg-{BG_COLOR}_sizerand-{SIZE}_rotationrand-{ROTATION}_{date_str}_{time_str}.png'
    # 保存先の絶対パスを生成
    folder_path = os.path.join(output_directory, output_name)

    # 生成パターンの保存
    main_object.draw(BG_COLOR, folder_path)

