import re

text = input()
location = []
travel_points = 0
pattern = r'(=|\/)([A-Z][A-Za-z]{2,})(\1)'
matches = re.finditer(pattern, text)
for match in matches:
    location.append(match.group(2))
    travel_points += len(match.group(2))
print(f"Destinations: {', '.join(location)}")
print(f"Travel Points: {travel_points}")

