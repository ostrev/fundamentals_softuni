initial_sequence = input().split()
number = int(input())
result = []
counter = 0
reset_index = 0

while len(initial_sequence) > 0:
    counter += 1
    if counter % number == 0:
        result.append(initial_sequence.pop(reset_index))
    else:
        reset_index += 1

    if len(initial_sequence) == reset_index:
        reset_index = 0

print(f"[{','.join(result)}]")


