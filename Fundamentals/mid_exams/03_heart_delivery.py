neighborhood = [int(x) for x in input().split("@")]
user_input = (input().split())
last_position = 0

while user_input[0] != "Love!":
    length = int(user_input[1])
    last_position += length
    if last_position >= len(neighborhood):
        last_position = 0
    if neighborhood[last_position] != 0:
        neighborhood[last_position] -= 2
        if neighborhood[last_position] == 0:
            print(f"Place {last_position} has Valentine's day.")
    else:
        print(f"Place {last_position} already had Valentine's day.")
    user_input = (input().split())

print(f"Cupid's last position was {last_position}.")
if sum(neighborhood) == 0:
    print("Mission was successful.")
else:
    house_count = len(neighborhood) - neighborhood.count(0)
    print(f"Cupid has failed {house_count} places.")


# house_count = 0
# for hearts in neighborhood:
#     if hearts != 0:
#         house_count += 1

# house_count = len(list(filter(lambda x: x != 0, neighborhood)))
