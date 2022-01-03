
import logging
import functools
import array
import operator
import math
import numbers
import reprlib
import random
from random import shuffle
import collections


class MyVector2d():
    """
    Definición de una clase con dos atributos y sus método 'get' asociados a los atributos.
    """
    typecode = 'd'

    def __init__(self, x, y) -> None:
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.__x, self.__y))


def __example1():
    my_vector2d = MyVector2d(3, 4)
    print(f'-*- Ejemplos de función get -*-')
    print(f'my_vector2d.x={my_vector2d.x}')
    print(f'my_vector2d.y={my_vector2d.y}')
    print()


class My2Vector2d(collections.MutableSequence):
    """
    Definición de una clase con dos atributos y sus método 'get' asociados a los atributos.

    La clase My2Vector2d hereda de la clase collections.MutableSequence, hay que definir las funciones abstractas:
        + __len__
        + __getitem__
        + __setitem__
        + __delitem__
        + insert()

    """
    typecode = 'd'

    def __init__(self, x, y) -> None:
        self.__x = float(x)
        self.__y = float(y)
        self._element = []

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.__x, self.__y))

    def __len__(self) -> int:
        return len(self._element)

    def __getitem__(self, position):
        return self._element[position]

    def __setitem__(self, position, value):
        self._element[position] = value

    def __delitem__(self, position):
        del self._element[position]

    def insert(self, index: int, value: typecode) -> None:
        return self._element.insert(index, value)


def __example2():
    print(f'-*- Ejemplos de función shuffle -*-')
    my_vector2d = My2Vector2d(3, 4)
    print(f'-*- Ejemplos de función get -*-')
    print(f'my_vector2d.x={my_vector2d.x}')
    print(f'my_vector2d.y={my_vector2d.y}')
    print(f'my_vector2d.y={my_vector2d.count}')
    print()

    my_vector2d.insert(0, 10)
    my_vector2d.insert(1, 20)
    my_vector2d.insert(2, 30)

    print(f'my_vector2d[2]={my_vector2d[2]}')
    print(f'my_vector2d[1]={my_vector2d[1]}')
    print(f'my_vector2d[0]={my_vector2d[0]}')
    print(f'len(my_vector2d)={len(my_vector2d)}')
    print()

    del my_vector2d[1]

    print(f'my_vector2d[1]={my_vector2d[1]}')
    print(f'my_vector2d[0]={my_vector2d[0]}')
    print(f'len(my_vector2d)={len(my_vector2d)}')
    print()

    # Invocación de una función predefinida de collections.MutableSequence
    my_vector2d.reverse()
    print(f'my_vector2d[1]={my_vector2d[1]}')
    print(f'my_vector2d[0]={my_vector2d[0]}')
    print(f'len(my_vector2d)={len(my_vector2d)}')
    print()


def run() -> None:
    __example1()
    __example2()


if __name__ == '__main__':
    try:
        run()
    except Exception as ex:
        logging.error(f'[ERROR] example1. Exception=[{ex}]')
