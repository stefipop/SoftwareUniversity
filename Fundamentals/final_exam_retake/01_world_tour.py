stops = input()
command = input()


def add_stop(stops, index, new_stop):
    if 0 <= index < len(stops):
        return stops[:index] + new_stop + stops[index:]
    return stops


def remove_stop(stops, start, end):
    if 0 <= start < len(stops) and 0 <= end < len(stops):
        return stops[:start] + stops[end + 1:]
    return stops


def replace_stop(stops, old_stop, new_stop):
    if old_stop in stops:
        return stops.replace(old_stop, new_stop)
    return stops


while command != "Travel":
    action, stop_info_one, stop_info_two = command.split(":")
    if action == "Add Stop":
        index = int(stop_info_one)
        stops = add_stop(stops, index, stop_info_two)
    elif action == "Remove Stop":
        start = int(stop_info_one)
        end = int(stop_info_two)
        stops = remove_stop(stops, start, end)
    else:
        stops = replace_stop(stops, stop_info_one, stop_info_two)
    print(stops)
    command = input()

print(f"Ready for world tour! Planned stops: {stops}")


# stops = input()
# command = input()
#
# while command != "Travel":
#     action, info_one, info_two = command.split(":")
#     if action == "Add Stop":
#         index = int(info_one)
#         if index in range(len(stops)):
#             stops = stops[:index] + info_two + stops[index:]
#     elif action == "Remove Stop":
#         start = int(info_one)
#         end = int(info_two)
#         if start in range(len(stops)) and end in range(len(stops)):
#             stops = stops[:start] + stops[end + 1:]
#     else:
#         if info_one in stops:
#             stops = stops.replace(info_one, info_two)
#     print(stops)
#     command = input()
#
# else:
#     print(f"Ready for world tour! Planned stops: {stops}")
