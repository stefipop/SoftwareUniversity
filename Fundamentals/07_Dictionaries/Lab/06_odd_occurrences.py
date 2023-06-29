# words = [el.lower() for el in input().split()]
words = input().lower().split()
default = 0
occurrences = dict.fromkeys(words, default)

for word in words:
    occurrences[word] += 1
    # occurrences[word] = words.count(word)

for word, count in occurrences.items():
    if count % 2 != 0:
        print(word, end=' ')
