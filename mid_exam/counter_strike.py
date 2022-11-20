initial_energy = int(input())
command = input()
count = 0

while command != 'End of battle':
    distance = int(command)
    if distance <= initial_energy:
        count += 1
        initial_energy -= distance
    else:
        print(f"Not enough energy! Game ends with {count} won battles and {initial_energy} energy")
        exit(0)
    if count % 3 == 0:
        initial_energy += count

    command = input()
print(f"Won battles: {count}. Energy left: {initial_energy}")
