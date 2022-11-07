input_line = input()
dwarf_dictionary = {}
colorname_physics_dictionary = {}
new_dwarf_dictionary = {}

while input_line != "Once upon a time":
    name_of_dwarf, head_color_dwarf, physics_of_dwarf = input_line.split(' <:> ')
    if head_color_dwarf not in dwarf_dictionary:
        dwarf_dictionary[head_color_dwarf] = {}
        dwarf_dictionary[head_color_dwarf][name_of_dwarf] = int(physics_of_dwarf)
    elif name_of_dwarf not in dwarf_dictionary[head_color_dwarf]:
        dwarf_dictionary[head_color_dwarf][name_of_dwarf] = int(physics_of_dwarf)
    else:
        if int(physics_of_dwarf) > dwarf_dictionary[head_color_dwarf][name_of_dwarf]:
            dwarf_dictionary[head_color_dwarf][name_of_dwarf] = int(physics_of_dwarf)

    input_line = input()

head_name_dictionary = {}

for head_color, value in dwarf_dictionary.items():
    head_name_dictionary[head_color] = []
    for name, physics in value.items():
        head_name_dictionary[head_color].append(name)
        first_str = f'({head_color}) {name}'
        colorname_physics_dictionary[first_str] = physics

sorted_head_name_dictionary = sorted(head_name_dictionary.items(), key=lambda x: -len(x[1]))

for color, names in sorted_head_name_dictionary:
    for name in names:
        x = f'({color}) {name}'
        new_dwarf_dictionary[x] = colorname_physics_dictionary[x]

for k, v in sorted(new_dwarf_dictionary.items(), key=lambda kvpt: -kvpt[1]):
    print(f'{k} <-> {v}')
