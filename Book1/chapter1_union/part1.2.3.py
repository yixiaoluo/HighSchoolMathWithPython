# 充分条件，必要条件
# 当命题“若P则Q”为真时，P称为Q的充分条件，Q称为P的必要条件。
# 当命题“若P则Q”与“若Q则P”皆为真时，P是Q的充分必要条件，同时，Q也是P的充分必要条件。
# 当命题“若P则Q”为真，而“若Q则P”为假时，我们称P是Q的充分不必要条件，Q是P的必要不充分条件，反之亦然。

# 充分条件的示例
def sufficient_condition(A):
    return A > 5

def B_satisfied_by_A(B):
    A = 7
    return A > 5 and B > 3

# 必要条件的示例
def necessary_condition(B):
    return B > 3

def A_required_for_B(A):
    return A > 5 and A < 10

# 测试充分条件
A_value = 7
if sufficient_condition(A_value):
    print("A > 5 is a sufficient condition for B > 3")

if B_satisfied_by_A(4):
    print("B > 3 is satisfied when A = 7")

# 测试必要条件
B_value = 4
if necessary_condition(B_value):
    print("B > 3 is a necessary condition for A > 5")

if A_required_for_B(7):
    print("A > 5 is required when B = 4")
