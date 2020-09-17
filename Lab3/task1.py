n = int(input('n = '))

data = dict()

for i in range(n):
    key, value = input().split()
    data[key] = data[key] + int(value) if key in data else int(value)

for key,value in sorted(data.items()):
    print("{} : {}".format(key, value))
