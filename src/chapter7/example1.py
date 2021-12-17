'''
Ejemplos del capítulo 7 del libro "Fluent Python"
Título: "Function Decorators y Clousers"
'''
import logging
from typing import Any


def deco(func):
    '''
    Función decoradora de ejemplo.
    '''
    def inner():
        print('running inner()...')
    return inner


@deco
def my_target() -> int:
    print(f'running target()')
    return 5


registry = []


def register(func):
    '''
    Función 2 decoradora de ejemplo.
    Esta función no funciona como decorator. Hay que definir una función interna
    para que funcione.
    '''
    print('running register(%s)' % func)
    registry.append(func)
    func()
    return func


@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')


def f3():
    print('running f3()')


def __example1() -> None:
    print(f'\n-*- Ejemplo Decorator 1 -*-')
    print(f'Referencia target={my_target}')
    # Ejecuta la función decoradora pero no entra en la función.
    result = my_target()
    print(result)


def __example2() -> None:
    print(f'\n-*- Ejemplo Decorator 2 -*-')
    print(f'Registry -> {registry}')
    f1()
    f2()
    f3()


def run() -> None:
    __example1()
    __example2()


if __name__ == '__main__':
    try:
        run()
    except Exception as ex:
        logging.error(f'[ERROR] Example1. Exception=[{ex}]')
