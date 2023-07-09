import re

key = input().split()
command = input()
decrypt_message = ''

while command != "find":
    for idx, char in enumerate(command):
        index = idx % len(key)
        decrypt_message += chr(ord(char) - int(key[index]))

    treasure_type = re.search(r'&(\w+)&', decrypt_message).group(1)
    coordinates = re.search(r'<(\w+)>', decrypt_message).group(1)

    print(f"Found {treasure_type} at {coordinates}")
    command = input()
    decrypt_message = ''
