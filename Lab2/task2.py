from math import sqrt, factorial

def count_denominator(n, curr_n=1):
    return 1 / 3 * sqrt(1 / factorial(curr_n) + count_denominator(n, curr_n + 1)) if curr_n <= n else 0


n = int(input('n = '))
m = int(input('m = '))

print(2 ** m / count_denominator(n))
