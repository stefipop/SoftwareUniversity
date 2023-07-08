user_input = input()
text = user_input[0]

for ch in user_input:
    if ch == text[-1]:
        continue
    text += ch

print(text)
