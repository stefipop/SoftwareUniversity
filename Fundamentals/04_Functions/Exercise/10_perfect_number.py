def aliquot_sum(num: int) -> str:
    divisor_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisor_sum += i
    if num == divisor_sum:
        return "We have a perfect number!"
    return "It's not so perfect."


number_input = int(input())
print(aliquot_sum(number_input))
