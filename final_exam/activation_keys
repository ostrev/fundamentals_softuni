message = input()

command = input()

while command != 'Generate':
    data = command.split('>>>')
    if data[0] == 'Contains':
        substring = data[1]
        if substring in message:
            print(f"{message} contains {substring}")
        else:
            print("Substring not found!")
    elif data[0] == 'Flip':
        type_case = data[1]
        start_index = int(data[2])
        end_index = int(data[3])
        if type_case == "Upper":
            for s in range(start_index, end_index):
                message = message[:s:] + message[s].upper() + message[s+1::]
            print(message)
        else:
            for s in range(start_index, end_index):
                message = message[:s:] + message[s].lower() + message[s+1::]
            print(message)

    elif data[0] == 'Slice':
        start_index = int(data[1])
        end_index = int(data[2])
        message = message[:start_index] + message[end_index:]
        print(message)
    command = input()
print(f'Your activation key is: {message}')
