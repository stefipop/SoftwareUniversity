phonebook = {}
data = input()

while "-" in data:
    person, phone = data.split('-')
    phonebook[person] = phone
    data = input()

num = int(data)

for _ in range(num):
    name = input()
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")
