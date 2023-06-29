# major, minor, patch = [int(x) for x in input().split('.')]
#
# patch += 1
# if patch == 10:
#     patch = 0
#     minor += 1
#     if minor == 10:
#         minor = 0
#         major += 1
#
# print(f"{major}.{minor}.{patch}")

version = int(input().replace(".", "")) + 1
print('.'.join(str(version)))


# version = [int(number) for number in input().split(".")]
# version[-1] += 1
# for index in range(len(version) -1, -1, -1):
#     if version[index] > 9 and index != 0:
#         version[index] = 0
#         if index -1 >=0:
#             version[index-1] += 1
# print(".".join(str(number) for number in version))
