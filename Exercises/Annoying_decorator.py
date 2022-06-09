def annoying_decorator(func):
    def wrapper():
        value = func()
        if value == 'Hi':
            greeting_text = f"Don't use Hi! with me, please!"
            return greeting_text
        else:
            greeting_text = f'Hello, Sir.'
            return greeting_text

    return wrapper


@annoying_decorator
def greetings():
    return "Hi"

    #return 'Hello'


if __name__ == '__main__':
    print(greetings())
