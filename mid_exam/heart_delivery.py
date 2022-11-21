neighborhood = [int(s) for s in input().split('@')]
command = input()
position = 0
while command != 'Love!':
    data = command.split()
    jump = int(data[1])
    if position + jump >= len(neighborhood):
        position = 0
    else:
        position += jump
    if neighborhood[position] > 1 and neighborhood[position] - 2 == 0 :
        print(f"Place {position} has Valentine's day.")
        neighborhood[position] -= 2
    elif neighborhood[position] > 1:
        neighborhood[position] -= 2
    else:
        print(f"Place {position} already had Valentine's day.")
    command = input()
    
print(f"Cupid's last position was {position}.")
counter = 0
failed = 0
for house in neighborhood:
    if house == 0:
        counter += 1
    else:
        failed += 1
if counter == len(neighborhood):
    print("Mission was successful.")
else:
    print(f"Cupid has failed {failed} places.")
