from collections import deque


def convert_time(str_time):
    h, m, s = [int(x) for x in str_time.split(":")]
    return h * 3600 + m * 60 + s


def format_time(seconds):
    seconds %= 86400
    h = seconds // 3600
    seconds %= 3600
    m = seconds // 60
    seconds %= 60
    return f"{h:02d}:{m:02d}:{seconds:02d}"


robots_data = input().split(";")
start_time = convert_time(input())
robots = {}
robots_busy_to = {}

for data in robots_data:
    name, sec = data.split("-")
    robots[name] = int(sec)
    robots_busy_to[name] = -1

products = deque()
product = input()

while product != "End":
    products.append(product)
    product = input()

while products:
    start_time += 1
    item = products.popleft()
    for name, time in robots_busy_to.items():
        if start_time >= time:
            robots_busy_to[name] = start_time + robots[name]
            print(f"{name} - {item} [{format_time(start_time)}]")
            break
    else:
        products.append(item)
