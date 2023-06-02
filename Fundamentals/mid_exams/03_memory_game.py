turns = 0
elements = input().split()
user_input = input()

while user_input != "end":
    ind_1, ind_2 = sorted(map(int, user_input.split()))
    turns += 1
    if ind_1 == ind_2 or ind_1 not in range(len(elements)) or ind_2 not in range(len(elements)):
        ind_1 = len(elements) // 2
        elements.insert(ind_1, f"-{turns}a")
        elements.insert(ind_1 + 1, f"-{turns}a")
        print("Invalid input! Adding additional elements to the board")
    elif elements[ind_1] == elements[ind_2]:
        print(f"Congrats! You have found matching elements - {elements[ind_1]}!")
        elements.remove(elements[ind_1])
        elements.remove(elements[ind_2 - 1])
    else:
        print("Try again!")

    if not elements:
        print(f"You have won in {turns} turns!")
        break

    user_input = input()

if user_input == "end":
    print("Sorry you lose :(")
if elements:
    print(*elements)
