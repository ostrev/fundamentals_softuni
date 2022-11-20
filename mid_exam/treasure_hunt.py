initial_list = input().split('|')
data = input()
stolen = []
while data != "Yohoho!":
    command = data.split()
    if command[0] == "Loot":
        for index in range(1, len(command)):
            if command[index] not in initial_list:
                initial_list.insert(0, command[index])
    elif command[0] == "Drop":
        if 0 <= int(command[1]) < len(initial_list):
            loot = initial_list.pop(int(command[1]))
            initial_list.append(loot)

    elif command[0] == "Steal":
        count = 0
        while len(initial_list) > 0 and count != int(command[1]):
            count += 1
            stolen.append(initial_list.pop())
        print(', '.join(reversed(stolen)))
        stolen.clear()
    data = input()

average = 0
if initial_list:
    for element in initial_list:
        average += len(element)
    average /= len(initial_list)
    print(f"Average treasure gain: {average:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
