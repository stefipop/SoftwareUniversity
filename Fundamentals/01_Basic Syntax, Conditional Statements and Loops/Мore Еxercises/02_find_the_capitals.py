word = list(input())
cap_letters = []

for i in range(len(word)):
    ch = word[i]
    if ch.isupper():
        cap_letters.append(i)

print(cap_letters)
