"""
Módulo con ejemplos corutinas
"""
import re
import reprlib
import logging
import itertools
import operator
import random
import sys
import contextlib

from inspect import getgeneratorstate


def simple_coroutine():
    """
    Definición de un corutina básica.
    """
    print(f'-> [Start] coroutine.')
    x = yield
    print(f'Received [{x}]')
    print(f'-> [End] coroutine.')


def __example1() -> None:
    my_coroutine = simple_coroutine()

    print(f'-*- Ejemplo 1 de corutina básica -*-')
    print(f'my_coroutine->{my_coroutine}')
    next(my_coroutine)

    my_coroutine.send(44)


def simple_coroutine2(a):
    """
    Definición de un corutina básica.
    """
    print(f'-> [Start] coroutine. a={a}')

    b = yield a
    print(f'Received [b={b}]')

    # OJO solo recibe el parámetro enviado desde el llamador. No realiza la suma
    c = yield (a + b)
    print(f'Received [c={c + b + a}]')

    print(f'-> [End] coroutine.')


def __example2() -> None:
    my_coroutine = simple_coroutine2(10)

    print(f'-*- Ejemplo 2 de corutina básica -*-')
    print(f'my_coroutine->{getgeneratorstate(my_coroutine)}')

    next(my_coroutine)
    print(f'my_coroutine->{getgeneratorstate(my_coroutine)}')

    my_coroutine.send(44)
    print(f'my_coroutine->{getgeneratorstate(my_coroutine)}')

    my_coroutine.send(6)
    print(f'my_coroutine->{getgeneratorstate(my_coroutine)}')


def run() -> None:
    try:
        __example1()
    except StopIteration as siex:
        print(siex)

    try:
        __example2()
    except StopIteration as siex:
        print(siex)


if __name__ == '__main__':
    try:
        run()
    except Exception as ex:
        logging.error(f'[ERROR] Example2. Exception=[{ex}]')
