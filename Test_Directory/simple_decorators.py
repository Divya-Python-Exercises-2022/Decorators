def simple_decorator(function):
    def wrapper():
        greeting_string = function()
        greeting_string = f'{greeting_string}, Welcome'
        return greeting_string
    return wrapper


@simple_decorator
def greeting():
    return 'Hi'


@simple_decorator
def greeting2():
    return 'Hi Divya'


if __name__ == '__main__':
    value = greeting()
    print(value)
    print(greeting2())
