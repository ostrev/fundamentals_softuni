message = input()

command = input()

while command != 'Decode':
    data = command.split('|')
    if data[0] == 'Move':
        number_of_letters = int(data[1])
        substring = message[:number_of_letters]
        message = message[number_of_letters::] + substring
    elif data[0] == 'Insert':
        index = int(data[1])
        value = data[2]
        message = message[:index] + value + message[index::]

    elif data[0] == 'ChangeAll':
        substring, replacement = data[1:]
        message = message.replace(substring, replacement)
    command = input()
print(f'The decrypted message is: {message}')
