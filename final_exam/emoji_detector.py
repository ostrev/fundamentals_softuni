import re
text = input()
emojis = []
threshold = 1
pattern_cool = r'\d'
cool_matches = [int(s) for s in re.findall(pattern_cool, text)]
for num in cool_matches:
    threshold *= num

print(f"Cool threshold: {threshold}")

pattern = r'(?P<emoji>(?P<sep>::|\*\*)([A-Z][a-z]{2,}))(?P=sep)'

matches = re.finditer(pattern, text)
for match in matches:
    emojis.append(match.group('emoji'))


print(f"{len(emojis)} emojis found in the text. The cool ones are:")
emoji_cool = 0
for emoji in emojis:
    cut_emoji = emoji[2::]
    for char in cut_emoji:
        emoji_cool += ord(char)

    if emoji_cool > threshold:
        print(emoji + emoji[:2])
    emoji_cool = 0

