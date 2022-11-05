beach_string = input().lower()
list_of_words = ['sand', 'water', 'fish', 'sun']
count = 0
for word in list_of_words:
    count += beach_string.count(word)

print(count)
