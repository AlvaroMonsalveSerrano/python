"""
Módulo con ejemplos de generación de funciones usando la librería estándar itertools.
"""
import re
import reprlib
import logging
import itertools


def __example1() -> None:
    """
    Ejemplos de funciones de filtrado.
    """
    def vowel(c):
        return c.lower() in 'aeiou'

    print(f'-*- Ejemplos de filtrado con itertools -*-')
    l1 = list(filter(vowel, 'Aardvark'))
    print(f'l1={l1}')
    l2 = list(itertools.filterfalse(vowel, 'Aardvark'))
    print(f'l2={l2}')
    l3 = list(itertools.dropwhile(vowel, 'Aardvark'))
    print(f'l3={l3}')
    l4 = list(itertools.takewhile(vowel, 'Aardvark'))
    print(f'l4={l4}')
    l5 = list(itertools.compress('Aardvark', (1, 0, 1, 1, 0, 1)))
    print(f'l5={l5}')
    l6 = list(itertools.islice('Aardvark', 4))
    print(f'l6={l6}')
    l7 = list(itertools.islice('Aardvark', 4, 7))
    print(f'l7={l7}')
    l8 = list(itertools.islice('Aardvark', 1, 7, 2))
    print(f'l8={l8}')

    pass


def run() -> None:
    __example1()


if __name__ == '__main__':
    try:
        run()
    except Exception as ex:
        logging.error(f'[ERROR] Example1. Exception=[{ex}]')
