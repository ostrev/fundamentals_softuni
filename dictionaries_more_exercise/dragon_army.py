def check_for_null(damage_check, health_check, armor_check, default):
    if damage_check == 'null':
        damage_check = default[0]
    if health_check == 'null':
        health_check = default[1]
    if armor_check == 'null':
        armor_check = default[2]
    return damage_check, health_check, armor_check

number_of_line = int(input())
default_value = [45, 250, 10]
dict = {}
for _ in range(number_of_line):
    type, name, damage, health, armor = input().split()
    if type not in dict:
        dict[type] = {}
        damage, health, armor = check_for_null(damage, health, armor, default_value)
        dict[type][name] = [int(damage), int(health), int(armor)]
    else:
        damage, health, armor = check_for_null(damage, health, armor, default_value)
        dict[type][name] = [int(damage), int(health), int(armor)]


damage = 0
health = 0
armor = 0
string_for_print = ''
for key, value in dict.items():
    val = sorted(value.items(), key=lambda kvp: kvp[0])
    for name, list_physics in val:
        damage += list_physics[0]
        health += list_physics[1]
        armor += list_physics[2]
    damage = damage / len(value)
    health /= len(value)
    armor /= len(value)
    print(f'{key}::({damage:.2f}/{health:.2f}/{armor:.2f})')
    damage, health, armor = 0, 0, 0
    for name, list_physics in val:
        print(f'-{name} -> damage: {list_physics[0]}, health: {list_physics[1]}, armor: {list_physics[2]}')

