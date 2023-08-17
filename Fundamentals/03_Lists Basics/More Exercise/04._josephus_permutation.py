people_count = input().split()
sequence = int(input())
executed = []
idx = 0
while len(people_count) > 0:
    idx = (idx + sequence - 1) % len(people_count)
    executed.append(people_count.pop(idx))
print(f"[{','.join(executed)}]")
