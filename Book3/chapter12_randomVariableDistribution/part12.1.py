# conditional probability
# P(B|A) = P(AB) / P(A)

# total probability formula
# P(B) = sum_i(P(A_i) * P(B|A_i)

# Bayes formula
# P(A_i|B) = P(A_i) * P(B | A_i) / P(B)


# Page 52, question 1
# There are 12 multiple-choice questions, each with four possible answers.
# Zhang Jun has some ideas about 9 of the questions and no ideas about the remaining 3.
# The probability of answering a question correctly when Zhang Jun has some ideas is 0.9,
# the probability of guessing correctly when Zhang Jun has no ideas is 0.25.
# If Zhang Jun randomly selects one question from these 12,
# find the probability that he answers the question correctly.

event_A = "he has idea"
event_B = "he has no idea"
event_C = "he answers the question correctly"
# Probabilities
P_A = 9 / 12
P_B = 3 / 12
P_C_given_A = 0.9
P_C_given_B = 0.25

# Calculate the total probability of answering correctly
P_C = P_C_given_A * P_A + P_C_given_B * P_B
print(P_C)
