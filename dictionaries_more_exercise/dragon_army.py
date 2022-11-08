dict = {
    'Red': {'Bazgargal': [100, 2500, 25], 'Obsidion': [220, 2200, 35]},
    'Black': {'Dargonax': [200, 3500, 18]},
    'Blue': {'Kerizsa': [60, 2100, 20], 'Algordox': [65, 1800, 50]}
        }

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

