import re

name = input()

while name:


    result = []
    pattern = r'\d+'

    matches = re.finditer(pattern, name)

    for match in matches:
        print(match.group(0), end=" ")

    name = input()
