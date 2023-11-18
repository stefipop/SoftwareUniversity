# from itertools import permutations
#
# def possible_permutations(args):
#     for perm in permutations(args):
#         yield list(perm)
def possible_permutations(lst):
    if len(lst) == 0:
        yield []
    else:
        for i in range(len(lst)):
            rest = lst[:i] + lst[i + 1:]
            for p in possible_permutations(rest):
                yield [lst[i]] + p


# [print(n) for n in possible_permutations([1, 2, 3])]
# [print(n) for n in possible_permutations([1])]