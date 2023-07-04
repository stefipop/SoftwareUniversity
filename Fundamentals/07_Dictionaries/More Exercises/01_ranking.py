data = input()
contests = {}

while ":" in data:
    course, watchword = data.split(":")
    contests[course] = watchword
    data = input()

ranking = {}
command = input()

while "=>" in command:
    contest, password, name, points = command.split("=>")
    if contest in contests and contests[contest] == password:
        if name not in ranking:
            ranking[name] = {}
        if contest not in ranking[name] or int(points) > ranking[name][contest]:
            ranking[name][contest] = int(points)
    command = input()

sum_points = {}
for name, contest in ranking.items():
    total_points = sum(contest.values())
    sum_points[name] = total_points

best_contest = max(sum_points, key=sum_points.get)
best_points = sum_points[best_contest]
sorted_name = sorted(ranking.keys())

print(f"Best candidate is {best_contest} with total {best_points} points.")
print("Ranking:")
for name in sorted_name:
    print(name)
    for contest, points in sorted(ranking[name].items(), key=lambda x: x[1], reverse=True):
            print(f"#  {contest} -> {points}")