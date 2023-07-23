def contains(raw_key, substring):
    if substring in raw_key:
        return f"{raw_key} contains {substring}"
    return f"Substring not found!"


def flipping(raw_key, upper_lower, first_i, second_i):
    if "Upper" in upper_lower:
        substring = raw_key[first_i:second_i].upper()
    else:
        substring = raw_key[first_i:second_i].lower()
    raw_key = raw_key[:first_i] + substring + raw_key[second_i:]
    return raw_key


def slicing(raw_key, first_i, second_i):
    raw_key = raw_key[:first_i] + raw_key[second_i:]
    return raw_key


text = input()
command = input()

while command != "Generate":
    action, info = command.split(">>>", 1)
    if action == "Contains":
        print(contains(text, info))
    elif action == "Flip":
        case, start, end = info.split(">>>")
        text = flipping(text, case, int(start), int(end))
        print(text)
    else:
        start, end = info.split(">>>")
        text = slicing(text, int(start), int(end))
        print(text)
    command = input()

print(f"Your activation key is: {text}")
