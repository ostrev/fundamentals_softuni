import re

text = input()
first_word = []
second_word = []
mirror_words = []
pattern = r'(@|#)(?P<word_one>[A-Za-z]{3,})(\1)(\1)(?P<word_tow>[A-Za-z]{3,})'
matches = re.finditer(pattern, text)
for match in matches:
    first_word.append(match.group('word_one'))
    second_word.append(match.group('word_tow'))
if first_word:
    print(f"{len(first_word)} word pairs found!")
    for index in range(len(first_word)):
        if first_word[index] == second_word[index][::-1]:
            mirror_word = first_word[index] + ' <=> ' + second_word[index]
            mirror_words.append(mirror_word)
else:
    print("No word pairs found!")

if mirror_words:
    print("The mirror words are:")
    print(', '.join(mirror_words))
else:
    print("No mirror words!")
