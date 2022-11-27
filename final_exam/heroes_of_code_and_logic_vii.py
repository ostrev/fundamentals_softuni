# add heroes to the dictionary
number_of_heroes = int(input())
heroes_dictionary = {}
for _ in range(number_of_heroes):
    hero = input()
    hero_name, hp, mp = hero.split(" ")

    if hero_name not in heroes_dictionary:
        heroes_dictionary[hero_name] = []
    heroes_dictionary[hero_name] = [int(hp), int(mp)]

command = input()

while command != 'End':
    data = command.split(' - ')

    if data[0] == 'CastSpell':
        hero_name = data[1]
        mp_needed = int(data[2])
        spell_name = data[3]
        if heroes_dictionary[hero_name][1] >= mp_needed:
            heroes_dictionary[hero_name][1] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes_dictionary[hero_name][1]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif data[0] == 'TakeDamage':
        hero_name = data[1]
        damage = int(data[2])
        attacker = data[3]
        heroes_dictionary[hero_name][0] -= damage

        if heroes_dictionary[hero_name][0] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes_dictionary[hero_name][0]} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            del(heroes_dictionary[hero_name])

    elif data[0] == 'Recharge':
        hero_name = data[1]
        amount = int(data[2])
        if heroes_dictionary[hero_name][1] + amount >= 200:
            amount = 200 - heroes_dictionary[hero_name][1]
        heroes_dictionary[hero_name][1] += amount
        print(f"{hero_name} recharged for {amount} MP!")
    elif data[0] == 'Heal':
        hero_name = data[1]
        amount = int(data[2])
        if heroes_dictionary[hero_name][0] + amount >= 100:
            amount = 100 - heroes_dictionary[hero_name][0]
        heroes_dictionary[hero_name][0] += amount
        print(f"{hero_name} healed for {amount} HP!")

    command = input()

for key, value in heroes_dictionary.items():
    print(f"{key}")
    print(f"  HP: {value[0]}")
    print(f"  MP: {value[1]}")
