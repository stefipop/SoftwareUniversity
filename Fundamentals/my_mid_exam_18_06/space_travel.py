travel_route = input().split("||")
fuel = int(input())
ammunition = int(input())

for idx, info in enumerate(travel_route):
    command, *amount = info.split(" ")
    amount = int(amount[0]) if amount else 0

    if command == "Travel":
        if fuel >= amount:
            fuel -= amount
            print(f"The spaceship travelled {amount} light-years.")
        else:
            print("Mission failed.")
            break
    elif command == "Enemy":
        if ammunition >= amount:
            ammunition -= amount
            print(f"An enemy with {amount} armour is defeated.")
        elif ammunition < amount:
            if fuel >= amount * 2:
                fuel -= amount * 2
                print(f"An enemy with {amount} armour is outmaneuvered.")
            else:
                print("Mission failed.")
                break
    elif command == "Repair":
        fuel += amount
        ammunition += amount * 2
        print(f"Ammunitions added: {amount * 2}.")
        print(f"Fuel added: {amount}.")
    else:
        print("You have reached Titan, all passengers are safe.")
        break
