class dictionary_iter:
    def __init__(self, dictionary: dict) -> None:
        self.items = list(dictionary.items())
        self.start = 0

    def __iter__(self) -> 'dictionary_iter':
        return self

    def __next__(self) -> tuple:
        if self.start < len(self.items):
            temp = self.items[self.start]
            self.start += 1
            return temp
        else:
            raise StopIteration


# result = dictionary_iter({1: "1", 2: "2"})
# for x in result:
#     print(x)
# result = dictionary_iter({"name": "Peter", "age": 24})
# for x in result:
#     print(x)
