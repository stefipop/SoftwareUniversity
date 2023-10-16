text = tuple(input())
text_dict = {}

for ch in text:
    text_dict.setdefault(ch, 0)
    text_dict[ch] += 1
    # text_dict[ch] = text_dict.get(ch, 0) + 1

for key, value in sorted(text_dict.items()):
    print(f"{key}: {value} time/s")

# unique_simbols = sorted(set(text))
#
# for el in unique_simbols:
#     print(f"{el}: {text.count(el)} time/s")
