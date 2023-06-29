message = list(input())
num_list = [int(num) for num in message if num.isdigit()]
message = [symbol for symbol in message if not symbol.isdigit()]
take_list = num_list[::2]
skip_list = num_list[1::2]
result = []

for n, m in zip(take_list, skip_list):
    result.extend(message[:n])
    message = message[n + m:]

print(''.join(result))

# message = list(input())
# num_list = [int(num) for num in message if num.isdigit()]
# message = [symbol for symbol in message if not symbol.isdigit()]
# result = []
#
# for idx in range(0, len(num_list), 2):
#     n = num_list[idx]
#     m = num_list[idx + 1] if idx + 1 < len(num_list) else 0
#     result.extend(message[:n])
#     message = message[n + m:]
#
# print(''.join(result))
