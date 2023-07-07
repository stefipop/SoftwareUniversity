text = input()

for idx in range(len(text)):
    if text[idx] == ":":
        print(f":{text[idx + 1]}")
