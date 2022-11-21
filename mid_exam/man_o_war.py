pirate_ship_status = [int(s) for s in input().split('>')]
warship_status = [int(s) for s in input().split('>')]
max_health_capacity = int(input())

command = input()

while command != "Retire":
    data = command.split()

    if data[0] == "Fire":
        index = int(data[1])
        damage = int(data[2])
        if 0 <= index < len(warship_status):
            warship_status[index] -= damage
            if warship_status[index] <= 0:
                print("You won! The enemy ship has sunken.")
                exit()
    elif data[0] == "Defend":
        start_index = int(data[1])
        end_index = int(data[2])
        damage = int(data[3])
        if 0 <= start_index < len(pirate_ship_status) and 0 <= end_index < len(pirate_ship_status):
            for index in range(start_index, end_index + 1):
                pirate_ship_status[index] -= damage
                if pirate_ship_status[index] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    exit()
    elif data[0] == "Repair":
        index = int(data[1])
        health = int(data[2])
        if 0 <= index < len(pirate_ship_status):
            pirate_ship_status[index] += health
            if pirate_ship_status[index] > max_health_capacity:
                pirate_ship_status[index] = max_health_capacity

    elif data[0] == "Status":
        count = 0
        for section in pirate_ship_status:
            if section < max_health_capacity * 0.2:
                count += 1
        print(f"{count} sections need repair.")
    command = input()

print(f"Pirate ship status: {sum(pirate_ship_status)}")
print(f"Warship status: {sum(warship_status)}")
