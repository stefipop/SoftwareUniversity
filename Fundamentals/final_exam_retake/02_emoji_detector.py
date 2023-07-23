import re
# from math import prod
from functools import reduce


def sum_threshold(data):
    digits = [int(x) for x in text if x.isdigit()]
    threshold = reduce(lambda x, y: x * y, (int(x) for x in text if x.isdigit()), 1)
    return threshold


def find_emojis(text):
    pattern = r"(?P<surr>::|\*\*)(?P<emoji>[A-Z][a-z]{2,})(?P=surr)"
    emojis = re.findall(pattern, text)
    return emojis


def sum_ascii(words):
    sum_letters = 0
    cool_emojis = []
    for emoji in words:
        for letter in emoji[1]:
            sum_letters += ord(letter)
        if sum_letters >= validator:
            cool_emojis.append(emoji)
        sum_letters = 0
    return cool_emojis


text = input()
validator = sum_threshold(text)
print(f"Cool threshold: {validator}")
emoji_list = find_emojis(text)
cool_emojis = sum_ascii(emoji_list)

print(f"{len(emoji_list)} emojis found in the text. The cool ones are:")
for emoji in cool_emojis:
    print(f"{emoji[0]}{emoji[1]}{emoji[0]}")
