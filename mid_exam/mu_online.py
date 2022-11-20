initial_health = 100
data = input().split('|')
best_room = 0
bitcoins = 0
for room in data:
    command, com = room.split()
    number = int(com)
    best_room += 1
    if command == 'potion':
        if initial_health + number > 100:
            need_health = 100 - initial_health
        else:
            need_health = number
        initial_health += need_health
        print(f"You healed for {need_health} hp.")
        print(f"Current health: {initial_health} hp.")
    elif command == 'chest':
        bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        if initial_health - number > 0:
            initial_health -= number
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {best_room}")
            exit(0)

print(f"You've made it!")
print(f"Bitcoins: {bitcoins}")
print(f"Health: {initial_health}")
