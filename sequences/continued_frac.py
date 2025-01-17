'''
Convert a repeating decimal number into a fraction

Example:
    5.464646... = 541/99
'''
from decimal import Decimal
from fractions import Fraction

x = Decimal('5.46') # for 5.464646...
y = x
x //= 1
i = 0

while y % 1 != 0:
    y *= 10
    i += 1

print(Fraction(int(y - x), 10**i - 1))