queue_of_animals = input().split(', ')

if queue_of_animals[-1] == 'wolf':
    print('Please go away and stop eating my sheep')
    exit()

for animal in range(len(queue_of_animals), -1, -1):
    if queue_of_animals[animal-1] == 'wolf':
        print(f'Oi! Sheep number {len(queue_of_animals) - animal}! You are about to be eaten by a wolf!')
        break
