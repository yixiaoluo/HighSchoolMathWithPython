'''
    同角三角函数的关系
    sin(x)^2 + cos(x)^2 = 1
    sin(x) / cos(x) = tan(x)
'''
import numpy as np

# page 183, example 6
# 已知sin(x) = -3/5, 求cos(x),tan(x)
sin_x = -3/5
cos_x = np.square(1-sin_x**2)
print(cos_x)


