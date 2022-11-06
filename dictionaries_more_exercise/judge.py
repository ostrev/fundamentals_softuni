input_line = input()
contests_users_points_dict = {}
individual_standing = {}
while input_line != 'no more time':
    user, contest, points = input_line.split(' -> ')
    if contest not in contests_users_points_dict:
        contests_users_points_dict[contest] = {}
        contests_users_points_dict[contest][user] = int(points)
    else:
        if user in contests_users_points_dict[contest]:
            if int(points) > contests_users_points_dict[contest][user]:
                contests_users_points_dict[contest][user] = int(points)
        else:
            contests_users_points_dict[contest][user] = int(points)

    input_line = input()

for contest, user_dict in contests_users_points_dict.items():
    counter = 0
    print(f'{contest}: {len(user_dict)} participants')
    sorted_user_dict = dict(sorted(user_dict.items(), key=lambda kvp: (-kvp[1], kvp[0])))
    for user, points in sorted_user_dict.items():
        counter += 1
        if user not in individual_standing:
            individual_standing[user] = points
        else:
            individual_standing[user] += points
        print(f'{counter}. {user} <::> {points}')

counter = 0
print('Individual standings:')
for user, points in sorted(individual_standing.items(), key=lambda kvp: (-kvp[1], kvp[0])):
    counter += 1
    print(f'{counter}. {user} -> {points}')
