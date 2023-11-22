from typing import Callable


def multiply(times: int) -> Callable[[Callable], Callable]:
    def decorator(function: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> int:
            result = function(*args, **kwargs)
            return result * times
        
        return wrapper
    
    return decorator

# @multiply(3)
# def add_ten(number):
#     return number + 10
# print(add_ten(3))

# @multiply(5)
# def add_ten(number):
#     return number + 10
# print(add_ten(6))
