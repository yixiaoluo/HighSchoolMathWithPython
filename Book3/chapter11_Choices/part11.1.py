# summation principle

# calculate how many choices you have
choices = {
    'A': 3,
    'B': 4,
    'C': 2
}
total_choices = sum(choices.values())
print(total_choices)

# multiplication Principle
# Car plate number sample: AJR005
# rule: (1) use number 0-9,
# (2)any English letters except I, O
# (3) max of two English letters

result = 24 * 24*10*10*10*10

# how many sub set in union of [1,2,3,4,5,6,7,8,9]
import itertools
list1 = [1,2,3,4,5,6,7,8,9]
combinations_1 = list(itertools.combinations(list1, 1))
combinations_2 = list(itertools.combinations(list1, 2))
combinations_3 = list(itertools.combinations(list1, 3))
combinations_4 = list(itertools.combinations(list1, 4))
combinations_5 = list(itertools.combinations(list1, 5))
combinations_6 = list(itertools.combinations(list1, 6))
combinations_7 = list(itertools.combinations(list1, 7))
combinations_8 = list(itertools.combinations(list1, 8))
combinations_9 = list(itertools.combinations(list1, 9))
print(combinations_2)



