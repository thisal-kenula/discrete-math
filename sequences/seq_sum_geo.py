'''
Calculate the sum of the first n + 1 terms of a geometric sequence
Example: 
    for the sequence 5 + 15 + 45 + ... + 5*3**20
    first term = 5; common_ratio = 3; n = 20
    output: 26150883005
'''
initial = 5
common_ratio = 3
n = 20 # last term (number of terms - 1, because first term = 0)
sum_n = initial * (1 - common_ratio ** (n + 1)) // (1 - common_ratio)

print(sum_n)