'''
Ejemplos del capítulo 7 del libro "Fluent Python"
Título: "Function Decorators y Clousers"
'''
import logging
from typing import Any


registry = []


def register(func):
    '''
    Función 2 decoradora de ejemplo.
    '''
    def inner():
        print('running register(%s)' % func)
        registry.append(func)
        result = func()
        return result

    return inner


@register
def f1() -> None:
    print('running f1()')


@register
def f2() -> None:
    print('running f2()')


def f3() -> None:
    print('running f3()')


def run() -> None:
    print(f'\n-*- Ejemplo Decorator 2 -*-')
    print(f'1 Registry -> {registry}')
    f1()
    f2()
    f3()
    print(f'2 Registry -> {registry}')


if __name__ == '__main__':
    try:
        run()
    except Exception as ex:
        logging.error(f'[ERROR] Example1. Exception=[{ex}]')
