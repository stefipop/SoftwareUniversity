from typing import List


def number_increment(numbers: List[int]) -> List[int]:
    def increase() -> List[int]:
        return [num + 1 for num in numbers]
    
    return increase()


print(number_increment([1, 2, 3]))
