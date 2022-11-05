next_happy_year = int(input())
while True:
    next_happy_year += 1
    set_of_happy_year = set(str(next_happy_year))
    if len(set_of_happy_year) == len(str(next_happy_year)):
        print(next_happy_year)
        break
