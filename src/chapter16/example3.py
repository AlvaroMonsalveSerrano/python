"""
Módulo 3 con ejemplos corutinas.

Ejemplos de yield from.
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

from collections import namedtuple


Result = namedtuple('Result', 'count average')


def averager():
    """
    Definición de una corrutina que realiza el cálculo de una media de los valores
    enviados. 

    El resultado se retorna con la excepción StopIteration. Retorna el resultado en 
    un objeto de tipo Result.

    Corrutina con función de subgenerador.

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


def grouper(results: dict, key):
    """
    La función grouper realiza una labor de generador delegado.

    Args:
        results (dict): Resultado de las corrutinas.
        key (¿?): Valor identificativo en los resultados.

    Yields:
        averager: Corrutina que realiza el cálculo de una media.
    """
    while True:
        results[key] = yield from averager()


def report(results: dict) -> None:
    """
    Función con la visualización de resultados pasados por parámetro.

    Args:
        results (dict): Diccionario de datos con los resultados.
    """
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print('{:2} {:5} averaging {:.2f}{}'.format(
            result.count, group, result.average, unit))
    pass


def main_coroutine(data):
    """
    Función cliente para el tratamiento de los generadores de corrutinas delegados.

    OJO! Recorre de forma secuencial los grupos y datos de cada grupo para su procesamiento 
    secuencial mediante la utlización de corrutinas.

    Args:
        data (dict): Datos que se utilizan en el envío a la corrutinas.
    """
    results = {}
    for key, values in data.items():
        group = grouper(results, key)
        next(group)
        for value in values:
            group.send(value)
        group.send(None)
    report(results)


def __example1() -> None:
    print(f'-*- Ejemplo 1 de corrutina básica yield from. -*-')

    data = {
        'girls;kg': [40.9, 38.5, 44.3, 42.2, 54.2],
        'girls;m': [1.6, 1.51, 1.4, 1.3, 1.41],
        'boys;kg': [39.0, 40.8, 43.2, 40.8, 43.1, 59.2],
        'boys;m': [1.38, 1.5, 1.32, 1.37, 1.25, 1.55],
    }

    main_coroutine(data)


def run() -> None:
    try:
        __example1()
    except StopIteration as siex:
        print(siex)


if __name__ == '__main__':
    try:
        run()
    except Exception as ex:
        logging.error(f'[ERROR] Example3. Exception=[{ex}]')
