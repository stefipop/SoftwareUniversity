initial_energy = int(input())
user_input = input()
winnings = 0

while user_input != "End of battle":
    distance = int(user_input)
    if initial_energy >= distance:
        initial_energy -= distance
        winnings += 1
        if winnings % 3 == 0:
            initial_energy += winnings
    else:
        print(f"Not enough energy! Game ends with {winnings} won battles and {initial_energy} energy")
        break
    user_input = input()

if user_input == "End of battle":
    print(f"Won battles: {winnings}. Energy left: {initial_energy}")
