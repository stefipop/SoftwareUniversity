def loading_bar(num):
    loading_str = ''
    for i in range(10, 101, 10):
        if i <= num:
            loading_str += "%"
        else:
            loading_str += "."
    if num < 100:
        print(f"{num}% [{loading_str}]")
        print("Still loading...")
    else:
        print("100% Complete!")
        print(f"[{loading_str}]")


number_input = int(input())
loading_bar(number_input)


# def loading_bar(some_number):
#     if some_number == 100:
#         return "100% Complete!\n[%%%%%%%%%%]"
#     loaded_percents = some_number // 10
#     return f"{some_number}% [{'%' * loaded_percents}{'.' * (10 - loaded_percents)}]\nStill loading..."
#
#
# number = int(input())
# print(loading_bar(number))