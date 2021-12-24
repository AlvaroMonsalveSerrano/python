

import logging
import functools
import array
import operator
import math
import numbers
import reprlib
import random


class MyVector:
    typecode = 'd'

    def __init__(self, components) -> None:
        # self._components protected
        self._components = array.array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self) -> str:
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'MyVector({})'.format(components)

    def __str__(self) -> str:
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(self._components))

    def __eq__(self, __o: object) -> bool:
        return (
            len(self) == len(__o) and
            all(a == b for a, b in zip(self.__o))
        )

    def __hash__(self) -> int:
        hashes = (hash(x) for x in self)
        return functools.reduce(operator.xor, hashes, 0)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = '{.__name__} indices must be integers'
            raise TypeError(msg.format(cls))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)


def __example1():
    """
    Ejemplo de definición de una clase.

    """
    print(f'-*- Objectos -*-')
    vector1 = MyVector((random.random() for i in range(3)))

    print(f'vector1={vector1}')
    print(f'vector1={str(vector1)}')
    for elem in vector1:
        print(f'->{elem}')

    print(f'vector1[1]={vector1[1]}')
    print(f'vector1.__bytes__={vector1.__bytes__}')
    print(f'len(vector1)={len(vector1)}')


def run() -> None:
    __example1()


if __name__ == '__main__':
    try:
        run()
    except Exception as ex:
        logging.error(f'[ERROR] example1. Exception=[{ex}]')
