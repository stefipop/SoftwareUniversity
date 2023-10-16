from os import path, remove


def create_file(filename):
    open(filename, "w").close()


def add_to_file(filename, content):
    with open(filename, "a") as file:
        file.write(content + "\n")


def replace_in_file(filename, old_str, new_str):
    if not path.exists(filename):
        print("An error occurred")
        return

    with open(filename, "r") as file:
        new_content = file.read().replace(old_str, new_str)

    with open(filename, "w") as file:
        file.write(new_content)


def delete_file(filename):
    if path.exists(filename):
        remove(filename)
    else:
        print("An error occurred")


user_input = input()
while user_input != "End":
    commands = user_input.split('-')
    if commands[0] == "Create":
        create_file(commands[1])
    elif commands[0] == "Add":
        add_to_file(commands[1], commands[2])
    elif commands[0] == "Replace":
        replace_in_file(commands[1], commands[2], commands[3])
    else:
        delete_file(commands[1])
    user_input = input()
