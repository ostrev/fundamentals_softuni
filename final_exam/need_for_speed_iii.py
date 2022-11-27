# add cars to the dictionary
number_of_cars = int(input())
cars_dictionary = {}
for _ in range(number_of_cars):
    cars = input()
    car, mileage, fuel = cars.split("|")

    if car not in cars_dictionary:
        cars_dictionary[car] = []
    cars_dictionary[car] = [int(mileage), int(fuel)]


command = input()

while command != 'Stop':
    data = command.split(' : ')

    if data[0] == 'Drive':
        car = data[1]
        distance = int(data[2])
        fuel = int(data[3])
        if not cars_dictionary[car][1] >= fuel:
            print("Not enough fuel to make that ride")
        else:
            cars_dictionary[car][0] += distance
            cars_dictionary[car][1] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars_dictionary[car][0] >= 100000:
            print(f"Time to sell the {car}!")
            del(cars_dictionary[car])

    elif data[0] == 'Refuel':
        car = data[1]
        fuel = int(data[2])
        if cars_dictionary[car][1] + fuel > 75:
            fuel = 75 - cars_dictionary[car][1]
            cars_dictionary[car][1] += fuel
        else:
            cars_dictionary[car][1] += fuel
        print(f"{car} refueled with {fuel} liters")

    elif data[0] == 'Revert':
        car = data[1]
        kilometers = int(data[2])
        cars_dictionary[car][0] -= kilometers
        if cars_dictionary[car][0] >= 10000:
            print(f"{car} mileage decreased by {kilometers} kilometers")
        else:
            cars_dictionary[car][0] = 10000

    command = input()

for key, value in cars_dictionary.items():
    print(f"{key} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.")
