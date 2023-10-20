from collections import deque, defaultdict

textiles = deque(int(el) for el in input().split())
medicaments = [int(el) for el in input().split()]
count_items = defaultdict(int)

while textiles and medicaments:
    current_textile = textiles.popleft()
    current_med = medicaments.pop()
    result = current_textile + current_med

    if result == 30:
        count_items["Patch"] += 1
    elif result == 40:
        count_items["Bandage"] += 1
    elif result == 100:
        count_items["MedKit"] += 1
    elif result > 100:
        count_items["MedKit"] += 1
        medicaments[-1] += result - 100
    else:
        current_med += 10
        medicaments.append(current_med)


if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")

sorted_items = sorted(count_items.items(), key=lambda kvp: (-kvp[1], kvp[0]))

for item, amount in sorted_items:
    print(f"{item} - {amount}")

if textiles:
    print(f"Textiles left: {', '.join(map(str, textiles))}")
if medicaments:
    medicaments.reverse()
    print(f"Medicaments left: {', '.join(map(str, medicaments))}")
