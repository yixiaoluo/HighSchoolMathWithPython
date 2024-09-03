# arrangement and combinations
# choose m from n

# page 16, question 1_(1)
# Generate all possible two-digit numbers using [0,1,2,3,4],
# make sure there are no repeated digits in each number
import itertools

digits = [0, 1, 2, 3, 4]
permutations = itertools.permutations(digits, 2)
valid_numbers = []
for num in permutations:
    if num[0] != 0:
        number = num[0] * 10 + num[1]
        valid_numbers.append(number)

print(valid_numbers)

# Arrangement
# choose m from n
# A_n_m = n * (n-1) * (n-2)* ...*(n-m+1)
# A_5_2 = 5 * 4 = 20
# A_8_3 = 8 * 7 * 6 = 336

# A_n_n = n!

# Page 19, question 3
# calculate A_7_3, A_7_4
import math
A_7_3 = 7*6*5
print(A_7_3)
A_7_3 = math.perm(7, 3)
print(A_7_3)

A_7_4 = 7*6*5*4
print(A_7_4)
A_7_4 = math.perm(7, 4)
print(A_7_4)

# combinations
# choose m from n
# calculate C_4_3
C_4_3 = math.comb(4,3)
print(C_4_3)
