# inequality
# python：比较运算符（等于，小于，大于，不等于，大于等于，小于等于）的用法
# https://blog.csdn.net/qq_44925904/article/details/103497315

print(1 > 2)  # False
print(1 < 2)  # True
print(1 == 2)  # False
print(1 != 2)  # True
print(1 >= 2)  # False
print(1 <= 2)  # True


# page 63, example 1
def y1(x):
    return x ** 2 - x


def y2(x):
    return x - 2


x = 1
y = y1(x) > y2(x)
print(y)  #True

x = -1
y = y1(x) > y2(x)
print(y)  #True

x = 0
y = y1(x) > y2(x)
print(y)  #True

# page 65, example 2
a = 2
b = 1
c = 3
d = 4
if a > b and c < d:
    x = (a - c) > (b - d)
    print(f"page 65, example 2, x: {x}")



