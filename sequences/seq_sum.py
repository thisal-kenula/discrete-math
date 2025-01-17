
# Sum of an arithmetic sequence (Know the first term, last term, and number of terms)
'''
Example: for the sequence 2, 4, 6, 8, 10, 12
first term = 2; last term = 12; number of terms = 5
Output: 42
'''
first_num = 2
last_num = 12
last_term = 5 # first term = 0
summand = first_num + last_num
S = summand * (last_term + 1) // 2
print(S)

