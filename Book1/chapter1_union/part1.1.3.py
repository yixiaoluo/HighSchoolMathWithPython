# 交集
# 创建两个集合
s = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}
print(s, s2)
result = s & s2  # {3, 4, 5}
print('交集 result =', result)

# 并集
# | 并集运算
result = s | s2  # {1,2,3,4,5,6,7}
print('并集 result =', result)

# 补集
# A是全集U的一个子集，U中不属于A的元素组成的集合是A在U中的补集
# 也就是 x 属于U，但是不属于A
# https://cloud.tencent.com/developer/article/1573223
list_U = [1, 2, 3, 4, 5]
list_A = [3, 4, 5, 6, 7]
list_B = [x for x in list_U if x not in list_A]
print(list_B)


