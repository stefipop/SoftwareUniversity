import re


def valid_destination(dest_data):
    pattern = r"(\=|\/)([A-Z][A-Za-z]{2,})\1"
    travel_points = 0
    valid_dest = []
    result = re.finditer(pattern, dest_data)

    for dest in result:
        valid_dest.append(dest.group(2))
        travel_points += len(dest.group(2))
    print(f"Destinations: {', '.join(valid_dest)}\nTravel Points: {travel_points}")


data = input()
valid_destination(data)
