def find_max(lst, odd_or_even_list):
    if lst:
        max_num = max(odd_or_even_list)
        for i in range(len(lst) - 1, -1, -1):
            if lst[i] == max_num:
                return i
    return None


def find_min(lst, odd_or_even_list):
    if lst:
        min_num = min(odd_or_even_list)
        for i in range(len(lst) - 1, -1, -1):
            if lst[i] == min_num:
                return i
    return None


def find_even(lst):
    return [num for num in lst if num % 2 == 0]


def find_odd(lst):
    return [num for num in lst if num % 2 != 0]


list_of_integers = [int(x) for x in input().split()]  # list(map(int, input().split()))
while True:
    command = input().split()
    if command[0] == "exchange":
        idx = int(command[1])
        if idx < 0 or idx >= len(list_of_integers):
            print("Invalid index")
        else:
            list_of_integers[idx + 1:], list_of_integers[:idx + 1] = list_of_integers[:idx + 1], list_of_integers[
                                                                                                 idx + 1:]
    elif command[0] == "max":
        if command[1] == "odd":
            odd_numbers = find_odd(list_of_integers)
            if odd_numbers:
                result = find_max(list_of_integers, find_odd(list_of_integers))
            else:
                result = "No matches"
        elif command[1] == "even":
            even_numbers = find_even(list_of_integers)
            if even_numbers:
                result = find_max(list_of_integers, find_even(list_of_integers))
            else:
                result = "No matches"
        print(result)
    elif command[0] == "min":
        if command[1] == "odd":
            odd_numbers = find_odd(list_of_integers)
            if odd_numbers:
                result = find_min(list_of_integers, find_odd(list_of_integers))
            else:
                result = "No matches"
        elif command[1] == "even":
            even_numbers = find_even(list_of_integers)
            if even_numbers:
                result = find_min(list_of_integers, find_even(list_of_integers))
            else:
                result = "No matches"
        print(result)
    elif command[0] in {"first", "last"}:
        counter = int(command[1])
        if command[2] == "odd":
            filtered = find_odd(list_of_integers)
        elif command[2] == "even":
            filtered = find_even(list_of_integers)
        if counter > len(list_of_integers):
            print("Invalid count")
        else:
            if command[0] == "first":
                result = filtered[:counter]
            else:
                result = filtered[-counter:]
            print(result)
    else:
        break

print(list_of_integers)
