class custom_range:
    def __init__(self, start: int, end: int) -> None:
        self.start: int = start
        self.end: int = end

    def __iter__(self) -> 'custom_range':
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        current = self.start
        self.start += 1
        return current


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
