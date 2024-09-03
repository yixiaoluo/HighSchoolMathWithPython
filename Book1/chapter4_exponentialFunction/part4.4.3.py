'''
    不同函数增长的差异
'''

# plot y=2^x, y=2*x x from 0 to 5
import matplotlib.pyplot as plt
import numpy as np

# Define the range of x values
x_values = np.linspace(0, 5, 400)

# Define the functions
y_values_exp = 2 ** x_values
y_values_linear = 2 * x_values

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values_exp, label='$y = 2^x$')
plt.plot(x_values, y_values_linear, label='$y = 2x$', linestyle='--')

# Add labels and title
plt.title('Plots of $y = 2^x$ and $y = 2x$')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()


# plot y=2^x, y=2*x x from 0 to 20
import matplotlib.pyplot as plt
import numpy as np

x_values = np.linspace(0, 20, 400)

y_values_exp = 2 ** x_values
y_values_linear = 2 * x_values

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values_exp, label='$y = 2^x$')
plt.plot(x_values, y_values_linear, label='$y = 2x$', linestyle='--')

plt.title('Plots of $y = 2^x$ and $y = 2x$')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()


# plot y=lg_x, y=(1/10) * x, x from 0 to 60
import matplotlib.pyplot as plt
import numpy as np

x_values = np.linspace(0.1, 60, 400)

y_values_log10 = np.log10(x_values)
y_values_linear = (1/10) * x_values

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values_log10, label='$y = \log_{10}(x)$')
plt.plot(x_values, y_values_linear, label='$y = \\frac{1}{10}x$', linestyle='--')

plt.title('Plots of $y = \log_{10}(x)$ and $y = \\frac{1}{10}x$')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()
