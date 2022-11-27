# add heroes to the dictionary
line = input()
targets_dictionary = {}
while line != 'Sail':
    data_targets = line.split("||")
    city = data_targets[0]
    population = int(data_targets[1])
    gold = int(data_targets[2])

    if city not in targets_dictionary:
        targets_dictionary[city] = []
        targets_dictionary[city] = [int(population), int(gold)]
    else:
        targets_dictionary[city][0] += int(population)
        targets_dictionary[city][1] += int(gold)
    line = input()

command = input()

while command != 'End':
    data = command.split('=>')

    if data[0] == 'Plunder':
        town = data[1]
        people = int(data[2])
        gold = int(data[3])
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        targets_dictionary[town][0] -= people
        targets_dictionary[town][1] -= gold
        if targets_dictionary[town][0] <= 0 or targets_dictionary[town][1] <= 0:
            del(targets_dictionary[town])
            print(f"{town} has been wiped off the map!")

    elif data[0] == 'Prosper':
        town = data[1]
        gold = int(data[2])
        if gold < 0:
            print(f"Gold added cannot be a negative number!")
        else:
            targets_dictionary[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {targets_dictionary[town][1]} gold.")

    command = input()

if targets_dictionary:
    print(f"Ahoy, Captain! There are {len(targets_dictionary)} wealthy settlements to go to:")
    for key, value in targets_dictionary.items():
        print(f"{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
