# contingency table
# 为比较甲、乙两所学校学生的数学水平，采用简单随机抽样的方法抽取８８名
# 学生．测验得到了如下数据：甲校４３名学生中有１０名数学成绩优秀；乙校５名学
# 生中有７名数学成绩优秀．试分析两校学生中数学成绩优秀率之间是否存在差异．
# X = 0: student from school A
# X = 1: student from school B
# Y = 0: student is good at math
# Y = 1: student is not good at math

# X=0, y= 0 , count = 33
# X=0, y= 1 , count = 10
# X=1, y= 0 , count = 38
# X=1, y= 1 , count = 7

# School A: frequency of student who are good at math:
freq_A_not = 33/(33+10)
freq_A_good = 10/(33+10)

freq_B_not = 38/(38+7)
freq_B_good = 7/(38+7)


# null hypothesis
# chi-square test: test of independence
# in the example above:
chi_square = (88 * (33*7 - 10*38)^2) / (43*45*71*17)
print(chi_square)


