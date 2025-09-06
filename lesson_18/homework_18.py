# декоратори

def log_decorator(fn):
    def wrapper (*args, **kwargs):
        print(f"Function :{fn.__name__}")
        print(f"Arguments :{args}, {kwargs}")
        result = fn(*args, **kwargs)
        return result
    return wrapper


def exception_decorator(fn):
    def wrapper(*args, **kwargs):
        def safe_generator():
            try:
                yield from fn(*args, **kwargs)
            except Exception as e:
                print(f"ERROR FOUND: {e}")
        return safe_generator()
    return wrapper

# генератори
@log_decorator
def even_number(n):
    for i in range (0, n + 1):
        if i % 2 ==0:
            yield i

@exception_decorator
def fibonacci(n):
    if not isinstance(n, (int, float)):
        raise TypeError("N повинно бути числом")
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b



# ітератори
class ReversIterator:
    def __init__(self, smth):
        self.list = smth
        self.index =len(smth)


    def __iter__(self):
        return self


    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.list[self.index]


class EvenIterator:
    def __init__(self, n):
        self.n = n
        self.current_number = 0


    def __iter__(self):
        return self


    def __next__(self):
        if self.current_number > self.n:
            raise StopIteration
        result = self.current_number
        self.current_number += 2
        return result


if __name__ == "__main__":
    print("Тест генератора парних чисел")
    for num in even_number(6):
        print(num)

    print("Тест генератора Фібоначчі - негативний ")
    for num in fibonacci("SMTH"):
        print(num)

    print("Тест генератора Фібоначчі - Позитивний ")
    for num in fibonacci(9):
        print(num)


    print("Тест зворотнього ітератора")
    reverse_iter = ReversIterator([1, 2, 3, 4, 5])
    for item in reverse_iter:
        print(item)

    print("Тест ітератора парних чисел")
    even_iter = EvenIterator(8)
    for num in even_iter:
        print(num)







