# 方程组的解集
# https://geek-docs.com/python/python-ask-answer/321_python_how_can_i_solve_equations_in_python.html
import sympy as sp

x = sp.Symbol('x')
equation = sp.Eq(2 * x + 3, 7)
sol = sp.solve(equation)
print(sol)


# -----------------------------
# page 54
# question:
# x -y = 1
# x + y = 3

from sympy import symbols, Eq, solve
x, y = symbols('x y')
# 定义方程
eq1 = Eq(x - y, 1)
eq2 = Eq(x + y, 3)
# 求解方程组
solution = solve((eq1, eq2), (x, y))
print(solution)

# -----------------------------
# page 56, example 1
# question:
# x^2 + y^2 = 5
# y = x + 1
x, y = symbols('x y')
# 定义方程
eq1 = Eq(x**2 + y**2, 5)
eq2 = Eq(y - x, 1)
# 求解方程组
solution = solve((eq1, eq2), (x, y))
print(solution)


# -----------------------------
# page 56, example 2
# question:
# x^2 + y^2 = 2
# (x-1)**2 + (y-2)**2 = 1
x, y = symbols('x y')
# 定义方程
eq1 = Eq(x**2 + y**2, 2)
eq2 = Eq((x-1)**2 + (y-2)**2, 1)
# 求解方程组
solution = solve((eq1, eq2), (x, y))
print(solution)
