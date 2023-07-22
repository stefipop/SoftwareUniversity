concealed = input()
command = input()

while command != "Reveal":
    action, details = command.split(":|:", 1)

    if action == "InsertSpace":
        index = int(details)
        concealed = concealed[:index] + " " + concealed[index:]
        print(concealed)

    elif action == "Reverse":
        if details in concealed:
            rev_details = details[::-1]
            concealed = concealed.replace(details, "", 1)
            concealed += rev_details
            print(concealed)
        else:
            print("error")

    elif action == "ChangeAll":
        substring, replacement = details.split(":|:")
        concealed = concealed.replace(substring, replacement)
        print(concealed)

    command = input()

print(f"You have a new text message: {concealed}")