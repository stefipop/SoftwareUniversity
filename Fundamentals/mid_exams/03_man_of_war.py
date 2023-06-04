pirate_status = [int(x) for x in input().split(">")]
warship_status = [int(x) for x in input().split(">")]
maximum_health = int(input())
end_command = input()

while end_command != "Retire":
    command, *data = end_command.split()
    if command == "Fire":
        index, damage = map(int, data)
        if 0 <= index < len(warship_status):
            warship_status[index] -= damage
            if warship_status[index] <= 0:
                print("You won! The enemy ship has sunken.")
                exit()
    elif command == "Defend":
        start, end, damage = map(int, data)
        if 0 <= start <= end < len(pirate_status):
            for index in range(start, end + 1):
                pirate_status[index] -= damage
                if pirate_status[index] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    exit()
    elif command == "Repair":
        index, health = map(int, data)
        if 0 <= index < len(pirate_status):
            pirate_status[index] += health
            if pirate_status[index] > maximum_health:
                pirate_status[index] = maximum_health
    elif command == "Status":
        low_health = maximum_health * 0.2
        bad_section = [x for x in pirate_status if x < low_health]
        print(f"{len(bad_section)} sections need repair.")
    end_command = input()
else:
    print(f"Pirate ship status: {sum(pirate_status)}")
    print(f"Warship status: {sum(warship_status)}")
