command = input()
list_of_events = ['coding', 'dog', 'cat', 'movie']
counter_of_coffees = 0

while command != 'END':
    if command.lower() in list_of_events:
        if command.isupper():
            counter_of_coffees += 2
        else:
            counter_of_coffees += 1
    command = input()

if counter_of_coffees > 5:
    print('You need extra sleep')
else:
    print(counter_of_coffees)