# 1.1.1 集合及其表示方法

# a 属于A
# 如果A是由所有小于10的自然数组成的集合
# set集合是： 无序的、不重复的元素集合
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(set1)
# result: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# list是有序的、可变的、可包含重复元素的集合
# range is [0，N), from zero to N,
# including 0， not including N

list_A = []
for i in range(11):
    list_A.append(i)
print(list_A)

# 2： 几种常见数集
# TODO：需要学习 SymPy 包
# -- 自然数集 N
n = 10
natural_numbers = [i for i in range(1, n)]
print(natural_numbers)
# result：[1, 2, 3, 4, 5, 6, 7, 8, 9]

# -- 正整数集 N+
# 创建一个包含正整数的集合
positive_integers = {1, 2, 3, 4, 5}
print(positive_integers)
# 添加元素
positive_integers.add(6)
print(positive_integers)
# 删除元素
positive_integers.remove(3)
print(positive_integers)

# -- 整数集 Z
integers = {-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5}
print(integers)

# -- 有理数集 Q
max_number = 10
denominators = range(1, max_number)
numerator = range(max_number * (-1), max_number)
rational_numbers = []
for i in numerator:
    for j in denominators:
        if denominators != 0:
            rational_numbers.append(i / j)
print("-10到10的有理数集： ")
print(rational_numbers)

# 3.列举法 (page6)
set1 = {0, 1}
# 24的所有正因素
set_24_factor = {1, 2, 3, 4, 6, 8, 12, 24}
# 找出一个数的所有正因数
# https://geek-docs.com/python/python-ask-answer/995_python_what_is_the_most_efficient_way_of_finding_all_the_factors_of_a_number_in_python.html

def find_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors
print(find_factors(24))

# 4. 描述法
# 所有能被３整除的整数组成的集合：
def integers_divide_by_3(x):
    if isinstance(x, int):
        return 3 * x
    else:
        exit(2)

# 5 区间及其表示
# 开区间： （1，2）
# 检查一个数是否在开区间 (1, 2)
x = 1.5

if 1 < x < 2:
    print(f"{x} 属于开区间 (1, 2)")
else:
    print(f"{x} 不属于开区间 (1, 2)")


# 半开半闭区间 [-2,+00)
x = 3
if x >= -2:
    print(f"{x} 属于半开半闭区间 [-2,+00)")
else:
    print(f"{x} 不属于半开半闭区间 [-2,+00)")
