# user_input = input().lower()
# words = ["sand", "water", "fish", "sun"]
# counter = 0
# for i in words:
#     counter += user_input.count(i)
# print(counter)


user_input = input().lower()
words = ["sand", "water", "fish", "sun"]
counter = sum(user_input.count(i) for i in words)
print(counter)

# import re
#
# user_input = input().lower()
# words = ["sand", "water", "fish", "sun"]
# counter = sum(len(re.findall(word, user_input)) for word in words)
# print(counter)
