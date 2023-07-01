# while True:
#     word = input()
#     if word == "End":
#         break
#     if word == "SoftUni":
#         continue
#     for ch in word:
#         print(f"{ch}{ch}", end = "")
#     print()

current_string = input()

while current_string != "End":
    if current_string != "SoftUni":
        new_string = ""

        for i in current_string:
            new_string += i * 2

        print(new_string)

    current_string = input()
