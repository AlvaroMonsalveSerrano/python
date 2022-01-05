"""
Módulos con ejemplos de gestores de contexto.
Los gestores de contexto se utilizan en el patrón Unit Of Work.
"""
import re
import reprlib
import logging
import itertools
import operator
import random
import sys
import contextlib


class LookingGlass:
    """
    La clase LookingGlass define las funciones para que sea utilizado en un contexto.
    """

    def __enter__(self):
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'JABBERWOCKY'

    def reverse_write(self, text):
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print(f'Please do not divide by zero!')
            return True


def __example1() -> None:
    """
    Ejemplo en donde se usa la clase LookinGlass para utilizarlo en un contexto.
    """
    print(f'-*- Ejemplo de contexto en una clase -*-')
    with LookingGlass() as what:
        print(f'Alice, kitty and Snowdrop')
        print(what)
    print()


@contextlib.contextmanager
def lookin_glass():
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write

    msg = ''
    try:
        # Hasta aquí corresponde con __enter__(), después, corresponde con __exit__
        yield 'JABBERWOCKY'
    except ZeroDivisionError:
        msg = 'Please do not divide by zero!'
    finally:
        sys.stdout.write = original_write
        if msg:
            print(msg)


def __example2() -> None:
    """
    Ejemplo de uso de un gestor de contexto en una función usando la anotación @contextlib.contextmanager
    """

    print(f'-*- Ejemplo de contexto en una función -*-')
    with lookin_glass() as what:
        print(f'Alice, kitty and Snowdrop')
        print(what)
    print()


def run() -> None:
    __example1()
    __example2()


if __name__ == '__main__':
    try:
        run()
    except Exception as ex:
        logging.error(f'[ERROR] Example2. Exception=[{ex}]')
