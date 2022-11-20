def reduce_increase_targets(elements, value):
    for i in range(len(elements)):
        if elements[i] > value and elements[i] != -1:
            elements[i] -= value
        elif elements[i] <= value and elements[i] != -1:
            elements[i] += value
    return elements


targets = [int(x) for x in input().split()]
count = 0
command = input()
while command != 'End':
    index = int(command)
    if not 0 <= index < len(targets):
        command = input()
        continue
    if targets[index] >= 0:
        count += 1
        temp_data = targets[index]
        targets[index] = -1
        reduce_increase_targets(targets, temp_data)
    command = input()

print(f"Shot targets: {count} -> {' '.join([str(s) for s in targets])}")
