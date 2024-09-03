# frequency distribution table
# frequency distribution histogram

sample_list = [1,2,3,4,5,6,7,8,9,10]
max_value = max(sample_list)
min_value = min(sample_list)

# calcualte frequency distribution table
import random
from collections import Counter

random_list = [random.randint(1, 10) for x in range(100)]
frequency_distribution = Counter(random_list)
sorted_frequency_distribution = sorted(frequency_distribution.items())
for value, frequency in sorted_frequency_distribution:
    print(f"{value}:{frequency}")

# plot frequency distribution histogram
import random
import matplotlib.pyplot as plt

# Generate a random list of integers between 1 and 10 (for simplicity)
random_list = [random.randint(1, 10) for _ in range(100)]

# Plot frequency distribution histogram
plt.hist(random_list, bins=range(1, 12), edgecolor='black', align='left')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Frequency Distribution Histogram')
plt.xticks(range(1, 11))
plt.grid(axis='y', linestyle='--')

# Display the histogram
plt.show()



