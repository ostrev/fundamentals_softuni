import re

text = input()
total_calories = []
food = []
pattern = r'(#|\|)(?P<item>[A-Za-z\s]+)(\1)(?P<data>\d{2}\/\d{2}\/\d{2})(\1)(?P<calories>\d+)(\1)'

matches = re.finditer(pattern, text)

for match in matches:
    food.append(match.group('item'))
    food.append(match.group('data'))
    food.append(match.group('calories'))
    total_calories.append(int(match.group('calories')))

days = sum(total_calories) // 2000
print(f"You have food to last you for: {days} days!")
range_ind = int(len(food) / 3)
for i in range(range_ind):
    print(f"Item: {food[i*3]}, Best before: {food[i * 3 +1]}, Nutrition: {food[i * 3 +2]}")
