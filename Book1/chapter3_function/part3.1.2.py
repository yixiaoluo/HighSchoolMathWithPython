# 函数的单调性

# page 101, example 1
# 求证：函数f(x) = -2 * x 在R上是减函数．
import matplotlib.pyplot as plt
import numpy as np

# 定义函数
def f(x):
    return -2 * x

# 创建x值范围
x_values = np.linspace(-10, 10, 400)
y_values = f(x_values)

# 创建图形
plt.figure(figsize=(10, 6))

# 绘制函数
plt.plot(x_values, y_values, label='f(x) = -2x')

# 设置标题和标签
plt.title('Function f(x) = -2x')
plt.xlabel('x')
plt.ylabel('f(x)')

# 添加网格
plt.grid(True)

# 添加图例
plt.legend()

# 显示图形
plt.show()


# ------------------------
# page 101, example 2
# 判断函数f(x) = 3 * x + 5, x 属于[-1, 6]的单调性，并求这个函数的最值
import matplotlib.pyplot as plt
import numpy as np

# 定义函数
def f(x):
    return 3 * x + 5

# 创建x值范围
x_values = np.linspace(-1, 6, 400)
y_values = f(x_values)

# 创建图形
plt.figure(figsize=(10, 6))

# 绘制函数
plt.plot(x_values, y_values, label='f(x) = 3x + 5')

# 设置标题和标签
plt.title('Function f(x) = 3x + 5, x in [-1, 6]')
plt.xlabel('x')
plt.ylabel('f(x)')

# 添加网格
plt.grid(True)

# 添加图例
plt.legend()

# 显示图形
plt.show()


# -------------------------------------------------------
# 函数的平均变化率
# 平面直角坐标系中两个点A(x1,x2),B(y1,y2)，直线AB的斜率是
# slope = (y2-y1) / (x2-x1)