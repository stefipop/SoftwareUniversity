data = input()
result = {}

while data != "stop":
    # if data in result:
    #     result[data] += int(input())
    # else:
    #     result[data] = int(input())
    quantity = int(input())
    result[data] = result.get(data, 0) + quantity
    data = input()

for k, v in result.items():
    print(f"{k} -> {v}")
