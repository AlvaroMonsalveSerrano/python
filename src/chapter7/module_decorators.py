
import time

registry = []


def register_decorator(func):
    '''
    Función 2 decoradora de ejemplo.
    '''
    print(f'Entramos en register_decorator')

    def inner():
        print('running register(%s)' % func)
        registry.append(func)
        result = func()
        return result

    return inner


promos = []


def promotion(promo_func):
    print(f'Running promotion...')
    promos.append(promo_func)
    print(f'promos={promo_func}')
    return promo_func


def clock(func):
    '''
    Definición de una función decoradora.
    '''
    def clocked(*args):
        start = time.perf_counter()
        result = func(*args)
        end = time.perf_counter() - start
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (end, name, arg_str, result))
        return result

    return clocked
