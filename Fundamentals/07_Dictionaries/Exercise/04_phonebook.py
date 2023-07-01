phonebook = {}
data = input()

while "-" in data:
    person, phone = data.split('-')
    phonebook[person] = phone
    data = input()

for _ in range(int(data)):
    name = input()
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")
