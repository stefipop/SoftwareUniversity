contest = {}
users = {}
command = input()

while "->" in command:
    name, course, points = command.split(" -> ")
    points = int(points)
    users[name] = users.get(name, 0)
    contest.setdefault(course, {}).setdefault(name, 0)
    contest[course][name] = max(points, contest[course].get(name, 0))
    command = input()

for course, participants in contest.items():
    print(f"{course}: {len(contest[course])} participants")
    sorted_participants = sorted(participants.items(), key=lambda x: (-x[1], x[0]))
    for index, (name, points) in enumerate(sorted_participants, 1):
        users[name] += points
        print(f"{index}. {name} <::> {points}")

print("Individual standings:")
sorted_users = sorted(users.items(), key=lambda x: (-x[1], x[0]))
for index, (name, points) in enumerate(sorted_users, 1):
    print(f"{index}. {name} -> {points}")
