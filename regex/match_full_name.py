import re
name = input()
result = []
pattern = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'

matches = re.finditer(pattern, name)

for match in matches:
    result.append(match.group())

print(*result)
