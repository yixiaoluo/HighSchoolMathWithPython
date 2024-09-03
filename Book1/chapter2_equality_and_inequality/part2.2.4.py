import numpy as np

# 均值不等式
# 算数平均值
a = 2
b = 3
x = (a + b)/2
print(f"算数平均值: {x}")

# 几何平均值
a = 2
b = 3
x = np.sqrt(a * b)
print(f"几何平均值: {x}")

# 均值不等式
# (a+b)/2 >= np.sqrt(a *b)

# -------------------------------------
# page 76, example 1
# 已知x >0, 求 y = x + (1/x)的最小值，并说明x为何值时y取得最小值
from sympy import symbols, diff, solve
x = symbols('x')
y = x + 1/x
y_prime = diff(y, x)

# 找到使得导数为零的 x 值
critical_points = solve(y_prime, x)

# 打印临界点
print("Critical points:", critical_points)

# 计算在临界点的函数值
minimum_value = y.subs(x, critical_points[0])
print("Minimum value of y:", minimum_value)


# -------------------------------------
# page 78, example 3
# (1) 已知矩形的面积为100，则这个矩形的长、宽各为多少时，矩形的周长最短？
# length： x
# width： y
#  x * y = 100
#  min((x+y)/2)
#  max((x+y)/2)
from sympy import symbols, solve, diff

# 定义变量
x, y = symbols('x y')

# 约束条件
constraint = x * y - 100

# 表达式
expression = (x + y) / 2

# 解约束方程
y_expr = solve(constraint, y)[0]
print("y_expr")
print(y_expr)  # [100/x]

# 代入y的表达式
expression_sub = expression.subs(y, y_expr)

# 计算导数并找到极小值
expression_prime = diff(expression_sub, x)
critical_points = solve(expression_prime, x)
print("critical_points")
print(critical_points)  # Critical points: [-1, 1]


# 计算在临界点的值
value1 = expression_sub.subs(x, critical_points[0])
value2 = expression_sub.subs(x, critical_points[1])
print("x1:", value1) # -10
print("x2:", value2) # 10
# Critical points结果有两个: [-1, 1]， 但是因为矩形边长必须 > 0,
# 所以 x= -10 不满足题目要求
# 所以 x = 10, y = 100 / 10 = 10, 所以周长 =
# length = 2 * (x + y) = 2 * (10 + 10) = 40



# 检查x -> 0 和 x -> infinity 的情况
from sympy import limit, oo

limit_at_zero = limit(expression_sub, x, 0)
limit_at_infinity = limit(expression_sub, x, oo)

print("Limit of (x + y) / 2 as x -> 0:", limit_at_zero)
print("Limit of (x + y) / 2 as x -> infinity:", limit_at_infinity)



# (2) 已知矩形的周长为36，则这个矩形的长、宽各为多少时，矩形的面积最大？最大面积为多少？
# length： x
# width： y
#  if 2 * (x + y) = 36
#  what is max(x*y)?

"""
x + y = 18
y = 18 - x
P = x * y = x(18-x) = 18x - x^2
dp/dx = 18 - 2x = 0
x = 9
"""

from sympy import symbols, diff, solve
# 定义变量
x = symbols('x')

# 表达乘积函数
P = 18 * x - x**2

# 计算导数
P_prime = diff(P, x)

# 找到使得导数为零的 x 值
critical_points = solve(P_prime, x)
print(f"critical_points: {critical_points}") #[9]

# 只有一个导数为0的临界值

# 计算在临界点的函数值
max_x = critical_points[0]
max_y = 18 - max_x
max_product = P.subs(x, max_x)

print(f"x: {max_x}")
print(f"y: {max_y}")
print(f"矩形最大面积: {max_product}")
