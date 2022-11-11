numbers = input().split()
string_for_manipulation = list(input())
list_numbers = []
result = []
index = 0
for number in numbers:
    for digit in number:
        index += int(digit)
    list_numbers.append(index)
    index = 0
for number in list_numbers:
    char_index = number
    while char_index >= len(string_for_manipulation):
        char_index -= len(string_for_manipulation)
    result.append(string_for_manipulation.pop(char_index))
print(''.join(result))
