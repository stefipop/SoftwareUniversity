# text = input()
# command = input()
#
# while command != "Done":
#     command = command.split()
#     if command[0] == "TakeOdd":
#         text = text[1::2]
#         print(text)
#     elif command[0] == "Cut":
#         index, length = int(command[1]), int(command[2])
#         # substring = text[index:index + length]
#         # text = text.replace(substring, "", 1)
#         text = text[:index] + text[index + length:]
#         print(text)
#     else:
#         substring, substitute = command[1], command[2]
#         if substring in text:
#             text = text.replace(substring, substitute)
#             print(text)
#         else:
#             print("Nothing to replace!")
#
#     command = input()
#
# print(f"Your password is: {text}")


def take_odd(password):
    new_password = password[1::2]
    print(new_password)
    return new_password


def cut(password, index, length):
    index, length = int(index), int(length)
    password = password[:index] + password[index + length:]
    print(password)
    return password


def substitute(password, substring, substitute):
    if substring in password:
        password = password.replace(substring, substitute)
        print(password)
    else:
        print("Nothing to replace!")
    return password


text = input()
command = input()

while command != "Done":
    command = command.split()
    if command[0] == "TakeOdd":
        text = take_odd(text)
    elif command[0] == "Cut":
        text = cut(text, command[1], command[2])
    elif command[0] == "Substitute":
        text = substitute(text, command[1], command[2])
    command = input()

print(f"Your password is: {text}")
