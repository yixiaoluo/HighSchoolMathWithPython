# bernoulli trials

# Binomial distribution
# X ~ B(n,p)

# Page 74, Example 1
# Toss a fair coin 10 times. calculate:
# The probability of getting 5 heads.
# The probability of frequency of heads falls within the interval [0.4, 0.6].

from scipy.stats import binom
n = 10
p = 0.5

k = 5
prob_5_heads = binom.pmf(k, n, p)
print(prob_5_heads)

k_low = int(n * 0.4)
k_high = int(n * 0.6)
prob_freq_in_range = binom.cdf(k_high, n, p) - binom.cdf(k_low - 1, n, p)
print(prob_freq_in_range)

# hypergeometric distribution
# page 78, example 4
# From 50 students, randomly select 5 students. Find the probability that Student A is selected.
from math import comb

total_students = 50
num_representatives = 5
total_ways = comb(total_students, num_representatives)
student_A_chosen = comb(total_students - 1, num_representatives - 1)
probability = student_A_chosen / total_ways
print(probability)





