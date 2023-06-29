def make_letter(any_word):
    sum_symbols = ''
    for symbol in any_word:
        if symbol.isdigit():
            sum_symbols += symbol
        else:
            break
    hidden_letter = chr(int(sum_symbols))
    return sum_symbols, hidden_letter


def change_position(word):
    word = list(word)
    word[1], word[-1] = word[-1], word[1]
    return ''.join(word)


secret_message = input().split()
for i in range(len(secret_message)):
    digits, secret_letter = make_letter(secret_message[i])
    secret_message[i] = secret_message[i].replace(digits, secret_letter)
    secret_message[i] = change_position(secret_message[i])

print(' '.join(secret_message))


# def make_letter(any_word):
#     digits = ''.join(filter(str.isdigit, any_word))
#     secret_letter = chr(int(digits))
#     return digits, secret_letter
#
#
# def change_position(word):
#     word = list(word)
#     word[1], word[-1] = word[-1], word[1]
#     return ''.join(word)
#
#
# secret_message = input().split()
# secret_message = [change_position(word.replace(*make_letter(word))) for word in secret_message]
#
# print(' '.join(secret_message))

