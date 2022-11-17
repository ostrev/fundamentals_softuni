def data_types(command, data):
    result = ''
    if command == 'int':
        result = int(data) * 2
    elif command == 'real':
        result = float(data) * 1.5
        result = f'{result:.2f}'
    elif command == 'string':
            result = '$' + data + '$'

    return result

command = input()
data = input()
print(data_types(command, data))
