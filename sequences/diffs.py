'''
Find the difference between each consecutive pair of numbers in a sequence.
'''
seq = [1,2,4,8,16,32,64]
diffs = []
k = 0
while len(diffs) != 1:
    k += 1
    diffs = []
    for i in range(1, len(seq)):
        diffs.append(seq[i] - seq[i - 1])
    seq = diffs
    print(diffs)
    if all(diffs[i] == diffs[i - 1] for i in range(1, len(diffs))):
        if len(diffs) != 1: print(f'Δ{k}-constant sequence')
        break
