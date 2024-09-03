# page 46, example 1
# 化简：(2x+1)^2 - (x-1)^2
# 结果：3x^2 + 6x
# 检验两者是否相同
x = 3
y1 = (2*x + 1) **2 - (x- 1)**2
y2 = 3 * x**2 + 6 * x
print(y1)
print(y2)

# 十字相乘法
# (ax+b)(cx+d)=ac(x^2) + (ad+bc)x + bd
a = 1
b = 2
c = 3
d = 4
y1 = (a * x + b) * (c*x + d)
y2 = a*c*(x**2) + (a*d + b*c) * x + b*d
print(y1)
print(y2)

# 方程的解集
# https://geek-docs.com/python/python-ask-answer/321_python_how_can_i_solve_equations_in_python.html
import sympy as sp

# page 48, 例2：求方程x^2-5x+6=0
x = sp.Symbol('x')
equation = sp.Eq(x**2 - 5*x + 6, 0)
sol = sp.solve(equation)
print(sol)