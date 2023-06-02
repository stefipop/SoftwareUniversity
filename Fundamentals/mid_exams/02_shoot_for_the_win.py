targets = [int(x) for x in input().split()]
user_input = input()
counter = 0
target_idx = 0

while user_input != "End":
    indices = int(user_input)
    if 0 <= indices < len(targets):
        counter += 1
        target_idx = targets[indices]
        targets[indices] = -1
        for idx in range(len(targets)):
            if targets[idx] != -1 and targets[idx] <= target_idx:
                targets[idx] += target_idx
            elif targets[idx] != -1 and targets[idx] > target_idx:
                targets[idx] -= target_idx
    user_input = input()

print(f"Shot targets: {counter} -> ", end='')
print(*targets, sep=' ')
