# 一元二次不等式的解集
# page 73： example 1
# 求不等式 x^2 - x - 2> 0 的解集
from sympy import symbols, solve_univariate_inequality
x = symbols('x')
inequality = x**2 - x - 2 > 0
solutions = solve_univariate_inequality(inequality, x, relational=False)

print("Solutions for x^2 - x - 2 > 0:")
print(solutions)


# -----------
# page 73： example 2
def solve_inequality(inequality):
    x = symbols('x')
    solutions = solve_univariate_inequality(inequality, x, relational=False)

    print(f"Solutions for {inequality}:")
    print(solutions)


inequality_1 = x ** 2 + 4 * x + 1 >= 0
solve_inequality(inequality=inequality_1)

inequality_2 = x ** 2 - 6 * x - 1 <= 0
solve_inequality(inequality=inequality_2)

inequality_3 = (-1) * x ** 2 + 2 * x - 1 < 0
solve_inequality(inequality=inequality_3)

inequality_4 = 2 * x ** 2 + 4 * x + 5 > 0
solve_inequality(inequality=inequality_4)


# -----------
# page 73： example 3
# 求不等式解集： (2*x + 1) / (x-2) >= 1
inequality_5 = (2*x + 1) / (x-2) >= 1
solve_inequality(inequality=inequality_5)

