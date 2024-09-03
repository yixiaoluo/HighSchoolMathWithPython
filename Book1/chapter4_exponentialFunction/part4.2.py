# 指数函数：
# 英文是：exponential function
# y = a ^ x, a是常数，a >0, 且 a ！= 1
import math

# plot a=1/3，a=2, a=3
import numpy as np
import matplotlib.pyplot as plt

# Define x values
x = np.linspace(-2, 2, 400)

# Define different values of a
a_values = [1/3, 2, 3]

# Plot y = a^x for each value of a
plt.figure(figsize=(8, 6))
for a in a_values:
    y = np.power(a, x)
    plt.plot(x, y, label=f'a={a}')

# Add labels and title
plt.title('Plot of y = a^x ')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)  # x-axis
plt.axvline(0, color='black', linewidth=0.5)  # y-axis
plt.grid(True)
plt.legend()
plt.show()


# page 13
# exercise A
# question 3, (1)
x = np.power(3, 0.8)
y = np.power(3, 0.7)
print(x)
print(y)
print(x > y)

# question 3, (2)
x = np.power(0.75, -0.1)
y = np.power(0.75, 0.1)
print(x)
print(y)
print(x > y)


# exercise B
# question 1, (1)
x = np.power(1.001, 0.001)
y = np.power(0.999, 0.999)
print(x)
print(y)
print(x > y)