"""
Módulo con ejemplos de generación de funciones usando la librería estándar itertools.
"""
import re
import reprlib
import logging
import itertools
import operator
import random


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


def __example2() -> None:
    """
    Ejemplos de generadores de funciones con itertools.

    La salida por consola de los ejemplos es la siguiente:

        -*- Ejemplos de filtrado con itertools -*-
        l1=['A', 'a', 'a']
        l2=['r', 'd', 'v', 'r', 'k']
        l3=['r', 'd', 'v', 'a', 'r', 'k']
        l4=['A', 'a']
        l5=['A', 'r', 'd', 'a']
        l6=['A', 'a', 'r', 'd']
        l7=['v', 'a', 'r']
        l8=['a', 'd', 'a']
        -*- Ejemplos de generadores de funciones con itertools -*-
        l1=[5, 9, 11, 19, 26, 32, 35, 35, 44, 45]
        l2=[5, 4, 2, 2, 2, 2, 2, 0, 0, 0]
        l3=[5, 5, 5, 8, 8, 8, 8, 8, 9, 9]
        l4=[5, 20, 40, 320, 2240, 13440, 40320, 0, 0, 0]
        l5=[1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]

        -*- Mapping -*-
        l6=[(1, 'a'), (2, 'l'), (3, 'b'), (4, 'a'), (5, 't'), (6, 'r'), (7, 'o'), (8, 'z')]
        l7=[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        l8=[0, 4, 16]
        l9=[(0, 2), (1, 4), (2, 8)]
        l10=['a', 'll', 'bbb', 'aaaa', 'ttttt', 'rrrrrr', 'ooooooo', 'zzzzzzzz']
        l11=[5.0, 4.5, 3.6666666666666665, 4.75, 5.2, 5.333333333333333, 5.0, 4.375, 4.888888888888889, 4.5]

        -*- Merging -*-
        l12=['A', 'B', 'C', 0, 1]
        l13=[(0, 'A'), (1, 'B'), (2, 'C')]
        l14=[0, 'A', 1, 'B', 2, 'C']
        l15=[('A', 0), ('B', 1), ('C', 2)]
        l16=[('A', 0), ('B', 1), ('C', 2), (None, 3), (None, 4)]
        l17=[('A', 0), ('B', 1), ('C', 2), ('?', 3), ('?', 4)]

        -*- Producto cartesiano -*-
        l18=[('A', 0), ('A', 1), ('B', 0), ('B', 1), ('C', 0), ('C', 1)]
        l19=[('A', 'spades'), ('A', 'hearts'), ('A', 'diamonds'), ('A', 'clubs'), ('K', 'spades'), ('K', 'hearts'), ('K', 'diamonds'), ('K', 'clubs')]
        l20=[('A',), ('B',), ('C',)]
        l21=[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
        l22=[(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]

        -*- Count, Cycle y repeat -*-
        1 next=0
        2 next=(1, 2, 3)
        l23=[1, 1.3, 1.6]
        l24=['A', 'B', 'C', 'A', 'B', 'C', 'A']
        3 next=(7, 7, 7)
        l25=[8, 8, 8, 8]
        l26=[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

        -*- Combinaciones y permutaciones -*-
        l27=[('A', 'B'), ('A', 'C'), ('B', 'C')]
        l28=[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
        l29=[('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
        l30=[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]

        -*- GroupBy -*-
        l31=[('L', <itertools._grouper object at 0x10bda92e0>), ('A', <itertools._grouper object at 0x10bda9370>), ('G', <itertools._grouper object at 0x10bda9b50>)]
        char=L -> ['L', 'L', 'L', 'L'] 
        char=A -> ['A', 'A'] 
        char=G -> ['G', 'G', 'G'] 
        length=4 -> ['duck'] 
        length=5 -> ['eagle'] 
        length=3 -> ['rat'] 
        length=7 -> ['giraffe'] 
        length=4 -> ['bear'] 
        length=3 -> ['bat'] 
        length=7 -> ['dolphin'] 
        length=5 -> ['shark'] 
        length=4 -> ['lion'] 

        -*- All, any,... -*-
        l32=True
        l33=False
        l34=True
        l35=True
        l35=True
        l36=False    
    """

    print(f'-*- Ejemplos de generadores de funciones con itertools -*-')
    sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]
    l1 = list(itertools.accumulate(sample))  # Suma acumulada.
    print(f'l1={l1}')
    l2 = list(itertools.accumulate(sample, min))  # mínimo.
    print(f'l2={l2}')
    l3 = list(itertools.accumulate(sample, max))  # máximo.
    print(f'l3={l3}')
    # multiplicación acumulada.
    l4 = list(itertools.accumulate(sample, operator.mul))
    print(f'l4={l4}')
    l5 = list(itertools.accumulate(range(1, 11), operator.mul))
    print(f'l5={l5}')
    print()
    print(f'-*- Mapping -*-')
    l6 = list(enumerate('albatroz', 1))  # lista de tuplas (index, elem)
    print(f'l6={l6}')
    l7 = list(map(operator.mul, range(11), range(11)))
    print(f'l7={l7}')
    l8 = list(map(operator.mul, range(11), [2, 4, 8]))
    print(f'l8={l8}')
    l9 = list(map(lambda a, b: (a, b), range(11), [2, 4, 8]))
    print(f'l9={l9}')
    l10 = list(itertools.starmap(operator.mul, enumerate('albatroz', 1)))
    print(f'l10={l10}')
    l11 = list(itertools.starmap(lambda a, b: b/a,
               enumerate(itertools.accumulate(sample), 1)))
    print(f'l11={l11}')
    print()

    print(f'-*- Merging -*-')
    l12 = list(itertools.chain('ABC', range(2)))
    print(f'l12={l12}')
    l13 = list(itertools.chain(enumerate('ABC')))
    print(f'l13={l13}')
    l14 = list(itertools.chain.from_iterable(enumerate('ABC')))
    print(f'l14={l14}')
    # igual a ist(itertools.chain(enumerate('ABC')))
    l15 = list(zip('ABC', range(5)))
    print(f'l15={l15}')
    l16 = list(itertools.zip_longest('ABC', range(5)))
    print(f'l16={l16}')
    l17 = list(itertools.zip_longest('ABC', range(5), fillvalue='?'))
    print(f'l17={l17}')
    print()

    print(f'-*- Producto cartesiano -*-')
    l18 = list(itertools.product('ABC', range(2)))
    print(f'l18={l18}')
    suites = 'spades hearts diamonds clubs'.split()
    l19 = list(itertools.product('AK', suites))
    print(f'l19={l19}')
    l20 = list(itertools.product('ABC'))
    print(f'l20={l20}')
    l21 = list(itertools.product('ABC', repeat=2))  # tuplas de 2
    print(f'l21={l21}')
    l22 = list(itertools.product(range(2), repeat=3))  # tuplas de 3
    print(f'l22={l22}')
    print()

    print(f'-*- Count, Cycle y repeat -*-')
    ct = itertools.count()
    print(f'1 next={next(ct)}')
    print(f'2 next={next(ct), next(ct), next(ct)}')
    l23 = list(itertools.islice(itertools.count(1, .3), 3))
    print(f'l23={l23}')
    cy = itertools.cycle('ABC')
    l24 = list(itertools.islice(cy, 7))
    print(f'l24={l24}')
    rp = itertools.repeat(7)
    print(f'3 next={next(rp), next(rp), next(rp)}')
    l25 = list(itertools.repeat(8, 4))
    print(f'l25={l25}')
    l26 = list(map(operator.mul, range(11), itertools.repeat(5)))
    print(f'l26={l26}')
    print()

    print(f'-*- Combinaciones y permutaciones -*-')
    l27 = list(itertools.combinations('ABC', 2))
    print(f'l27={l27}')
    l28 = list(itertools.combinations_with_replacement('ABC', 2))
    print(f'l28={l28}')
    l29 = list(itertools.permutations('ABC', 2))
    print(f'l29={l29}')
    l30 = list(itertools.product('ABC', repeat=2))
    print(f'l30={l30}')
    print()

    print(f'-*- GroupBy -*-')
    l31 = list(itertools.groupby('LLLLAAGGG'))
    print(f'l31={l31}')
    for char, group in itertools.groupby('LLLLAAGGG'):
        print(f'char={char} -> {list(group)} ')
    animals = ['duck', 'eagle', 'rat', 'giraffe', 'bear',
               'bat', 'dolphin', 'shark', 'lion']
    for length, group in itertools.groupby(animals, len):
        print(f'length={length} -> {list(group)} ')
    print()

    print(f'-*- All, any,... -*-')
    l32 = all([1, 2, 3])
    print(f'l32={l32}')
    l33 = all([1, 0, 3])
    print(f'l33={l33}')
    l34 = any([1, 2, 3])
    print(f'l34={l34}')
    l35 = any([1, 0, 3])
    print(f'l35={l35}')
    l35 = any([0, 0.4])
    print(f'l35={l35}')
    l36 = any([])
    print(f'l36={l36}')
    print()


def __example3() -> None:
    """
    Ejemplo de una función como iterador.
    """

    def d6():
        return random.randint(1, 6)

    d6_iter = iter(d6, 1)

    print(f'-*- Ejemplo de función como iterador -*-')
    print(f'iter_d6={d6_iter}')
    for i in d6_iter:
        print(f'i={i}')
    print()


def run() -> None:
    __example1()
    __example2()
    __example3()


if __name__ == '__main__':
    try:
        run()
    except Exception as ex:
        logging.error(f'[ERROR] Example1. Exception=[{ex}]')
