def multiplication_sign(a, b, c):
    if a > 0 and (b < 0 and c < 0):
        return "positive"
    elif b > 0 and (a < 0 and c < 0):
        return "positive"
    elif c > 0 and (a < 0 and b < 0):
        return "positive"
    elif a == 0 or b == 0 or c == 0:
        return "zero"
    elif a < 0 or b < 0 or c < 0:
        return "negative"
    else:
        return "positive"


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

answer = multiplication_sign(num_1, num_2, num_3)
print(answer)
