
import logging
import time
import functools
import copy
import array


class BeanObject:

    typecode = 'd'

    def __init__(self, x, y) -> None:
        """Constructor de la clase BeanObject.

           Los atributos con dos '_' son privados; por ejemplo: self.__x
           Los atributos con un '_' son protegidos; por ejemplo: self._p.

        Args:
            x ([type]): [description]
            y ([type]): [description]
        """
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        """Hay que definir este método para que sea un objeto iterable.
           Si no se define, no funciona __repr__

        Returns:
            [type]: [description]
        """
        return (i for i in (self.x, self.y))

    def __repr__(self) -> str:
        """Visualiación de cómo el desarrollador quiere mostrar los datos.

        Returns:
            str: [description]
        """
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self) -> str:
        """Visualización de cómo el usuario quiere ver los datos

        Returns:
            str: [description]
        """
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array.array(self.typecode, self)))

    def __hash__(self) -> int:
        return hash(self.x) ^ hash(self.y)


def __example1():
    print(f'-*- Objectos -*-')
    bean1 = BeanObject(1.0, 2.0)
    print(f'bean1.x={bean1.x}')
    print(f'bean1.y={bean1.y}')
    print(f'bean1={bean1}')
    print(f'repr(bean1)={repr(bean1)}')
    print(f'bean1.__bytes__={bean1.__bytes__}')


def run() -> None:
    __example1()


if __name__ == '__main__':
    try:
        run()
    except Exception as ex:
        logging.error(f'[ERROR] example1. Exception=[{ex}]')
