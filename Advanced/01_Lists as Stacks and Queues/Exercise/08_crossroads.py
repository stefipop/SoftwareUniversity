from collections import deque

green_duration = int(input())
yellow_duration = int(input())
cars = deque()
count = 0

command = input()
while command != "END":
    if command != "green":
        cars.append(command)
    elif command == "green":
        duration = green_duration
        while cars and duration > 0:
            current_car = cars.popleft()
            if duration >= len(current_car) or duration + yellow_duration >= len(current_car):
                count += 1
                duration -= len(current_car)
            else:
                print("A crash happened!")
                print(f"{current_car} was hit at {current_car[duration + yellow_duration]}.")
                exit()

    command = input()

else:
    print("Everyone is safe.")
    print(f"{count} total cars passed the crossroads.")
