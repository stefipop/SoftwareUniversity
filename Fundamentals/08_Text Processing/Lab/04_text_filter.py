banned_words = input().split(", ")
sentence = input()

for word in banned_words:
    while word in sentence:
        sentence = sentence.replace(word, '*' * len(word))

print(sentence)
