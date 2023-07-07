text = input().upper()
unique_symbols = ""
current_symbol = ""
repetitions = ''

for idx in range(len(text)):
    if not text[idx].isdigit():
        current_symbol += text[idx]
    else:
        for next_symbol in range(idx, len(text)):
            if not text[next_symbol].isdigit():
                break
            repetitions += text[next_symbol]
        unique_symbols += current_symbol * int(repetitions)
        current_symbol = ''
        repetitions = ''

print(f"Unique symbols used: {len(set(unique_symbols))}")
print(unique_symbols)
