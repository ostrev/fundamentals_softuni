number = int(input())
type_name = {}
name_stats = {}
overwrite = False
for _ in range(number):
    command = input()
    data = command.split()
    type = data[0]
    name = data[1]
    if data[2] != 'null':
        damage = int(data[2])
    else:
        damage = int(45)
    if data[3] != 'null':
        health = int(data[3])
    else:
        health = int(250)
    if data[4] != 'null':
        armor = int(data[4])
    else:
        armor = int(10)

    if type not in type_name:
        type_name[type] = []
        type_name[type].append(name)
    else:
        if name not in type_name[type]:
            type_name[type].append(name)

    t_n = f'{type} {name}'
    if t_n not in name_stats:
        name_stats[t_n] = []
        name_stats[t_n].append(damage)
        name_stats[t_n].append(health)
        name_stats[t_n].append(armor)
    else:  # проверка за дали ми трябва булева за презаписване
        name_stats[t_n][0] = damage
        name_stats[t_n][1] = health
        name_stats[t_n][2] = armor

new_dic = {}
avr_dic = {}
for types, names in {x: sorted(type_name[x]) for x in type_name.keys()}.items():
    for name in names:
        type_name_str = f'{types} {name}'
        for key in name_stats:
            if key == type_name_str:
                new_dic[type_name_str] = name_stats[type_name_str]
                if types not in avr_dic:
                    avr_dic[types] = []
                avr_dic[types] += name_stats[type_name_str]
                break
sum_list = []
total = 0
my_dic = {}
for k, list in avr_dic.items():
    if len(list) > 3:
        for g in range(0, int((len(list)/3)) + 1):
            for i in range(g, len(list), 3):
                total += list[i]
            average = total/int(len(list)/3)
            total = 0
            if k not in my_dic:
                my_dic[k] = []
            my_dic[k].append(average)
    else:
        if k not in my_dic:
            my_dic[k] = []
        my_dic[k] = list
        # да вкарам стойностите в новия речник

for k, v in my_dic.items():
    print(f"{k}::({v[0]:.2f}/{v[1]:.2f}/{v[2]:.2f})")
    for key, value in new_dic.items():
        list_name = key.split()
        if k == list_name[0]:
            print(f"-{list_name[1]} -> damage: {value[0]}, health: {value[1]}, armor: {value[2]}")
