from collections import deque

count_killed = 0
monster_armor = deque(int(el) for el in input().split(","))
soldier_strikes = [int(el) for el in input().split(",")]

while monster_armor and soldier_strikes:
    current_monster = monster_armor.popleft()
    current_soldier = soldier_strikes.pop()

    if current_soldier >= current_monster:
        count_killed += 1
        current_soldier -= current_monster
        if not soldier_strikes and current_soldier > 0:
            soldier_strikes.append(current_soldier)
        elif soldier_strikes:
            soldier_strikes[-1] += current_soldier
    else:
        current_monster -= current_soldier
        monster_armor.append(current_monster)

if not monster_armor:
    print("All monsters have been killed!")
if not soldier_strikes:
    print("The soldier has been defeated.")
# if count_killed:
print(f"Total monsters killed: {count_killed}")
