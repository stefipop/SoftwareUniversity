class reverse_iter:
    def __init__(self, args) -> None:
        self.start = len(args) - 1
        self.end = 0
        self.args = args

    def __iter__(self) -> 'reverse_iter':
        return self

    def __next__(self):
        if self.start < self.end:
            raise StopIteration
        current = self.start
        self.start -= 1
        return self.args[current]


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
