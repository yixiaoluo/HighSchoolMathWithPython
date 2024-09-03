# 不等式的解集
# https://deepinout.com/sympy/sympy-questions/185_sympy_solving_inequalities_in_sympy.html


# page 68, example 1, solve the following:
# 2x + 1 >= -9
# (x/3 - 2) > (2x + 3)

from sympy import symbols, solve

# 创建符号变量 x
x = symbols('x')
inequality1 = 2*x + 1 >= -9
inequality2 = (x/3 - 2) > (2*x + 3)

# 同时解两个不等式
solutions = solve([inequality1, inequality2], x)
print("不等式组的解集为：", solutions)
# 不等式组的解集为： (-5 <= x) & (x < -3)
# answer in the textbook: [-5, -3)



# -------------------------------------------
# 绝对值不等式
# page: 68
# solve: |x| > 3
from sympy import symbols, solve_univariate_inequality
x = symbols('x')
inequality = abs(x) > 3
solutions = solve_univariate_inequality(inequality, x, relational=False)

print("Solutions for |x| > 3:")
print(solutions)

# page 69
# solve: |a - 1| <= 2
a = symbols('a')
inequality = abs(a - 1) <= 2
solutions = solve_univariate_inequality(inequality, a, relational=False)

print("Solutions for |a - 1| <= 2:")
print(solutions)

# page 70
# solve: |(3 + x) / 2| <= 5
x = symbols('x')
inequality = abs((3 + x)/2) <= 5
solutions = solve_univariate_inequality(inequality, x, relational=False)

print("Solutions for |(3 + x) / 5|:")
print(solutions)





