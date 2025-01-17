'''
Check if a sequence is arithmetic or geometric and print the formula
- Sequence starts with term 0
'''
seq = [2, 4, 8, 16, 32]

diff = seq[1] - seq[0]
if all(seq[i + 1] - seq[i] == diff for i in range(len(seq) - 1)):
    print(f"a_n = {seq[0]} + {diff}n")
else:
    print("Not an arithmetic sequence")

ratio = seq[1] / seq[0]
if all(seq[i + 1] / seq[i] == ratio for i in range(len(seq) - 1)):
    print(f"a_n = {seq[0]} * {ratio}^n")
else:
    print("Not a geometric sequence")