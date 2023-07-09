start_char = input()
end_char = input()
text = input()
ascii_sum = 0

for char in text:
    if start_char < char < end_char:
        ascii_sum += ord(char)

print(ascii_sum)
