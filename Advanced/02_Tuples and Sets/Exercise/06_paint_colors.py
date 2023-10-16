from collections import deque

text = deque(input().split())
colors = {"red", "yellow", "blue", "orange", "purple", "green"}
secondary_colors = {
    "orange": {"yellow", "red"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"},
}
result = []

while text:
    start = text.popleft()
    end = text.pop() if text else ''

    for word in (start + end, end + start):
        if word in colors:
            result.append(word)
            break
    else:
        for el in (start[:-1], end[:-1]):
            if el:
                text.insert(len(text) // 2, el)
for color in set(secondary_colors.keys()).intersection(result):
    if not secondary_colors[color].issubset(result):
        result.remove(color)

print(result)
