user_input = input()
text = ""
last_chr = ""

for ch in user_input:
    if ch != last_chr:
        text += ch
        last_chr = ch

print(text)
