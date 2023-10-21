from collections import deque

seats = set(input().split(", "))
first = deque(input().split(", "))
second = deque(input().split(", "))
rotations = 0
seat_matches = []

while True:
    if len(seat_matches) == 3:
        break
    if rotations == 10:
        break

    num1, num2 = first[0], second[-1]
    letter = chr(int(num1) + int(num2))
    possible_seats = {num1 + letter, num2 + letter}
    result = seats & possible_seats

    if result:
        seat = result.pop()
        seat_matches.append(seat)
        seats.discard(seat)
        first.popleft()
        second.pop()
    else:
        first.rotate(-1)
        second.rotate(1)
    rotations += 1

print(f"Seat matches: {', '.join(seat_matches)}")
print(f"Rotations count: {rotations}")
