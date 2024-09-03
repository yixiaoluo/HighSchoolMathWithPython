# variance and standard deviation

list1 = [5,5,5,5,5,5,5,5,5]
list2 = [5,5,5,6,6,6,7,7,7]
from statistics import variance
from statistics import stdev

list_variance = variance(list1)
standard_deviation = stdev(list1)
print(list_variance)
print(standard_deviation)


list_variance = variance(list2)
standard_deviation = stdev(list2)
print(list_variance)
print(standard_deviation)


