data = input()
list_of_string = []
list_of_numbers = []
result_list = []

for char in data:
    if char.isdigit():
        list_of_numbers.append(char)
    else:
        list_of_string.append(char)

take_list = []
skip_list = []

for index in range(len(list_of_numbers)):
    if index % 2 == 0:
        take_list.append(int(list_of_numbers[index]))
    else:
        skip_list.append(int(list_of_numbers[index]))

for index in range(len(take_list)):
    result_list += list_of_string[0:take_list[index]:1]
    list_of_string = list_of_string[(take_list[index] + skip_list[index])::]

print(''.join(result_list))
