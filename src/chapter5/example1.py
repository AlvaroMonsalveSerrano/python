'''
Chapter 5: First-Class Functions
'''
import logging
import sys
import re
import os
import random

from functools import reduce, partial
from operator import add, mul, itemgetter, attrgetter, methodcaller

from collections import abc, namedtuple

logging.basicConfig(level=logging.DEBUG)


class BingoCage:
    '''
    Ejemplo para definir una clase como si fuese un objeto. Para crear un objeteo de la clase como 
    un objeto es necesario definir la función __call__

    Ejemplo en __callable_types()
    '''

    def __init__(self, items) -> None:
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCase')

    def __call__(self):
        return self.pick()


def factorial(n: int) -> int:
    ''' 
        Return n!
        '''
    return 1 if n < 2 else n * factorial(n-1)


def __funcion_como_objeto() -> None:
    print(f'\n-*- Función como objeto -*-')

    print(f'factorial(5)={factorial(5)}')
    print(f'factorial.__doc__={factorial.__doc__}')

    fact = factorial
    print(f'fac(5)={fact(5)}')

    l_r1 = list(map(factorial, range(10)))
    print(f'l_r1={l_r1}')


def __high_order_function() -> None:
    print(f'\n-*- Higher Order Function -*-')
    fact = factorial

    list_factorial1 = list(map(fact, range(10)))
    print(f'list_factorial1={list_factorial1}')

    list_factorial2 = [fact(i) for i in range(10)]
    print(f'list_factorial2={list_factorial2}')

    list_factorial3 = list(map(factorial, filter(lambda n: n % 2, range(10))))
    print(f'list_factorial3={list_factorial3}')

    list_factorial4 = [factorial(n) for n in range(10) if n % 2]
    print(f'list_factorial4={list_factorial4}')

    result_reduce = reduce(add, range(100))
    print(f'result_reduce={result_reduce}')


def __anonymous_functions() -> None:

    print(f'\n-*- Anonymous functions -*-')
    fruits = ['stawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']

    print(f'fruits={fruits}')
    # Ordena del reves las palabras de la lista.
    result1 = sorted(fruits, key=lambda word: word[::-1])
    print(f'result1={result1}')


def __callable_types() -> None:
    print(f'\n-*- Callable types -*-')
    bingo = BingoCage(range(3))
    print(f'bingo.pick()={bingo.pick()}')
    print(f'bingo()={bingo()}')
    print(f'bingo()={bingo()}')
    print(f'callable()?={callable(bingo)}')


def __functions_annotations() -> None:
    print(f'\n-*- Functions Annotations -*-')

    def my_sum(oper_a: int, oper_b: int, plus: 'int > 0' = 10) -> int:
        '''
        Ejemplo de una función en la que se define una anotación en el parámetro plus.
        '''
        return oper_a + oper_b + plus

    print(f'my_sum(4, 5)={my_sum(4, 5)}')
    print(f'my_sum(4, 5)={my_sum(4, 5, 20)}')
    print(f'my_sum.__annotations__={my_sum.__annotations__}')


def __module_operator() -> None:
    print(f'\n-*- Module Operator -*-')

    def fact1(n):
        return reduce(lambda a, b: a*b, range(1, n+1))

    print(f'fact1(5)={fact1(5)}')

    def fact2(n):
        return reduce(mul, range(1, n+1))
    print(f'fact2(5)={fact2(5)}')

    metro_data = [
        ('Tokyo', 'JP', 36.933, (35.4684, 139.68434)),
        ('Mexico City', 'MX', 16.933, (56.4684, 39.68434)),
        ('Sao Paulo', 'BR', 26.93, (33.44252, -131.6454)),
        ('Delhi NCR', 'In', 66.533, (39.47784, -99.68434)),
        ('New York-Newark', 'US', 36.933, (22.2222, 33.3333))
    ]

    print(f'Ordenación de una lista por el campo de la posición 1 de las tuplas de una lista...')
    for city in sorted(metro_data, key=itemgetter(1)):
        print(f'city={city}')

    print(f'Listado de los elementos seleccionados de las tuplas de una lista...')
    cc_name = itemgetter(0, 1)
    for city in metro_data:
        print(f'cc_name(city)={cc_name(city)}')

    # Creación de entidades y su estructura.
    LatLong = namedtuple('LatLong', 'lat long')
    Metropolis = namedtuple('Metropolis', 'name cc pop coord')
    metro_areas = [
        Metropolis(name, cc, pop, LatLong(lat, long)) for name, cc, pop, (lat, long) in metro_data
    ]

    # Acceso a los elementos de la lista creada.
    print(f'-->>{metro_areas[1]}')
    print(f'-->>{metro_areas[1].coord}')
    print(f'-->>{metro_areas[1].coord.lat}')

    # Ordenación de la lista por un atributo de la clase.
    for city in sorted(metro_areas, key=attrgetter('coord.lat')):
        print(f'city={city}')

    # Ejemplo de uso de methodcaller
    s = 'String de prueba'
    upcase = methodcaller('upper')
    print(f'upcase(s) == s.upper()?{upcase(s) == s.upper()}')

    suss = methodcaller('replace', ' ', '-')
    print(f'suss={suss(s)}')

    # Ejemplo de partial
    triple = partial(mul, 3)
    print(f'triple={triple(7)}')
    print(f'list(map(triple, range(1,10)))={list(map(triple, range(1,10)))}')


def run() -> None:
    __funcion_como_objeto()
    __high_order_function()
    __anonymous_functions()
    __callable_types()
    __functions_annotations()
    __module_operator()


if __name__ == '__main__':
    try:
        run()
    except Exception as ex:
        logging.error(f'[ERROR] Example1. Exception=[{ex}]')
