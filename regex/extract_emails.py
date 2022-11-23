import re
name = input()

pattern = r'(?<=\s)(?P<user>[a-zA-Z0-9]+)(\.|_|-*[a-zA-Z0-9])*@(?P<host>[a-zA-z]{2,}(-[a-zA-Z]*)*)(\.[a-z]+)+'
matches = re.finditer(pattern, name)
for match in matches:
    print(match.group())

