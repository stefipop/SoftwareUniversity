def solution():
    def integers(num: int = 1) -> 'Iterator[int]':
        while True:
            yield num
            num += 1

    def halves() -> 'Iterator[float]':
        for num in integers():
            yield num / 2

    def take(n: int, seq: 'Iterator[T]') -> 'List[T]':
        result = []
        for _ in range(n):
            result.append(next(seq))
        return result

    return take, halves, integers



# take = solution()[0]
# halves = solution()[1]
# print(take(5, halves()))
# take = solution()[0]
# halves = solution()[1]
# print(take(0, halves()))
