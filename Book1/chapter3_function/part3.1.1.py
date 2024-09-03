x = 1

# 正比例函数
y = 2 * x
# 一次函数
y = -3 * x - 1
# 反比例函数
y = -(2 / x)
# 二次函数
y = x **2 + 2 * x - 3

# 定义变量的域
# https://geek-docs.com/sympy/sympy-questions/53_sympy_sympy_define_domain_of_variable.html


from sympy import symbols
# 定义一个整数变量
x = symbols('x', domain='Z')
# 定义一个有理数变量
y = symbols('y', domain='Q')
# 定义一个实数变量
z = symbols('z', domain='R')


# --------------------------------------------
# todo: 学一下画图包 matplotlib
# page 94
# 画函数图像y = -x + 1
import matplotlib.pyplot as plt
import numpy as np

# 定义 x 的范围
x = np.linspace(-10, 10, 400)

# 定义 y = -x + 1
y = -x + 1

plt.figure(figsize=(8, 6))

# 画图
plt.plot(x, y, label='y = -x + 1', color='b')

plt.title('plot y = -x + 1')
plt.xlabel('x')
plt.ylabel('y')

# 显示网格
plt.grid(True)

# 显示图例
plt.legend()

# 显示图像
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.show()


# --------------------------------------------
# page 94， example 4, 分段函数
def water_fee(x):
    if 0 <= x <= 180:
        y = 5 * x
    if 180 < x <= 260:
        y = 7 * x - 360
    return y

# 定义 x 的范围
x1 = np.linspace(0, 180, 1000)
x2 = np.linspace(180.01, 260, 1000)


y1 = 5 * x1
y2 = 7 * x2 - 360

plt.figure(figsize=(10, 6))
plt.plot(x1, y1, label='y = 5x (0 ≤ x ≤ 180)', color='b')
plt.plot(x2, y2, label='y = 7x - 360 (180 < x ≤ 260)', color='r')

# 添加x轴和y轴
plt.xlabel('x')
plt.ylabel('y')

plt.grid(True)

plt.legend()
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.show()


# --------------------------------------------
# page 95， example 5, 分段函数画图
# 当 n属于整数，当x属于[n, n-1)，y = n
import matplotlib.pyplot as plt
import numpy as np

# 定义函数
def example5(x):
    return np.floor(x).astype(int)

# 创建x值范围
x_values = np.linspace(-5, 5, 1000)
y_values = example5(x_values)

# 创建图形
plt.figure(figsize=(10, 6))

# 绘制函数
plt.step(x_values, y_values, where='post', label='y = n for x in [n, n+1)')

# 设置标题和标签
plt.title(' y = n for x in [n, n+1)')
plt.xlabel('x')
plt.ylabel('y')

plt.grid(True)
plt.legend()
plt.show()


# --------------------------------------------
# page 96, example 8
# 已知 f(x) = x^2, 求 f(x-1)
# f(x-1) = (x-1) ^ 2 = x^2 - 2x + 1
def example_8(x):
    y = x * x
    return y

def example_8_b(x):
    y = x * x - 2* x + 1
    return y

x = 0
print(example_8(x - 1))
print(example_8_b(x))
x = 1
print(example_8(x - 1))
print(example_8_b(x))
x = 2
print(example_8(x - 1))
print(example_8_b(x))
