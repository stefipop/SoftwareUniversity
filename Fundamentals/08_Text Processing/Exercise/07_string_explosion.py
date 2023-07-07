text = input()
strength = 0
final_str = ""

for idx in range(len(text)):
    if strength > 0 and text[idx] != ">":
        strength -= 1
    elif text[idx] == ">":
        final_str += text[idx]
        strength += int(text[idx + 1])
    else:
        final_str += text[idx]

print(final_str)
