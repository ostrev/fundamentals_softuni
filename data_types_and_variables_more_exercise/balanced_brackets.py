number_of_lines = int(input())
is_balanced = True

left_bracket = ''
for _ in range(number_of_lines):
    line = input()
    if line != '(' and line != ')':
        continue

    if (line == ')' and left_bracket == '') or (line == '(' and left_bracket == '('):
        is_balanced = False
        break

    left_bracket += line

if is_balanced:
    print('BALANCED')
else:
    print('UNBALANCED')
