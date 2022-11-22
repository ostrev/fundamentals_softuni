import re
name = input()
result = []
pattern = r'(?P<code>\+359)(?P<separator>[\s|-])(2)(?P=separator)(\d{3})(?P=separator)(\d{4})\b'


matches = re.finditer(pattern, name)

for match in matches:
    result.append(match.group())

print(', '.join(result))
