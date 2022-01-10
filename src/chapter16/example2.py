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

from collections import namedtuple


class DemoException(Exception):
    """
    Excepción de ejemplo.
    """


def demo_exec_handling() -> None:
    """
    Definición de una corrutina con el tratamiento de una excepción.
    """
    print(f'[Start] coroutine.')
    while True:
        try:
            x = yield
            if x == 30:
                raise DemoException("Recibido 30!")
        except DemoException as ex:
            print(f'Exception DemoException, ex=[{ex}]')
        else:
            print(f'Corrutina recibe x=[{x}]')


def __example1() -> None:
    print(f'-*- Ejemplo 1 de corrutina básica -*-')
    my_coroutine = demo_exec_handling()
    next(my_coroutine)
    print(f'my_coroutine->{getgeneratorstate(my_coroutine)}')

    r1 = my_coroutine.send(10)
    print(f'r1->{r1}')

    r2 = my_coroutine.send(30)
    print(f'r2->{r2}')

    r3 = my_coroutine.send(5)
    print(f'r3->{r3}')

    print(f'my_coroutine->{getgeneratorstate(my_coroutine)}')


def demo_exec_handling2() -> None:
    """
    Definición de una corrutina con el tratamiento de una excepción.
    """
    print(f'[Start] coroutine.')
    while True:
        try:
            x = yield
        except DemoException as ex:
            print(f'Exception DemoException, ex=[{ex}]')
        else:
            print(f'Corrutina recibe x=[{x}]')


def __example2() -> None:
    print(f'-*- Ejemplo 2 de corrutina básica lanzando una excepción definida y tratada en la corrutina. -*-')
    my_coroutine = demo_exec_handling2()
    next(my_coroutine)
    print(f'my_coroutine->{getgeneratorstate(my_coroutine)}')

    r1 = my_coroutine.send(10)
    print(f'r1->{r1}')

    r2 = my_coroutine.throw(DemoException("Excepción enviado a la rutina!"))
    print(f'r2->{r2}')

    r3 = my_coroutine.send(5)
    print(f'r3->{r3}')

    print(f'my_coroutine->{getgeneratorstate(my_coroutine)}')


def __example3() -> None:
    print(f'-*- Ejemplo 3 de corrutina básica lanzando una excepción NO definida y tratada en la corrutina. -*-')
    my_coroutine = demo_exec_handling2()
    next(my_coroutine)
    print(f'my_coroutine->{getgeneratorstate(my_coroutine)}')

    r1 = my_coroutine.send(10)
    print(f'r1->{r1}')

    # Al ser una excepción no manejada en la corrutina, se cierra la corrutina.
    r2 = my_coroutine.throw(ZeroDivisionError(
        "Excepción enviado a la rutina!"))
    print(f'r2->{r2}')

    print(f'my_coroutine->{getgeneratorstate(my_coroutine)}')


Result = namedtuple('Result', 'count average')


def averager():
    """
    Definición de una corrutina que realiza el cálculo de una media de los valores
    enviados. 

    El resultado se retorna con la excepción StopIteration. Retorna el resultado en 
    un objeto de tipo Result.

    Returns:
        Result: DTO con el resultado de la corrutina.
    """
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total/count

    return Result(count, average)


def __example4() -> None:
    print(f'-*- Ejemplo 4 de corrutina básica retornando un objeto con el resultado. -*-')
    my_coroutine = averager()
    next(my_coroutine)
    print(f'my_coroutine->{getgeneratorstate(my_coroutine)}')

    r1 = my_coroutine.send(10)
    print(f'r1->{r1}')

    r2 = my_coroutine.send(30)
    print(f'r2->{r2}')

    r3 = my_coroutine.send(5)
    print(f'r3->{r3}')

    try:
        r4 = my_coroutine.send(None)
    except StopIteration as si:
        r4 = si.value
    print(f'r4->{r4}')

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

    try:
        __example3()
    except Exception as siex:
        print(siex)

    try:
        __example4()
    except Exception as siex:
        print(siex)


if __name__ == '__main__':
    try:
        run()
    except Exception as ex:
        logging.error(f'[ERROR] Example1. Exception=[{ex}]')
