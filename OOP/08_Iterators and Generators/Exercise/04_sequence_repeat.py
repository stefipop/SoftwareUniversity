class sequence_repeat:
    def __init__(self, sequence: str, number: int) -> None:
        self.sequence = sequence
        self.number = number
        self.index = 0

    def __iter__(self) -> 'sequence_repeat':
        return self

    def __next__(self) -> str:
        if self.number == 0:
            raise StopIteration

        temp = self.sequence[self.index]
        self.index = (self.index + 1) % len(self.sequence)
        self.number -= 1

        return temp

# from itertools import cycle
#
#
# class sequence_repeat:
#     def __init__(self, sequence: str, number: int) -> None:
#         self.sequence = cycle(sequence)
#         self.number = number
#
#     def __iter__(self) -> 'sequence_repeat':
#         return self
#
#     def __next__(self) -> str:
#         if self.number == 0:
#             raise StopIteration
#         temp = next(self.sequence)
#         self.number -= 1
#         return temp


# result = sequence_repeat('abc', 5)
# for item in result:
#     print(item, end='')
# result = sequence_repeat('I Love Python', 3)
# for item in result:
#     print(item, end='')
