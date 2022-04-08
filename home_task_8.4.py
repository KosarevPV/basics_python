def val_checker(check):
    def _logger(func):
        def wrapper(*args):
            for arg in args:
                if not check(arg):
                    msg = f'wrong val {arg}'
                    raise ValueError(msg)
                else:
                    print(func(arg))

        return wrapper

    return _logger


@val_checker(lambda x: x > 0)
def calc_cube1(x):
    return x ** 3


a = calc_cube1(5, 6, 2, 2.5, 0)
