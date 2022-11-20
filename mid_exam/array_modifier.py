initial_list = [int(x) for x in input().split()]
command = input()

while command != 'end':
    data = command.split()
    if data[0] == "swap":
        index_one, index_two = int(data[1]), int(data[2])
        temp_data = initial_list[index_one]
        initial_list[index_one] = initial_list[index_two]
        initial_list[index_two] = temp_data
    elif data[0] == "multiply":
        index_one, index_two = int(data[1]), int(data[2])
        initial_list[index_one] *= initial_list[index_two]
    elif data[0] == "decrease":
        initial_list = [int(s - 1) for s in initial_list]

    command = input()

print(', '.join([str(x) for x in initial_list]))
