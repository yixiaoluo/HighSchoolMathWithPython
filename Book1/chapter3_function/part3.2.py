# 函数的零点
# 如果函数y=f(x)在实数a处的函数值等于零，则称a为函数的零点

# 二次函数的零点及其与对应方程、不等式解集之间的关系
# 求不等式的解集
# (1) x^2-x-6<0
# (1) x^2-x-6>=0
# 3 和 -2 是函数的零点

# plot y = x^2-x-6
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x ** 2 - x - 6


x_values_f = np.linspace(-5, 5, 400)
x_values_f = x_values_f[x_values_f != 0]

# Generate y values for g(x)
y_f = f(x_values_f)

# Plot g(x) = 1/x
plt.figure(figsize=(8, 6))
plt.plot(x_values_f, y_f, label='f(x) =  x^2-x-6', color='green')
plt.axhline(y=0, color='black', linewidth=0.5)  # x-axis
plt.axvline(x=0, color='black', linewidth=0.5)  # y-axis
plt.title('Plot of g(x) = x^2-x-6')
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(-10, 10)  # Set y-axis limits to avoid infinite values
plt.grid(True)
plt.legend()
plt.show()

# ------------------------
# page 122, example 6
# 求证： 函数f(x) = x**3-2x+2至少有一个零点
# 一种解法是二分法：求函数零点近似值
# 二分法英文是：Bisection Method
"""
f(x) = x**3 - 2x + 2
f(0) = 2 > 0
f(-2) = -2 < 0
use program to find a number between 0 and -2 to satisfy f(x) = 0
"""


def f(x):
    return x ** 3 - 2 * x + 2


def bisection_method(f, a, b, tolerance=1e-8, max_iterations=100):
    iteration = 0
    while iteration < max_iterations:
        c = (a + b) / 2
        if abs(f(c)) < tolerance:
            print(f"误差范围内的解存在： x = {c}，当前迭代次数： {iteration}.")
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iteration += 1

    print("达到最大迭代次数，没有发现解.")
    return None


# Define the initial interval [a, b]
a = 0
b = -2

answer = bisection_method(f, a, b)
if answer is not None:
    print(f"f({answer}) = {f(answer)}")

# page 124, 拓展阅读： 二分法在搜索中的应用
# 给出15个按从小到大排列的数列
# 随机给出一个不大于100的自然数x，让计算机查找x是否在这个数列中，需要在指定步骤内完成
# 用二分法，每次都和数列正中间的数进行比大小，缩小位置的可能性
l = [2, 5, 8, 11, 12, 16, 23, 27, 29, 35, 51, 53, 69, 75, 77]


def binary_search(list_in, x):
    left_index = 0
    right_index = len(list_in) - 1

    iter = 0
    while left_index <= right_index:
        print(f"迭代次数: {iter}")
        print(f"left_index: {left_index}")
        print(f"right_index: {right_index}")
        mid_index = (left_index + right_index) // 2
        iter += 1
        if list_in[mid_index] == x:
            return True  # 找到了 x，返回 True
        elif list_in[mid_index] < x:
            left_index = mid_index + 1  # x 在右半部分，更新左边界
        else:
            right_index = mid_index - 1  # x 在左半部分，更新右边界

    return False  # 没找到 x，返回 False


# 给定的已排序数列
l = [2, 5, 8, 11, 12, 16, 23, 27, 29, 35, 51, 53, 69, 75, 77]
x = 5
# 使用二分法查找 x 是否在数列 l 中
found = binary_search(l, x)

"""
输出：
迭代次数: 0
left_index: 0
right_index: 14
迭代次数: 1
left_index: 0
right_index: 6
迭代次数: 2
left_index: 0
right_index: 2
"""
