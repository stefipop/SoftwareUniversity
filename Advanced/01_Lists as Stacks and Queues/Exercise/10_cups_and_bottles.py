from collections import deque

cups = deque(int(x) for x in input().split())
bottles = [int(x) for x in input().split()]
wasted_litters_of_water = 0

while cups and bottles:
    # първи вариант
    # current_bottle = bottles.pop()
    # current_cup = cups.popleft()
    # if current_bottle < current_cup:
    #     current_cup -= current_bottle
    #     cups.appendleft(current_cup)
    #     continue
    # elif current_bottle > current_cup:
    #     current_bottle -= current_cup
    #     wasted_litters_of_water += current_bottle
    # втори вариант
    # current_cup = cups[0]
    # while current_cup > 0:
    #     current_bottle = bottles.pop()
    #     current_cup -= current_bottle
    # wasted_litters_of_water -= current_cup
    # cups.popleft()
    # трети вариант
    bottle = bottles.pop()
    cup = cups.popleft() - bottle

    if cup > 0:
        cups.appendleft(cup)
    else:
        wasted_litters_of_water += abs(cup)

if cups:
    print(f"Cups:", *cups, sep= " ")
else:
    print(f"Bottles:", *bottles, sep= " ")
print(f"Wasted litters of water: {wasted_litters_of_water}")
