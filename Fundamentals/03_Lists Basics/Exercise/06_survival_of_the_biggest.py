numbers_string = input().split()
# num = [int(x) for x in input().split()]
n = int(input())

for i in range(len(numbers_string)):
    numbers_string[i] = int(numbers_string[i])

for i in range(n):
    min_element = min(numbers_string)
    numbers_string.remove(min_element)

for i in range(len(numbers_string)):
    numbers_string[i] = str(numbers_string[i])

print(', '.join(numbers_string))

# numbers_string = [int(x) for x in numbers_string]
# print(', '.join([str(x) for x in numbers_string]))
