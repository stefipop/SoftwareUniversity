message = input()
command = input()

while command != "Decode":
    instruction = command.split("|")
    if instruction[0] == "Move":
        letters = int(instruction[1])
        message = message[letters:] + message[:letters]
    elif instruction[0] == "Insert":
        index = int(instruction[1])
        value = instruction[2]
        message = message[:index] + value + message[index:]
    else:
        substring = instruction[1]
        replacement = instruction[2]
        message = message.replace(substring, replacement)
    command = input()

print(f"The decrypted message is: {message}")
