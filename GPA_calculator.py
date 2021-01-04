import numpy as np

grade_points=np.array([
    21,17,8,13,21,15,16,16,
    19,16,22,17,22
])

credits=10

points=18*40+20*12

points+=np.sum(grade_points*10)

total=credits*len(grade_points)

total+=40+20

print(points/total)