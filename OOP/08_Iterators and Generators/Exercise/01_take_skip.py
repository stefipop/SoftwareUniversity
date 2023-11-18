class take_skip:
    def __init__(self, step: int, count: int) -> None:
        self.step = step
        self.count = count
        self.current = 0

    def __iter__(self) -> 'take_skip':
        return self

    def __next__(self) -> int:
        if self.count > 0:
            result = self.current
            self.current += self.step
            self.count -= 1
            return result
        else:
            raise StopIteration


# numbers = take_skip(2, 6)
# for number in numbers:
#     print(number)
#
# numbers = take_skip(10, 5)
# for number in numbers:
#     print(number)
