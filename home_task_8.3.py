def type_logger(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            print(f'{arg}: {type(arg)}')
        for key, value in kwargs.items():
            print(f'{key}: {type(value)}')

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


a = calc_cube(5.5, 6 ,7, 99, a=2.4, b=5)
