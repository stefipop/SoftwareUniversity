dungeon_rooms = input().split("|")
initial_health = 100
initial_bitcoins = 0

for room, room_info in enumerate(dungeon_rooms):
    info, amount = room_info.split()
    amount = int(amount)

    if info == "potion":
        if initial_health + amount > 100:
            amount = 100 - initial_health
        initial_health += amount
        print(f"You healed for {amount} hp.")
        print(f"Current health: {initial_health} hp.")

    elif info == "chest":
        initial_bitcoins += amount
        print(f"You found {amount} bitcoins.")

    else:
        if amount >= initial_health:
            print(f"You died! Killed by {info}.")
            print(f"Best room: {room + 1}")
            break

        initial_health -= amount
        print(f"You slayed {info}.")

else:
    print("You've made it!")
    print(f"Bitcoins: {initial_bitcoins}")
    print(f"Health: {initial_health}")
