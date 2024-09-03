# 一元二次方程的解集
# ax^2 + bx + c = 0
# a,b,c are constant, and a != 0
# 因式分解法, if b**2-4*a*c > 0, solution：
# x1 = (b * (-1) + np.sqrt(b**2 - 4 * a * c)) / (2 * a)
# x2 = (b * (-1) - np.sqrt(b**2 - 4 * a * c)) / (2 * a)

# page 52， example 1
# x - s* np.sqrt(x) - 1 = 0
# let y = np.sqrt(x)
# y **2 - 2^y - 1 = 0
import numpy as np

a = 1
b = -2
c = -1
y1 = (b * (-1) + np.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
y2 = (b * (-1) - np.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
x1 = y1 ** 2
x2 = y2 ** 2
print(x1)
print(x2)

# page 52, example2
# 2x^2 + 3x -4=0
a = 2
b = 3
c = -4
x1 = (b * (-1) + np.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
x2 = (b * (-1) - np.sqrt(b ** 2 - 4 * a * c)) / (2 * a)

print(x1**2 + x2**2)
print(25/4)
print(abs(x1 - x2))
print(np.sqrt(41)/2)




