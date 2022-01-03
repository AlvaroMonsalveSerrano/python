
import logging
import functools
import array
import operator
import math
import numbers
import reprlib
import random
from random import randrange, shuffle
import collections
import abc


class Tombola(abc.ABC):

    @abc.abstractmethod
    def load(self, iterable):
        """
        """

    @abc.abstractmethod
    def pick(self):
        """[summary]
        """

    def loaded(self):
        """Retorna 'True' si hay al menos un elemento; 'False', en otro caso.

        Returns:
            [type]: [description]
        """
        return bool(self.inspect())

    def inspect(self):
        """Retorna una tupla ordenada con los datos insertados.

        Returns:
            tuple: resultado
        """
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))


class BingoCage(Tombola):
    """Definición de la clase BingoCage la cual hereda de Tombola y es una clase de tipo callable.

    Args:
        Tombola ([type]): [description]
    """

    def __init__(self, items) -> None:
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        """Función que permite definir la clase BingoCage como callable.
        """
        return self.pick()


def __example1():
    bingo1 = BingoCage([1, 2, 3, 4])
    print(f'-*- Example1: definición de una clase BingoCage que hereda de Tombola-*-')
    print(f'bingo1={bingo1.pick()}')
    print(f'bingo1={bingo1.pick()}')
    print(f'bingo1={bingo1()}')
    print()


class LotteryBlower(Tombola):
    """Definición de la clase LotteryBlower la cual hereda de Tombola. 
    Mismas funciones pero con distinta funcionalidad.

    """

    def __init__(self, iterable):
        self._balls = list(iterable)  # Realiza una copia de iterable

    def load(self, iterable):
        self._balls.extend(iterable)

    def pick(self):
        try:
            position = random.randrange(len(self._balls))
        except ValueError:
            raise LookupError('pick from empty BingoCage')
        return self._balls.pop(position)

    def loaded(self):
        return bool(self._balls)

    def inspect(self):
        return tuple(sorted(self._balls))


def __example2():
    print(f'-*- Example2: definición de una clase LotteryBlower que hereda de Tombola-*-')
    bingo1 = LotteryBlower([1, 2, 3, 4])
    print(f'bingo1.pick()={bingo1.pick()}')
    print(f'bingo1.loaded()={bingo1.loaded()}')
    print(f'bingo1.inspect()={bingo1.inspect()}')
    print()

#
# -- Ejemplo de una subclase virtual de Tombola.
#


@Tombola.register
class TomboList(list):
    """Nos e realiza ninguna comprobación de la existencia total a parcial de las funciones 
    que se definen en la clase virtual.

    La idea es definir una clase que hereda de otra y la implementación de las funciones 
    definidas en el 'interface' Tombola. 

    """

    def pick(self):
        if self:
            position = randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError('pop from empty TomboList')

    load = list.extend  # Tombolist.load es igual a list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))


def __example3():
    print(f'-*- Example3: definición de una subclase virtual de Tombola y que hereda de list. -*-')
    list1 = TomboList([1, 2, 3, 4])
    print(f'list1.pick()={list1.pick()}')
    list1.extend([5, 6, 7])
    print(f'list1.loaded()={list1.loaded()}')
    print(f'list1.inspect()={list1.inspect()}')
    print(f'issubclass(TomboList, Tombola)={issubclass(TomboList, Tombola)}')
    print(f'isinstance(list1, Tombola)={isinstance(list1, Tombola)}')
    print(f'isinstance(list1, TomboList)={isinstance(list1, TomboList)}')

    print()


def run() -> None:
    __example1()
    __example2()
    __example3()


if __name__ == '__main__':
    try:
        run()
    except Exception as ex:
        logging.error(f'[ERROR] example1. Exception=[{ex}]')
