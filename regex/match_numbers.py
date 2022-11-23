import re
name = input()
result = []
pattern = r'(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))'

matches = re.finditer(pattern, name)

for match in matches:
    print(match.group(0), end=" ")
