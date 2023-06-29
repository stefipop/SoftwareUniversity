words = input().split()
result = list(filter(lambda x: len(x) % 2 == 0, words))

# # result = [word for word in words if len(word) % 2 == 0]
# # print('\n'.join(result))

[print(x) for x in result]
