from functools import reduce

a = float(input('a = '))
b = float(input('b = '))

n = int(input('n = '))

arr = []
vector = []

for i in range(n):
    arr.append(int(elem) for elem in input().split())
    searched_values = list(filter(lambda x: a <= x <= b, arr[i]))

    vector.append(0 if len(searched_values) == 0 else reduce((lambda x, y: (x*y)**2), searched_values))

print(vector)
