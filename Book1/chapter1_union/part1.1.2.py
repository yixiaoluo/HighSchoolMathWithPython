# 集合的基本关系
# useful sites：
# https://developer.aliyun.com/article/748690
#https://blog.csdn.net/horses/article/details/122539249


# 子集
# A包含于B，或B包含A
set_A = {1, 2, 3}
set_B = {2}
set_C = {4}

if set_B.issubset(set_A):
    print("set_B is a subset of set_A")
else:
    print("set_B is not a subset of set_A")

if set_C.issubset(set_A):
    print("set_C is a subset of set_A")
else:
    print("set_C is not a subset of set_A")


# 真子集
set1 = {1, 2}
if set1.issubset(set_A) and set1 != set_A:
    print("set1是真子集")
else:
    print("set1不是真子集")

# 集合的相等
# 如果A属于B，且B属于A，则A=B
# https://deepinout.com/python/python-examples/t_python-program-to-check-two-set-are-equal_zh.html
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

if set1 & set2 == set1:
    print("两个集合相等")
else:
    print("两个集合不相等")

