contests_dictionary = {}
first_commands = input()
while first_commands != "end of contests":
    contest, password = first_commands.split(':')
    contests_dictionary[contest] = password
    first_commands = input()

user_contests_points_dict = {}
command = input()
while command != 'end of submissions':
    contest, password, username, points = command.split('=>')
    if contest in contests_dictionary and contests_dictionary[contest] == password:
        if username not in user_contests_points_dict:
            user_contests_points_dict[username] = {}
            user_contests_points_dict[username][contest] = int(points)
        else:
            if contest not in user_contests_points_dict[username]:
                user_contests_points_dict[username][contest] = int(points)
            else:
                if int(points) > user_contests_points_dict[username][contest]:
                    user_contests_points_dict[username][contest] = int(points)
    command = input()

max_points = 0
total_points = 0
best_candidate = ''
for user, contest in user_contests_points_dict.items():
    total_points = sum(user_contests_points_dict[user].values())
    if total_points > max_points:
        max_points = total_points
        best_candidate = user
        total_points = 0
print(f"Best candidate is {best_candidate} with total {max_points} points.")

sorted_dictionary = dict(sorted(user_contests_points_dict.items(), key=lambda kvp: kvp[0]))
print('Ranking:')
for user, contest in sorted_dictionary.items():
    print(user)
    for contest, points in sorted(contest.items(), key=lambda kvp: -kvp[1]):
        print(f'#  {contest} -> {points}')
