from collections import deque

# bullet_price = int(input())
# gun_size = int(input())
# bullets = [int(x) for x in input().split()]
# locks = deque(int(x) for x in input().split())
# value = int(input())
# fired_bullets = 0
# size = gun_size
#
# while bullets and locks:
#     if bullets and size > 0:
#         current_bullet = bullets.pop()
#         fired_bullets += 1
#         size -= 1
#         if locks and locks[0] >= current_bullet:
#             print("Bang!")
#             locks.popleft()
#         elif locks and locks[0] < current_bullet:
#             print("Ping!")
#     if bullets and size <= 0:
#         print("Reloading!")
#         size = gun_size
#         continue
#
# if not locks:
#     money_earned = value - (fired_bullets * bullet_price)
#     print(f"{len(bullets)} bullets left. Earned ${money_earned}")
# else:
#     print(f"Couldn't get through. Locks left: {len(locks)}")


bullet_price = int(input())
gun_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque(map(int, input().split()))
value = int(input())
fired_bullets = 0

while bullets and locks:
    current_bullet = bullets.pop()
    fired_bullets += 1

    if current_bullet <= locks[0]:
        print("Bang!")
        locks.popleft()
    else:
        print("Ping!")

    if fired_bullets % gun_size == 0 and bullets:
        print("Reloading!")

if not locks:
    money_earned = value - (fired_bullets * bullet_price)
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
