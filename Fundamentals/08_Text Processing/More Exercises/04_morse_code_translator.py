morse_code_mapping = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z'
}


def decode_morse_code(morse_code):
    message = ''
    for word in morse_code:
        letters = word.split()
        for letter in letters:
            message += morse_code_mapping.get(letter, '')
        message += ' '
    return message.strip()


data = input().split(' | ')
decoded_message = decode_morse_code(data)

print(decoded_message)
