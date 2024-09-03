import math
import numpy as np

'''
    M=a^m, N=a^n
    log_a(MN) = m+n
    
    # 对数换底公式
    # log_a(b)=[log_c(b)]/[log_c(a)]

'''


# page 124, 求下列各式的值
# lg(The 5th root of 100 )
x = math.log(100 ** (1/5), 10)
print(x)

x = math.log(4**7 * 2**5, 2)
print(x)
x1 = math.log(4**7, 2)
x2 = math.log(2**5, 2)
print(x1+x2)


# page 125, tourism number question
x = math.log(2, 1.11)
x1 = math.log(2, 10)
x2 = math.log(1.11, 10)
x = x1/x2


# page 126 Exercize, 求下列各式的值
# (1) log_3(27 * 9^2)
x = math.log(27,3) + math.log(9**2, 3)
print(x)
# (2) lg5 + lg2
x = math.log(5 * 2, 10)
print(x)
# (3) ln3 + ln(1/3)
x = math.log(3 * (1/3), math.e)
print(x)
# (4) log_3(5) - log_3(15)
x = math.log(5 /15, 3)
print(x)






