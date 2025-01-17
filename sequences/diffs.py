'''
Find the difference between each consecutive pair of numbers in a sequence.
'''
seq = [2, 7, 15, 26, 40, 57]
diffs = []

for i in range(1, len(seq)):
    diffs.append(seq[i] - seq[i - 1])

print(diffs)