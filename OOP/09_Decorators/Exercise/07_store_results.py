class store_results:
    def __init__(self, func_name):
        self.func_name = func_name
    
    def __call__(self, *args, **kwargs):
        with open("results.txt", "a") as file:
            result = self.func_name(*args, **kwargs)
            file.write(f"Function '{self.func_name.__name__}' was called. Result: {result}\n")


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)