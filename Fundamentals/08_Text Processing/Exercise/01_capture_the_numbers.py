def valid_by_len(user_name):
    if 3 <= len(user_name) <= 16:
        return True
    return False


def valid_characters(user_name):
    for ch in user_name:
        if not (ch.isalnum() or ch == "-" or ch == "_"):
            return False
    return True


def no_redundant_symbols(user_name):
    if " " in user_name:
        return False
    return True


def valid_user_name(user_name):
    if valid_by_len(user_name) and valid_characters(user_name) and no_redundant_symbols(user_name):
        return True


names = input().split(", ")

for name in names:
    if valid_user_name(name):
        print(name)
