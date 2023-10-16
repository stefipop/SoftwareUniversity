from collections import deque

n = int(input())
pumps = deque()
stops = 0

for _ in range(n):
    current_fuel, distance = input().split()
    pumps.append([int(current_fuel), int(distance)])
# pumps = deque(list(map(int, input().split())) for _ in range(int(input())))
# pumps = deque([int(x) for x in input().split()] for _ in range(int(input())))

# while stops < n:
#     fuel = 0
#     for i in range(n):
#         fuel += pumps[i][0]
#         if fuel >= pumps[i][1]:
#             fuel -= pumps[i][1]
#         else:
#             break
#     else:
#         break
#     pumps.rotate(-1)
#     stops += 1
#
# print(stops)

pumps_data = pumps.copy()
fuel = 0
index = 0

while pumps_data:
    liters, distance = pumps_data.popleft()
    fuel += liters

    if fuel >= distance:
        fuel -= distance
    else:
        pumps.rotate(-1)
        pumps_data = pumps.copy()
        index += 1
        fuel = 0

print(index)
