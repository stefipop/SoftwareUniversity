# main_string = input()
#
# list_result = []
# total = 0
# items = main_string.split("|")
# for item in items:
#     if "#" in item:
#         item_parts = item.split("#")
#         item_name = item_parts[1]
#         item_date = item_parts[2]
#         item_calories = item_parts[3]
#         total += int(item_calories)
#         list_result.append({"name": item_name, "date": item_date, "nutrition": item_calories})
#
# total = total // 2000
#
# print(f"You have food to last you for: {total} days!")
# for item in list_result:
#     print(f"Item: {item['name']}, Best before: {item['date']}, Nutrition: {item['nutrition']}")

electrons_count = int(input())
shell = 1
electrons_in_shells = []

while electrons_count > 0:
    max_electrons = 2 * shell**2
    electrons = min(electrons_count, max_electrons)
    electrons_in_shells.append(electrons)
    electrons_count -= electrons
    shell += 1
print(electrons_in_shells)

# for electrons in range(1, max_electrons + 1):
#     electrons_count -= 1
#     if electrons_count == 0:
#         break