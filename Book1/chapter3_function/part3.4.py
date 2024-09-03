# 数学建模：国民收入、消费与投资的关系
# 凯恩斯静态模型
# 国民收入：Y
# 国民投资：I
# 国民消费：C
"""
assumptions:
(1) Y,I,C 单位相同
(2) Y = C + I
(3) C = C_0 + a * Y, C_0 is fixed
(4) 边际消费倾向：收入从Y1变化到Y2，消费变化多少：
dc/dy = ((C_0 + a * Y2) - (C_0 + a * Y1)) / (Y2-Y1)
 = (a* (Y2 - Y1)) / (Y2 - Y1) = a
 a：收入每增加一个单位，消费将增加a个单位，a通常被成为边际消费倾向

"""

#  ----------- 收入与消费的关系
# Y =  (1/a)*C - C_0 / a
def consumption_to_income(C,a,C_0):
    income = (1/a)*C - C_0 / a
    print(f"消费: {C}， 收入: {income}")

C_0 = 10
a = 4/5
consumption_to_income(C=30, a=a, C_0=C_0)
consumption_to_income(C=35, a=a, C_0=C_0)

"""
output:
消费: 30， 收入: 25.0
消费: 35， 收入: 31.25
可以看到，消费增长5个单位时，收入增加了6.25个单位
"""

#  ----------- 收入与投资的关系
# Y =  (1/(1-a))*I - C_0 / (1-a)
def investment_to_income(I,a,C_0):
    income = (1/(1-a))*I + C_0 / (1-a)
    print(f"投资: {I}， 收入: {income}")

C_0 = 10
a = 4/5
investment_to_income(I=10, a=a, C_0=C_0)
investment_to_income(I=15, a=a, C_0=C_0)

"""
output:
投资: 10， 收入: 100.00000000000003
投资: 15， 收入: 125.00000000000003
可以看到，投资增长5个单位时，收入增加了25个单位
"""






