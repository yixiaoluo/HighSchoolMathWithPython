# continous random variable
# normal distribution

# Plot the Standard Normal Distribution:
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Define the range for x values
x = np.linspace(-4, 4, 1000)

# Calculate the standard normal distribution (mean=0, std=1)
pdf = norm.pdf(x, 0, 1)

# Plot the standard normal distribution
plt.figure(figsize=(8, 6))
plt.plot(x, pdf, label='Standard Normal Distribution', color='blue')
plt.fill_between(x, pdf, alpha=0.2, color='blue')
plt.title('Standard Normal Distribution')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.grid(True)
plt.legend()
plt.show()
