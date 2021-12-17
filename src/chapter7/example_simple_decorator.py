
import logging
import time
import functools

from module_decorators import clock

#
# Si la función se define en este módulo, funciona bien.
#
# def clock(func):
#     '''
#     Definición de una función decoradora.
#     '''
#     def clocked(*args):
#         start = time.perf_counter()
#         result = func(*args)
#         end = time.perf_counter() - start
#         name = func.__name__
#         arg_str = ', '.join(repr(arg) for arg in args)
#         print('[%0.8fs] %s(%s) -> %r' % (end, name, arg_str, result))
#         return result

#     return clocked


@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n-1)


def factorial2(n):
    return 1 if n < 2 else n * factorial(n-1)


def __ejemplo1() -> None:
    print(f'-*- Ejemplo de funciones con decoradores. -*-')
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'Calling factorial(6)')
    print(f'6! = {factorial(6)}')


def __ejemplo2() -> None:
    print(f'-*- Ejemplo de funciones. -*-')
    # Funciones que se ejecutan internamente al invocar una función y el decorador.
    fact = clock(factorial)
    print(f'6! = {fact(6)}')


@clock
def fibonacci(n):
    '''
    En la salida de la función se escriben todas las funciones de llamada sin cachear.
    '''
    if n < 2:
        return n
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


@functools.lru_cache()
@clock
def fibonacci2(n):
    '''
    En la salida de la función se escriben todas las funciones de llamada cacheando las llamadas.
    '''
    if n < 2:
        return n
    else:
        return fibonacci2(n - 2) + fibonacci2(n - 1)


def __ejemplo3() -> None:
    print(f'-*- Ejemplo de funciones con decoradores. -*-')
    print('*' * 40, 'Calling fibonacci(6)')
    print(f'fibonacci(6) = {fibonacci(6)}')
    print('*' * 40, 'Calling fibonacci2(6) Esta opción es la más eficiente porque usa @functools.lru_cache()')
    print(f'fibonacci2(6) = {fibonacci2(6)}')


@functools.singledispatch
def add(a, b):
    raise NotImplementedError('Unsupported type')


@add.register(float)
@add.register(int)
def _(a, b):
    print(f'Tipos de argumentos={type(a)}')
    return a + b


def __ejemplo4() -> None:
    print(f'-*- Ejemplo de singledispatch -*-')
    print(f'add(4, 5)={add(4, 5)}')
    print(f'add(4.3, 5.7)={add(4.3, 5.7)}')

    try:
        # Error porque es un tipo no soportado.
        print(f'add([4], [5])={add( [4], [5])}')
    except Exception as ex:
        print(f'Exception singledispatch()={ex}')


def run() -> None:
    __ejemplo1()
    __ejemplo2()
    __ejemplo3()
    __ejemplo4()


if __name__ == '__main__':
    try:
        run()
    except Exception as ex:
        logging.error(f'[ERROR] example_simple_decorator. Exception=[{ex}]')
