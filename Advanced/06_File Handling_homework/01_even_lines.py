char_for_change = ["-", ",", ".", "!", "?"]

with open('text.txt', 'r') as file:
    for line, text in enumerate(file):
        if line % 2 == 0:
            reversed_text = ' '.join(reversed(text.strip().split()))
            for char in char_for_change:
                reversed_text = reversed_text.replace(char, '@')
            print(''.join(reversed_text))
