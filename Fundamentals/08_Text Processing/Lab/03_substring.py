letters = input()
word = input()

while letters in word:
    word = word.replace(letters, '')

print(word)
