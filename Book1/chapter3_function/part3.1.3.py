# 函数的奇偶性
# y = f(x)的定义域为D，如果对于D内的任意一个x，都有 -x 属于D，且
# 偶函数：f(-x) = f(x)
# 奇函数：f(-x) = -f(x)

# page 110，example of 奇函数和偶函数
# 奇函数的英语：odd function
# 奇函数的英语：even function

# plot：f(x) = x ^ 3
import matplotlib.pyplot as plt
import numpy as np

# Define the function f(x) = x^3
def f(x):
    return x**3

# Generate x values
x_values = np.linspace(-2, 2, 400)

# Generate y values for f(x)
y_f = f(x_values)

# Plot f(x) = x^3
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_f, label='f(x) = x^3', color='blue')
plt.axhline(y=0, color='black', linewidth=0.5)  # x-axis
plt.axvline(x=0, color='black', linewidth=0.5)  # y-axis
plt.title('Plot of f(x) = x^3')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()


# plot：g(x) = 1/ x
# Define the function g(x) = 1/x
def g(x):
    return 1 / x

# Generate x values avoiding zero for g(x)
x_values_g = np.linspace(-2, 2, 400)
x_values_g = x_values_g[x_values_g != 0]

# Generate y values for g(x)
y_g = g(x_values_g)

# Plot g(x) = 1/x
plt.figure(figsize=(8, 6))
plt.plot(x_values_g, y_g, label='g(x) = 1/x', color='green')
plt.axhline(y=0, color='black', linewidth=0.5)  # x-axis
plt.axvline(x=0, color='black', linewidth=0.5)  # y-axis
plt.title('Plot of g(x) = 1/x')
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(-10, 10)  # Set y-axis limits to avoid infinite values
plt.grid(True)
plt.legend()
plt.show()


# page 111, example 1
# 判断下列函数是否具有奇偶性，用画图来测试
def plot_odd_even_function(fx, label):

    # Generate x values
    x_values = np.linspace(-10, 10, 400)

    # Generate y values for f(x)
    y_f = fx(x_values)

    # Plot f(x) = x^3
    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_f, label=label, color='blue')
    plt.axhline(y=0, color='black', linewidth=0.5)  # x-axis
    plt.axvline(x=0, color='black', linewidth=0.5)  # y-axis
    plt.title(f'Plot of f(x): {label}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.show()

# (1) f(x) = x + x^3 + x^5
def f(x):
    return x + x**3 + x**5
plot_odd_even_function(fx= f, label="f(x) = x + x^3 + x^5")

# (2) f(x) = x^2 + 1
def f(x):
    return x**2 + 1
plot_odd_even_function(fx= f, label="f(x) = x^2 + 1")

# (3) f(x) = x + 1
def f(x):
    return x + 1
plot_odd_even_function(fx= f, label="f(x) = x + 1")

# (4) f(x) = x^2
def f(x):
    return x**2
plot_odd_even_function(fx= f, label="f(x) = x**2")


