"""
Módulo 1 con ejemplos corutinas
"""
import re
import reprlib
import logging
import itertools
import operator
import random
import sys
import contextlib
from coroutine_util import coroutine

from inspect import getgeneratorstate


def simple_coroutine():
    """
    Definición de un corrutina básica.
    """
    print(f'-> [Start] coroutine.')
    x = yield
    print(f'Received [{x}]')
    print(f'-> [End] coroutine.')


def __example1() -> None:
    my_coroutine = simple_coroutine()

    print(f'-*- Ejemplo 1 de corrutina básica -*-')
    print(f'my_coroutine->{my_coroutine}')
    next(my_coroutine)

    my_coroutine.send(44)


def simple_coroutine2(a):
    """
    Definición de un corrutina básica.
    """
    print(f'-> [Start] coroutine. a={a}')

    b = yield a
    print(f'Received [b={b}]')

    # OJO solo recibe el parámetro enviado desde el llamador. No realiza la suma
    c = yield (a + b)
    print(f'Received [c={c + b + a}]')

    print(f'-> [End] coroutine.')


def __example2() -> None:
    """
    Definición de un corrutina básica en la que se definen variables internas para la realización de cálculos como es 
    el cálculo de una media de unos valores enviados.
    """

    my_coroutine = simple_coroutine2(10)

    print(f'-*- Ejemplo 2 de corrutina básica -*-')
    print(f'my_coroutine->{getgeneratorstate(my_coroutine)}')

    next(my_coroutine)
    print(f'my_coroutine->{getgeneratorstate(my_coroutine)}')

    my_coroutine.send(44)
    print(f'my_coroutine->{getgeneratorstate(my_coroutine)}')

    my_coroutine.send(6)
    print(f'my_coroutine->{getgeneratorstate(my_coroutine)}')


def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count


def __example3() -> None:
    coroutine_average = averager()

    print(f'-*- Ejemplo 3 de corrutina  -*-')
    print(f'my_coroutine->{getgeneratorstate(coroutine_average)}')

    next(coroutine_average)
    r1 = coroutine_average.send(10)
    print(f'r1->{r1}')

    r2 = coroutine_average.send(30)
    print(f'r2->{r2}')

    r3 = coroutine_average.send(5)
    print(f'r3->{r3}')


@coroutine
def averager2():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count


def __example4() -> None:
    coroutine_average = averager2()

    print(f'-*- Ejemplo 4 de corrutina con una clase decoradora.  -*-')
    print(f'my_coroutine->{getgeneratorstate(coroutine_average)}')

    r1 = coroutine_average.send(10)
    print(f'r1->{r1}')

    r2 = coroutine_average.send(30)
    print(f'r2->{r2}')

    r3 = coroutine_average.send(5)
    print(f'r3->{r3}')


def run() -> None:
    try:
        __example1()
    except StopIteration as siex:
        print(siex)

    try:
        __example2()
    except StopIteration as siex:
        print(siex)

    try:
        __example3()
    except StopIteration as siex:
        print(siex)

    try:
        __example4()
    except StopIteration as siex:
        print(siex)


if __name__ == '__main__':
    try:
        run()
    except Exception as ex:
        logging.error(f'[ERROR] Example1. Exception=[{ex}]')
