# frequency and probability

# Monte Carlo Estimate of Pi
import numpy as np
n = 1000

x = np.random.uniform(-1, 1, n)
y = np.random.uniform(-1, 1, n)

distance = x**2 + y**2
inside_circle = np.sum(distance <= 1)
pi_estimate = 4 * inside_circle / n
print(pi_estimate)


