from math import cos, factorial, fabs

eps = float(input('Eps = '))
a = float(input('a = '))
x = float(input('b = '))

all_sum = 0
k = 0

while True:
    curr_sum = cos(a ** k + x ** k) / factorial(k ** 2)
    k = k + 1
    all_sum += curr_sum

    if fabs(curr_sum) <= eps:
        print('Sum = ', all_sum)
        print('Additions count = ', k)
        break
