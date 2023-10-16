from collections import deque, defaultdict

programming_time = deque(int(el) for el in input().split())
tasks = [int(el) for el in input().split()]
duck_range = {
    "Darth Vader Ducky": slice(0, 61),
    "Thor Ducky": slice(61, 121),
    "Big Blue Rubber Ducky": slice(121, 181),
    "Small Yellow Rubber Ducky": slice(181, 241),
}
ducks = defaultdict(int)

while programming_time and tasks:
    current_time = programming_time.popleft()
    current_task = tasks.pop()

    result = current_time * current_task
    matched_duck = None
    for duck, duck_slice in duck_range.items():
        if duck_slice.start <= result < duck_slice.stop:
            matched_duck = duck
            break

    if matched_duck:
        ducks[matched_duck] += 1
    else:
        current_task -= 2
        tasks.append(current_task)
        programming_time.append(current_time)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")

for key in duck_range.keys():
    print(f"{key}: {ducks[key]}")
