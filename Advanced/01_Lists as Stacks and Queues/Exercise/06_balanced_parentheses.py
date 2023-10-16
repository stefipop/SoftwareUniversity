# from collections import deque
#
# parenthesis = deque(input())
# open_brackets = deque()
#
# while parenthesis:
#     current_bracket = parenthesis.popleft()
#     if current_bracket in "({[":
#         open_brackets.append(current_bracket)
#     elif not open_brackets:
#         print("NO")
#         break
#     else:
#         if f"{open_brackets.pop() + current_bracket}" not in "(){}[]":
#             print("NO")
#             break
# else:
#     if open_brackets:
#         print("NO")
#     else:
#         print("YES")

parenthesis = input()
open_brackets = []
balanced = True

for ch in parenthesis:
    if ch in "({[":
        open_brackets.append(ch)
    elif not open_brackets:
        balanced = False
        break
    else:
        last_bracket = open_brackets.pop()
        if f"{last_bracket}{ch}" not in "(){}[]":
            balanced = False
            break
if balanced and not open_brackets:
    print("YES")
else:
    print("NO")


# open_brackets = "([{"
# closing_brackets = ")]}"
# counter = 0
#
# while parenthesis and counter < len(parenthesis) / 2:
#     if parenthesis[0] not in open_brackets:
#         break
#     idx = open_brackets.index((parenthesis[0]))
#     if parenthesis[1] == closing_brackets[idx]:
#         parenthesis.popleft()
#         parenthesis.popleft()
#         parenthesis.rotate(counter)
#         counter = 0
#     else:
#         parenthesis.rotate(-1)
#         counter += 1
#
# if parenthesis:
#     print("NO")
# else:
#     print("YES")
