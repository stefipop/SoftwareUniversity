from typing import Iterable, Generator

def get_primes(args: Iterable[int]) -> Generator[int, None, None]:
    for num in args:
        if num < 2:
            continue  # Skip numbers less than 2, as they are not prime
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
# print(list(get_primes([-2, 0, 0, 1, 1, 0])))