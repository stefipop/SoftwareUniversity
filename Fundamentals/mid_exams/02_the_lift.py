people_waiting = int(input())
current_state = [int(x) for x in input().split()]
for i in range(len(current_state)):
    max_people = min(4 - current_state[i], people_waiting)
    current_state[i] += max_people
    people_waiting -= max_people
if people_waiting > 0:
    print(f"There isn't enough space! {people_waiting} people in a queue!")
elif len(current_state) * 4 > sum(current_state):
    print("The lift has empty spots!")
print(*current_state)
