message = input()

command = input()

while command != 'Travel':
    data = command.split(':')
    if data[0] == 'Add Stop':
        index = int(data[1])
        string_for_insert = data[2]
        if 0 <= index < len(message):
            message = message[:index] + string_for_insert + message[index::]
        print(message)
    elif data[0] == 'Remove Stop':
        start_index = int(data[1])
        stop_index = int(data[2])
        if 0 <= start_index < len(message) and 0 <= stop_index < len(message):
            message = message[:start_index] + message[stop_index+1::]
        print(message)
    elif data[0] == 'Switch':
        substring, replacement = data[1:]
        message = message.replace(substring, replacement)
        print(message)
    command = input()
print(f'Ready for world tour! Planned stops: {message}')
