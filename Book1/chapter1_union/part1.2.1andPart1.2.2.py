# 命题
# 真命题： True
# 假命题：  False
# https://www.hugchange.life/posts/2023_mathlogicpy/index.html
# https://www.cnblogs.com/qingchengzi/articles/18188592



print(1 + 1 > 2)

# and
# or
# not

age = int(input("请输入年龄："))
height = int(input("请输入身高："))
if age>=18 and age<=30 and height >=170 and height <= 185 :
    print("恭喜，你符合报考飞行员的条件")
else:
    print("抱歉，你不符合报考飞行员的条件")

# https://blog.csdn.net/m0_51284422/article/details/109441190
print(not 0)
print(not 1)
print(0 or 0)