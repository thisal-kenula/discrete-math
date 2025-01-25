'''
Find the difference between each consecutive pair of numbers in a sequence.
Find the coefficients of the polynomial that generates the sequence.

Example:
    sequence = [1, 2, 4, 8, 15, 26]
    >>> k = find_diffs(sequence)
    [1, 2, 4, 7, 11]
    [1, 2, 3, 4]
    [1, 1, 1]
    Δ3-constant sequence
    >>> print(find_a_n(k, sequence))
    [1/6, 0, 5/6, 1] # Coefficients of the polynomial 1/6n^3 + 0n^2 + 5/6n + 1
'''

def find_diffs(seq):
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
            if len(diffs) != 1: 
                print(f'Δ{k}-constant sequence')
                return k
    return None

def find_a_n(k, seq):
    import sympy as sp
    m1 = sp.Matrix([[i**j for j in range(k, -1, -1)] for i in range(k+1)]).inv()
    m2 = sp.Matrix(seq[:k+1])
    return list(m1 * m2)

# Usage
sequence = [4, 7, 11, 18, 29, 47]

k = find_diffs(sequence)

if k:
    print(find_a_n(k, sequence))
