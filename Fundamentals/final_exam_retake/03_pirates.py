command = input()
city_population = {}
city_gold = {}

while command != "Sail":
    cities, population, gold = command.split("||")
    city_population.setdefault(cities, 0)
    city_gold.setdefault(cities, 0)
    city_population[cities] += int(population)
    city_gold[cities] += int(gold)
    command = input()

actions = input()

while actions != "End":
    action, town, info = actions.split("=>", 2)
    if action == "Plunder":
        people, gold = info.split("=>")
        city_population[town] -= int(people)
        city_gold[town] -= int(gold)
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if city_population[town] <= 0 or city_gold[town] <= 0:
            print(f"{town} has been wiped off the map!")
            del city_population[town]
            del city_gold[town]
    else:
        gold = int(info)
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            city_gold[town] += gold
            print(f"{info} gold added to the city treasury. {town} now has {city_gold[town]} gold.")

    actions = input()

if not city_gold:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(city_gold)} wealthy settlements to go to:")
    for town, population in city_population.items():
        print(f"{town} -> Population: {population} citizens, Gold: {city_gold[town]} kg")
