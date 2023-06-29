# def check_rooms(num_rooms):
#     free_chairs = 0
#     for room in range(1, num_rooms + 1):
#         current_free_chairs, visitors = input().split()
#         diff = len(current_free_chairs) - int(visitors)
#         if diff < 0:
#             print(f"{abs(diff)} more chairs needed in room {room}")
#             free_chairs += diff
#         else:
#             free_chairs += diff
#     return free_chairs
#
#
# rooms_count = int(input())
# total_free_chairs = check_rooms(rooms_count)
# if total_free_chairs >= 0:
#     print(f"Game On, {total_free_chairs} free chairs left")

rooms = int(input())
free_chairs = 0
game_on = True
for room in range(1, rooms + 1):
    chairs, str_guests = input().split()
    guests = int(str_guests)
    if guests > len(chairs):
        needed_chairs = guests - len(chairs)
        print(f"{needed_chairs} more chairs needed in room {room}")
        game_on = False
    else:
        free_chairs_by_row = len(chairs) - guests
        free_chairs += free_chairs_by_row
if game_on:
    print(f"Game On, {free_chairs} free chairs left")
