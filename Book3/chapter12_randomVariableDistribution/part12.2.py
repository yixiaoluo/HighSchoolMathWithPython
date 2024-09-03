# discrete random variable

# Page 60, question 4
# 抛掷一枚质地均匀的硬币２次，写出正面向上次次数的分布列．
# Toss a coin twice. Write the probability distribution of the number of times the coin shows heads.

# toss a coin
P_head = 0.4
P_tail = 1- P_head

# toss the coin twice
# zero head: TT
# one head: HT,TH
# two head: HH
p_0 = P_tail * P_tail
print(p_0)
p_1 = P_head * P_tail + P_tail * P_head
print(p_1)
p_2 = P_head * P_head
print(p_2)



