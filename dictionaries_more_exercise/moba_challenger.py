input_line = input()
player_position_skills_dict = {}
list_of_position = []
total_skills = {}
while input_line != 'Season end':
    if '->' in input_line:
        player, position, skills = input_line.split(' -> ')

        if player not in player_position_skills_dict:
            player_position_skills_dict[player] = {}
            player_position_skills_dict[player][position] = int(skills)
        else:
            if position not in player_position_skills_dict[player]:
                player_position_skills_dict[player][position] = int(skills)
            else:
                if int(skills) > player_position_skills_dict[player][position]:
                    player_position_skills_dict[player][position] = int(skills)
    else:
        player_one, player_two = input_line.split(' vs ')
        if player_one in player_position_skills_dict and player_two in player_position_skills_dict:
            for position in player_position_skills_dict[player_one].items():
                list_of_position.append(position[0])
            for position in player_position_skills_dict[player_two].items():
                if position[0] in list_of_position:
                    if player_position_skills_dict[player_one][position[0]] >\
                            player_position_skills_dict[player_two][position[0]]:
                        player_position_skills_dict.pop(player_two)
                    elif player_position_skills_dict[player_one][position[0]] <\
                            player_position_skills_dict[player_two][position[0]]:
                        player_position_skills_dict.pop(player_one)
                    list_of_position.clear()
    input_line = input()

sorted_total_skills = {}
for player, position_dict in player_position_skills_dict.items():
    total_skills[player] = sum(position_dict.values())
    sorted_total_skills = dict(sorted(total_skills.items(), key=lambda kvpt: (-kvp[1], kvp[0])))

for player, total_skills in sorted_total_skills.items():
    print(f'{player}: {total_skills} skill')
    for position, skills in sorted(player_position_skills_dict[player].items(), key=lambda kvp: (-kvp[1], kvp[0])):
        print(f'- {position} <::> {skills}')
