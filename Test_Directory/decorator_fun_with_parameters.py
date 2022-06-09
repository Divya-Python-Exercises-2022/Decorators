def simple_decorator(func):

    def wrapper(*args, **kwargs):
        name = args[0]
        name = name.upper()

        if 'city' in kwargs.keys():
            city = kwargs['city']
            city = city.upper()
            greeting_str = func(name, city=city)
        else:
            greeting_str = greeting(name)
        return greeting_str

    return wrapper


@simple_decorator
def greeting(name, city='Berlin'):
    return f'Hi {name} {city}'


if __name__ == '__main__':
    print(greeting('divya', 'Hamburg', city='Hamburg', address='Asd 123'))
