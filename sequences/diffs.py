'''
Find the difference between each consecutive pair of numbers in a sequence.
'''
seq = [1, 2, 4, 9, 19, 36, 62, 99, 149]
diffs = []
while len(diffs) != 1:
    diffs = []
    for i in range(1, len(seq)):
        diffs.append(seq[i] - seq[i - 1])
    seq = diffs
    print(diffs)
    if all(diffs[i] == diffs[i - 1] for i in range(1, len(diffs))):
        break
