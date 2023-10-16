from collections import deque

tools = deque(int(el) for el in input().split())
substances = [int(el) for el in input().split()]
challenges = [int(el) for el in input().split()]


while tools and substances and challenges:
    first_tool = tools.popleft()
    substance = substances.pop()

    result = first_tool * substance
    if result in challenges:
        challenges.remove(result)
    else:
        first_tool += 1
        tools.append(first_tool)
        substance -= 1
        if substance > 0:
            substances.append(substance)

if not challenges:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")
else:
    print("Harry is lost in the temple. Oblivion awaits him.")
if tools:
    print(f"Tools: {', '.join(map(str, tools))}")
if substances:
    print(f"Substances: {', '.join(map(str, substances))}")
if challenges:
    print(f"Challenges: {', '.join(map(str, challenges))}")
