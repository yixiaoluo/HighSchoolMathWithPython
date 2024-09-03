# a^n
# 英语的说法是：a to the power of n
# a: the base
# n: the exponent

# 3 methods
a = 2
n = 5
method1 = a ** n

import math
method2 = math.pow(a, n)

import numpy as np
method3 = np.power(a, n)

print(method1)
print(method2)
print(method3)

# ------------------------------------------------------
# a的n次方根， 英语：the nth root of a
# 3 methods
a = 27
n = 3
method1 = a ** (1 / n)

import math
method2 = math.pow(a, 1 / n)

import numpy as np
method3 = np.power(a, 1 / n)
print(method1)
print(method2)
print(method3)

# 2.实数指数幂
# 比较2^3, 2^pi, 2^4
x1 = 2**3
x2 = 2**math.pi
x3 = 2**4
print(f"x1: {x1}")
print(f"x2: {x2}")
print(f"x3: {x3}")


# page 7, example 2
# question (1)
x1 = math.pow(3, 10)
x2 = math.pow(x1, 1/2)
x3 = math.pow(x2, 1/3)
x4 = math.pow(9, 1/3)
x5 = x3/x4
print(x5)  # 2.9999999999999996,书上答案是3

# question (2)
x1 = 2 + math.pow(3, 1/2)
x2 = math.pow(5, x1)
x3 = (math.pow(3, 1/2) * (-1)) / 3
x4 = math.pow(125, x3)
x5 = x2 * x4
print(x5)  #25.0











