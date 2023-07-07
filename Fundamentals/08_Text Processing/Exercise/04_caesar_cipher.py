text = input()
encrypted_text = ""

for ch in text:
    encrypted_ch = chr(ord(ch) + 3)
    encrypted_text += encrypted_ch

print(encrypted_text)
