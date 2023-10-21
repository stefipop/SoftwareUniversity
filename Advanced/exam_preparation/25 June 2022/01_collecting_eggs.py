from collections import deque

BOX_SIZE = 50
filled_boxes = 0

eggs = deque(int(el) for el in input().split(", "))
paper = deque(int(el) for el in input().split(", "))

while eggs and paper:
    current_egg = eggs[0]
    current_paper = paper[-1]
    if current_egg <= 0:
        eggs.popleft()
    elif current_egg == 13:
        eggs.popleft()
        paper[0], paper[-1] = paper[-1], paper[0]
    else:
        if current_paper + current_egg <= BOX_SIZE:
            eggs.popleft()
            paper.pop()
            filled_boxes += 1
        else:
            eggs.popleft()
            paper.pop()

if filled_boxes:
    print(f"Great! You filled {filled_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")
if eggs:
    print(f"Eggs left: {', '.join(map(str, eggs))}")
if paper:
    print(f"Pieces of paper left: {', '.join(map(str, paper))}")
