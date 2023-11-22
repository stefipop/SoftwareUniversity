from typing import Any, Iterable, Generator, Union

def read_next(*args: Union[str, Iterable, dict]) -> Generator[Any, None, None]:
    for element in args:
        for iterable in element:
            yield iterable


for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')

# for i in read_next("Need", (2, 3), ["words", "."]):
#     print(i)
