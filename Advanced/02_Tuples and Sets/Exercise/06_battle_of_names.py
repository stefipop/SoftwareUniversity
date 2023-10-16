n = int(input())
even_set = set()
odd_set = set()

for row in range(1, n + 1):
    name_sum = sum([ord(ch) for ch in input()]) // row
    if name_sum % 2 == 0:
        even_set.add(name_sum)
    else:
        odd_set.add(name_sum)

if sum(odd_set) == sum(even_set):
    result = odd_set | even_set
elif sum(odd_set) > sum(even_set):
    result = odd_set - even_set
else:
    result = odd_set ^ even_set
# if sum(odd_set) == sum(even_set):
#     result = odd_set.union(even_set)
# elif sum(odd_set) > sum(even_set):
#     result = odd_set.difference(even_set)
# else:
#     result = odd_set.symmetric_difference(even_set)

print(*result, sep=", ")
