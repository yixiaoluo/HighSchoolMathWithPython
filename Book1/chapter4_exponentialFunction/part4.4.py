'''
对数函数 logarithmic function
y = log_a(x), a > 0 and a != 1, The domain of x is from 0 to positive infinity.
'''

# page 132, 画函数 y = log_2(x)的图象
import matplotlib.pyplot as plt
import numpy as np

# Define the function y = log_2(x)
def log_base_2(x):
    return np.log2(x)

# Define the range of x values (from 0.1 to 10 to avoid log(0))
x_values = np.linspace(0.1, 10, 400)
y_values = log_base_2(x_values)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='$y = \log_2(x)$')
plt.title('Plot of $y = \log_2(x)$')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()



# 反函数 inverse function
# page 132, 画函数 y = log_2(x)的图象和y = log_(1/2)(x)
import matplotlib.pyplot as plt
import numpy as np

# Define the functions
def log_base_2(x):
    return np.log2(x)

def log_base_half(x):
    return np.log2(x) / np.log2(0.5)

# Define the range of x values (from 0.1 to 10 to avoid log(0))
x_values = np.linspace(0.1, 10, 400)
y_values_log2 = log_base_2(x_values)
y_values_log_half = log_base_half(x_values)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values_log2, label='$y = \log_2(x)$')
plt.plot(x_values, y_values_log_half, label='$y = \log_{1/2}(x)$', linestyle='--')

# Add labels and title
plt.title('Plots of $y = \log_2(x)$ and $y = \log_{1/2}(x)$')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()




