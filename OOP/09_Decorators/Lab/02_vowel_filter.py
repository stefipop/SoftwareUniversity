from typing import List, Callable


def vowel_filter(func: callable) -> Callable[[], list[str]]:
    def wrapper() -> List[str]:
        result = func()
        vowels = [char for char in result if char.lower() in "aeouiy"]
        return vowels
    
    return wrapper


@vowel_filter
def get_letters() -> List[str]:
    return ["a", "b", "c", "d", "e"]


print(get_letters())
