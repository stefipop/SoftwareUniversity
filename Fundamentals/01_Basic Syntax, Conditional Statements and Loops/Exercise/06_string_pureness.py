n = int(input())

for _ in range(n):
    word = input()
    is_pure = True

    for i in word:
        if i == ',' or i == '.' or i == '_':
            is_pure = False
            break
    if is_pure:
        print(f"{word} is pure.")
    else:
        print(f"{word} is not pure!")
