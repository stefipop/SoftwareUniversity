total_energy = 100
total_coins = 100

events = input().split('|')
is_bankrupted = True

for event in events:
    event_info = event.split('-')
    event_type = event_info[0]
    event_number = int(event_info[1])
    if event_type == "rest":
        temporary_energy = total_energy
        total_energy += event_number
        if total_energy > 100:
            total_energy = 100
        gained_energy = total_energy - temporary_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {total_energy}.")
    elif event_type == "order":
        if total_energy - 30 >= 0:
            total_energy -= 30
            total_coins += event_number
            print(f"You earned {event_number} coins.")
        else:
            total_energy += 50
            if total_energy > 100:
                total_energy = 100
            print("You had to rest!")
    else:
        if total_coins >= event_number:
            total_coins -= event_number
            print(f"You bought {event_type}.")
        else:
            print(f"Closed! Cannot afford {event_type}.")
            is_bankrupted = False
            break

if is_bankrupted:
    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")
