'''
logarithm
'''
import math

# x = log_a(N)
# x叫做以a为底的对数： x is called the logarithm with base a
# log_10(N): 常用对数，common logarithm
# log_e(N): 自然对数，natural logarithm

# page122, example 1:
# (1) 5^4 = 625，把指数式化为对数式
x = math.log(625, 5)
print(x)
x = math.log(1/64, 2)
print(x)
x = math.log(5.73, 1/3)
print(x)
x = math.log(16, 1/2)
print(x)
x = math.log(0.01, 10)
print(x)
x = math.log(10, math.e)
print(x)

# page122, example 2: 求下列各式中的x值
# log_64(x) = -2/3
x = 64 ** (-2/3)
print(x)
# log_x(8) = 6
x = 8 ** (1/6)
print(x)
# lg(100) = x
x = math.log(100, 10)
print(x)
# -ln(e^2) = x
x = -1 * (math.log(math.e **2, math.e))
print(x)








