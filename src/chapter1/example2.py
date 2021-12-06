'''
Ejemplo de utilización de los operadores con una clase Vector.
'''

import logging

from math import hypot

logging.basicConfig(level=logging.DEBUG)


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        '''
        Para imprimir el estado de la clase. Equivale a toString.
        La función str() invoca a este método de la clase si la función __str__ no está defino en la clase.
        '''
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __str__(self) -> str:
        '''
        Para imprimir el estado de la clase. Equivale a toString.
        Si está esta función definida no se invoca a __repr__.
        '''
        return 'Vector2(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        '''
        Valor absoluto. Aquí se calcula la hipotenusa. 
        
        El método __abs__ se invoca con la función abs()
        '''
        return hypot(self.x, self.y)

    def __bool__(self):
        '''
        Función que se invoca con la función bool().
        
        Si __bool__ no está definido, se invoca a __len__
        '''
        return bool(abs(self))

    def __add__(self, other):
        '''
        Operación de suma. El operador + invoca esta función.

        Si esta función no está definida, el operador + no funciona y saltaría 
        una excepción del tipo : unsupported operand type(s) for +: 'Vector' and 'Vector'

        '''
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        '''
        Operación de multiplicación.
        '''
        return Vector(self.x * scalar, self.y * scalar)


def __ejemplo1() -> None:

    v1 = Vector(2, 2)
    logging.info(f'{v1}')
    logging.info(f'str={str(v1)}')

    v2 = Vector(3, 3)
    logging.info(f'v1 + v2={v1 + v2}')

    logging.info(f'v1 * 3={v1.__mul__(3)}')

    logging.info(f'abs(v1)={abs(v1)}')

    logging.info(f'bool(v1)={bool(v1)}')


def run():
    __ejemplo1()


if __name__ == '__main__':
    try:
        run()
    except Exception as ex:
        logging.error(f'[ERROR] Example1. Exception=[{ex}]')
