new_password = input()
command = input()

while command != 'Done':
    data = command.split(' ')
    if data[0] == 'TakeOdd':
        new_password = new_password[1::2]
        print(new_password)
    if data[0] == 'Cut':
        index = int(data[1])
        length = int(data[2])
        substring = new_password[index:index+length]
        new_password = new_password.replace(substring, '', 1)
        print(new_password)
    elif data[0] == 'Substitute':
        substring, substitute = data[1:]
        if substring in new_password:
            new_password = new_password.replace(substring, substitute)
            print(new_password)
        else:
            print("Nothing to replace!")
            
    command = input()
    
print(f'Your password is: {new_password}')
