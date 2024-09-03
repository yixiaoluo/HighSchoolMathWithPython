'''
函数的零点与方程的解
# y=f(x), find x to make y = 0 (zero)
函数零点存在定理
'''
import math

# page 143, example 1
# 求方程 lnx+2x-6=0 的实数解的个数。
# plot y = lnx+2x-6
import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return np.log(x) + 2*x - 6

x = np.linspace(0.1, 10, 400)

y = f(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y, label='y = ln(x) + 2x - 6')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of y = ln(x) + 2x - 6')
plt.grid(True)
plt.legend()
plt.show()

# 用二分法求方程的近似解 (bisection method)
# 已知函数f(x) = ln_x +2x - 6 在区间（2，3）内存在一个零点，求这个零点
def y(x):
    y = math.log(x, math.e) + 2* x - 6
    return y

def bisection_recursive(func, a, b, error_tolerance=1e-6, max_iter=100, iter_count=0):
    print(f"iter_count: {iter_count}")

    if func(a) * func(b) >= 0:
        raise ValueError("该方程在区间内存在0解")

    iter_count += 1
    c = (a + b) / 2.0

    if func(c) == 0 :
        print(f"发现解：{c} ")
        return c, iter_count
    if (b - a) / 2.0 < error_tolerance:
        print("区间过小，超过error_tolerance ")
        return c, iter_count
    if iter_count >= max_iter:
        print("迭代次数超过最大值 ")
        return c, iter_count

    if func(c) * func(a) < 0:
        print(f"func(c): {func(c)},func(a): {func(a)}")
        return bisection_recursive(func, a, c, error_tolerance, max_iter, iter_count)
    else:
        print(f"func(c): {func(c)},func(a): {func(a)}")
        return bisection_recursive(func, c, b, error_tolerance, max_iter, iter_count)


root, num_iter = bisection_recursive(func=y,
                                     a=2,
                                     b=3,
                                     max_iter=10)
# Print results
print(f"循环结束: x = {root}，共循环： {num_iter}.")

