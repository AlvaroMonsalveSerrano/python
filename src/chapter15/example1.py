"""
Módulo con ejemplos del capítulo 15 'Context Managers and else blocks'
"""
import re
import reprlib
import logging
import itertools
import operator
import random


def __example1() -> None:

    def f() -> None:
        """
        Ejemplo de bucle for con else: búsqueda de un elemento en una lista.

        Raises:
            ValueError: Si no se encuentra un valor
        """
        my_list = ['a', 'b', 'c', 'd', 'e', 'f']
        for item in my_list:
            if item == 'g':
                break
        else:
            # Se ejecuta si no se rompe con break el bucle
            raise ValueError('No se ha encontrado el valor')

    try:
        print(f'-*- Ejemplo de for con else -*-')
        f()
    except ValueError as ve:
        print(f'Error. Exception={ve}')


def __example2() -> None:

    def f() -> None:
        """
        Ejemplo de bucle for con else: búsqueda de un elemento en una lista.

        Raises:
            ValueError: Si no se encuentra un valor
        """
        my_list = ['a', 'b', 'c', 'd', 'e', 'f']
        index = 0
        while (index < len(my_list)):
            if my_list[index] == 'g':
                # Mejor utilizar una variable de corte (encontrado = True)
                break
            index += 1
        else:
            # Se ejecuta si no se rompe con break el bucle
            raise ValueError('No se ha encontrado el valor')

    try:
        print(f'-*- Ejemplo de while con else -*-')
        f()
    except ValueError as ve:
        print(f'Error. Exception={ve}')


def __example3() -> None:

    def f() -> None:
        """
        Ejemplo de bucle for con else: búsqueda de un elemento en una lista.

        Raises:
            ValueError: Si no se encuentra un valor
        """
        my_list = ['a', 'b', 'c', 'd', 'e', 'f']
        for item in my_list:
            if item == 'b':
                break
        else:
            # Se ejecuta si no se rompe con break el bucle
            raise ValueError('No se ha encontrado el valor')

    try:
        print(f'-*- Ejemplo de try con else -*-')
        f()
    except ValueError as ve:
        print(f'Error. Exception={ve}')
    else:
        print(f'Siguiente tarea si no hay excepción...')


def run() -> None:
    __example1()
    __example2()
    __example3()


if __name__ == '__main__':
    try:
        run()
    except Exception as ex:
        logging.error(f'[ERROR] Example1. Exception=[{ex}]')
