def is_valid_length(user_input):
    return 6 <= len(user_input) <= 10


def contains_alpha_num_chars(user_input):
    return password.isalnum()


def contains_at_least_two_digits(user_input):
    digit_count = 0
    for ch in user_input:
        if ch.isdigit():
            digit_count += 1
    return digit_count >= 2


password = input()
is_valid = True

if not is_valid_length(password):
    is_valid = False
    print("Password must be between 6 and 10 characters")
if not contains_alpha_num_chars(password):
    is_valid = False
    print("Password must consist only of letters and digits")
if not contains_at_least_two_digits(password):
    is_valid = False
    print("Password must have at least 2 digits")
if is_valid:
    print("Password is valid")


# def length_validation(password):
#     if len(password) < 6 or len(password) > 10:
#         print("Password must be between 6 and 10 characters")
#         return False
#     return True
#
#
# def symbols_validation(password):
#     if not password.isalnum():
#         print("Password must consist only of letters and digits")
#         return False
#     return True
#
#
# def two_digits_validation(password):
#     counter_of_digits = 0
#     for character in password:
#         if character.isdigit():
#             counter_of_digits += 1
#     if counter_of_digits < 2:
#         print("Password must have at least 2 digits")
#         return False
#     return True
#
#
# some_password = input()
# password_is_valid = [length_validation(some_password),
#                      symbols_validation(some_password),
#                      two_digits_validation(some_password)]
#
# if all(password_is_valid):
#     print("Password is valid")
