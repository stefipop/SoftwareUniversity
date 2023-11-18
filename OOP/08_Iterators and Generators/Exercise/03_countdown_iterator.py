class countdown_iterator:
    def __init__(self, count: int) -> None:
        self.count = count

    def __iter__(self) -> 'countdown_iterator':
        return self

    def __next__(self) -> int:
        if self.count >= 0:
            temp = self.count
            self.count -= 1
            return temp
        else:
            raise StopIteration


# iterator = countdown_iterator(10)
# for item in iterator:
#     print(item, end=" ")
# iterator = countdown_iterator(0)
# for item in iterator:
#     print(item, end=" ")
