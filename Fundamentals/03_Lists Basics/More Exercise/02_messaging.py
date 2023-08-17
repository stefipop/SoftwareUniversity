number_list = input().split()
sentence = list(input())
message = []
for num in number_list:
    digit_sum = 0
    for digit in num:
        digit_sum += int(digit)
    index = digit_sum % len(sentence)
    message.append(sentence[index])
    sentence.pop(index)
print(''.join(message))
