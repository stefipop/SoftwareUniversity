strings = input().split()
empty_word = ''.join([ch * len(ch) for ch in strings])
print(empty_word)
