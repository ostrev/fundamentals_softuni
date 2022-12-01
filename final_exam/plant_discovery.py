line = int(input())
plants_dictionary = {}

for _ in range(line):
    data = input(). split("<->")
    plant = data[0]
    rarity = int(data[1])
    if plant not in plants_dictionary:
        plants_dictionary[plant] = []
        plants_dictionary[plant] = [int(rarity), 0]
    else:
        plants_dictionary[plant][0] = int(rarity)

command = input()

while command != 'Exhibition':
    data = command.split(': ')
    if data[0] == 'Rate':
        plant_rating = data[1].split(" - ")
        plant = plant_rating[0]
        rating = int(plant_rating[1])
        if plant not in plants_dictionary:
            print("error")
        else:
            plants_dictionary[plant].append(rating)
    elif data[0] == 'Update':
        plant_rating = data[1].split(" - ")
        plant = plant_rating[0]
        new_rarity = int(plant_rating[1])
        if plant not in plants_dictionary:
            print("error")
        else:
            plants_dictionary[plant][0] = new_rarity
    elif data[0] == 'Reset':
        plant = data[1]
        if plant not in plants_dictionary:
            print("error")
        else:
            rarity = plants_dictionary[plant][0]
            plants_dictionary[plant] = [int(rarity), 0]

    command = input()
    
print('Plants for the exhibition:')

for plant, value in plants_dictionary.items():
    rarity = value[0]
    rating_list = value[1::]
    if sum(rating_list) == 0:
        average = 0
    else:
        average = sum(rating_list)/(len(rating_list) - 1)
    print(f'- {plant}; Rarity: {rarity}; Rating: {average:.2f}')
