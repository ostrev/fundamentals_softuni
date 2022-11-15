def check_list(list_of_car):
    car_sum = 0
    for number in list_of_car:
        if number == 0:
            car_sum *= 0.8
        car_sum += number
    return car_sum


list_of_race = [int(s) for s in input().split()]
middle_index = len(list_of_race) // 2
left_car = list_of_race[0:middle_index]
right_car = list_of_race[len(list_of_race):middle_index:-1]

left_car_sum = check_list(left_car)
right_car_sum = check_list(right_car)

winner = ''
if left_car_sum < right_car_sum:
    winner = 'left'
    total_time = left_car_sum
else:
    winner = 'right'
    total_time = right_car_sum
print(f"The winner is {winner} with total time: {total_time:.1f}")
