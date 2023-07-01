n = int(input())

for _ in range(n):
    number = int(input())
    if number % 2 != 0:
        print(f"{number} is odd!")
        break
else:
    print("All numbers are even.")


# is_even = True
# for _ in range(n):
#     number = int(input())
#     if number % 2 != 0:
#         is_even = False
#         print(f"{number} is odd!")
#         break
# if is_even:
#     print("All numbers are even.")
