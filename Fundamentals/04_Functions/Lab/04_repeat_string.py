# def repeat(word, times):
#     return word * times
#
#
# wrap_text = input()
# n = int(input())
#
# result = repeat(wrap_text, n)
# print(result)

wrap_text = input()
n = int(input())

result = lambda word, times: word * times
print(result(wrap_text, n))
