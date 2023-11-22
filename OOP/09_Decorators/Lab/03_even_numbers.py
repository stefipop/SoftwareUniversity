from typing import List, Callable


def even_numbers(func: Callable) -> Callable[[list[int]], list[int]]:
    def wrapper(nums: List[int]) -> List[int]:
        even_nums = [num for num in nums if num % 2 == 0]
        return even_nums
    
    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))
