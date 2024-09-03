# positive correlation and negative correlation

# page 103, question 2
import numpy as np
import matplotlib.pyplot as plt
list1 = [(2,2), (3,-1), (5,-7)]
x = [pair[0] for pair in list1]
y = [pair[1] for pair in list1]

# Calculate the correlation coefficient
correlation_matrix = np.corrcoef(x, y)
correlation = correlation_matrix[0, 1]
print(correlation)

# Plot the dot pairs
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='blue')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.legend()
plt.show()
