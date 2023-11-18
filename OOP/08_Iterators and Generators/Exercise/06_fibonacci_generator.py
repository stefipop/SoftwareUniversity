# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b

from typing import Generator

def fibonacci() -> Generator[int, None, None]:
    fibonacci_seq: list[int] = [0, 1]
    while True:
        new_number = fibonacci_seq[-2] + fibonacci_seq[-1]
        yield fibonacci_seq[-2]
        fibonacci_seq = fibonacci_seq[-2:]  # Keep only the last two numbers
        fibonacci_seq.append(new_number)



# generator = fibonacci()
# for i in range(5):
#     print(next(generator))

# generator = fibonacci()
# for i in range(1):
#     print(next(generator))
