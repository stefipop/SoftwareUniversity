command_count = int(input())
parking_list = {}

for _ in range(command_count):
    data = input().split()
    name = data[1]
    if "register" in data:
        plate_num = data[2]
        if name in parking_list:
            print(f"ERROR: already registered with plate number {plate_num}")
        else:
            parking_list[name] = plate_num
            print(f"{name} registered {plate_num} successfully")
    else:
        if name in parking_list:
            print(f"{name} unregistered successfully")
            del parking_list[name]
        else:
            print(f"ERROR: user {name} not found")

for k, v in parking_list.items():
    print(f"{k} => {v}")
