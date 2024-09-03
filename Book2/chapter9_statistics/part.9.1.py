import random

# population_mean = sum all x / n

# generate 100 random number between [0,1]
random_numbers = [random.uniform(0, 1) for x in range(100)]
print(random_numbers)


# generate 100 random number between [a, b]
a = 10
b = 20
random_numbers_between_a_b = [random.uniform(a, b) for _ in range(100)]
print(random_numbers_between_a_b)


# mean, median, var, sd, quantile
import random
import statistics

# Define the range
a = 10
b = 20

# Generate 100 random numbers between a and b
random_numbers = [random.uniform(a, b) for _ in range(100)]

# Calculate mean, median, variance, standard deviation, and quantiles
mean_value = statistics.mean(random_numbers)
median_value = statistics.median(random_numbers)
variance_value = statistics.variance(random_numbers)
std_dev_value = statistics.stdev(random_numbers)
quartiles = statistics.quantiles(random_numbers, n=4)
deciles = statistics.quantiles(random_numbers, n=10)  