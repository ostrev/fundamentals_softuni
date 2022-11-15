data = input().split(', ')
counter = 0
while '0' in data:
    data.remove('0')
    counter += 1
for _ in range(counter):
    data.append('0')

print([int(s) for s in data])
