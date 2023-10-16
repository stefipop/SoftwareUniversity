word = input()

try:
    times = int(input())
except ValueError:
    print("Variable times must be an integer")
else:
    print(word * times)
