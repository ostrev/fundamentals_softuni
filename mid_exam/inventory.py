inventory = input().split(', ')

command = input()

while command != 'Craft!':
    data = command.split(' - ')
    if data[0] == 'Collect':
        if data[1] not in inventory:
            inventory.append(data[1])
    elif data[0] == 'Drop':
        if data[1] in inventory:
            inventory.remove(data[1])
    elif data[0] == 'Combine Items':
        items = data[1].split(":")
        if items[0] in inventory:
            index = inventory.index(items[0])
            inventory.insert(index + 1, items[1])
    elif data[0] == 'Renew':
        if data[1] in inventory:
            index = inventory.index(data[1])
            item = inventory.pop(index)
            inventory.append(item)

    command = input()
print(', '.join(inventory))
