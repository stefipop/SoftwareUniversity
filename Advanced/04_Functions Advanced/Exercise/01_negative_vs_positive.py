def find_negative(*args):
    negative = sum([x for x in args if x < 0])
    return negative


def find_positive(*args):
    positive = sum([x for x in args if x > 0])
    return positive


def find_biggest(negative, positive):
    if abs(negative) > positive:
        return f"The negatives are stronger than the positives"
    else:
        return f"The positives are stronger than the negatives"


data = [int(x) for x in (input().split())]
neg_num = find_negative(*data)
pos_num = find_positive(*data)

print(neg_num)
print(pos_num)
print(find_biggest(neg_num, pos_num))
