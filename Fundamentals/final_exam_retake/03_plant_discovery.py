number = int(input())
plant_list, average_rating = {}, {}

for i in range(number):
    plant, rarity = input().split("<->")
    plant_list[plant] = int(rarity)
    average_rating[plant] = []

command = input()

while command != "Exhibition":
    action, info = command.split(": ", 1)
    if action == "Rate":
        plant, rating = info.split(" - ")
        if plant not in plant_list:
            print("error")
        else:
            average_rating[plant].append(int(rating))
    elif action == "Update":
        plant, new_rarity = info.split(" - ")
        if plant not in plant_list:
            print("error")
        else:
            plant_list[plant] = int(new_rarity)
    else:
        if info not in plant_list:
            print("error")
        else:
            average_rating[info] = []
    command = input()


print(f"Plants for the exhibition:")
for plant, ratings in average_rating.items():
    if not ratings:
        average = 0
    else:
        average = sum(ratings) / len(ratings)
    print(f"- {plant}; Rarity: {plant_list[plant]}; Rating: {average:.2f}")
