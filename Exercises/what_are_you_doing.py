def verbose(func):
    def wrapper(*args):
        a = args[0]
        b = args[1]
        c = func(a, b)
        #d = a, b  # means d = (a, b)
        d = a, b, c
        # return print(f'{func.__name__} invoked with {d} -> {c}')
        return print(f'sum_two invoked with ({a, b}) -> {c}')

    return wrapper


@verbose
def sum_two(a, b):
    return a + b


if __name__ == "__main__":
    sum_two(3, 4)

