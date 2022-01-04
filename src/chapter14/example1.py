
import re
import reprlib
import logging


def __example1() -> None:

    RE_WORLD = re.compile('\w+')

    words = reprlib.repr((3.0, 'texto'))  # 'Texto de prueba'
    print(f'words={words}')

    words2 = RE_WORLD.findall('Texto de prueba')
    print(f'words2={words2}')  # words2=['Texto', 'de', 'prueba']


RE_WORLD = re.compile('\w+')

#
# Forma 1 para definir una clase iterable
#


class Sentence:
    """Definición de la clase Sentence con la funciones para que sea iterable (__getitem__, __len__).
    Esta es la forma sencilla de hacer una clase iterable.

    Sentence es una clase que define una lista con las palabras del string pasado por parámetro.
    """

    def __init__(self, text) -> None:
        self.text = text
        self.words = RE_WORLD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self) -> str:
        return 'Sentence(%s)' % reprlib.repr(self.text)


def __example2() -> None:
    print(f'-*- Ejemplo de clase iterable -*-')
    s = Sentence('"Esto es un texto de prueba," para un ejemplo de Python...')
    print(f'Sentence={s}')
    for word in s:
        print(word)
    print()

    list_s = list(s)
    print(f'list_s={list_s}')
    print()


def __example3() -> None:
    """Un ibjeto es iterador si implementa la función __iter__. La función iter() construye un iterador.
    Un iterador implmenta la función __next__ y __iter__
    """
    print(f'-*- Ejemplo de clase iterador -*-')
    s = Sentence("Ejemplos de clase iterador")
    print(f'Sentence={s}')
    it_s = iter(s)
    print(f'Sentence iterador={it_s}')
    print(f'->{next(it_s)}')
    print(f'->{next(it_s)}')
    print(f'->{next(it_s)}')
    print(f'->{next(it_s)}')
    try:
        print(f'->{next(it_s)}')
    except StopIteration as ex:
        print(f'Fin de iteración. Exception=[{ex}]')
    print()

#
# Forma 2 para definir una clase iterable. Implementaco el patron Iterator (GoF)
#


class Sentence2:
    """Definición de la clase Sentence2 con las funciones de un iterador(__iter__).

    Sentence es una clase que define una lista con las palabras del string pasado por parámetro.
    """

    def __init__(self, text) -> None:
        self.text = text
        self.words = RE_WORLD.findall(text)

    def __repr__(self) -> str:
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return SentenceIterator(self.words)


class SentenceIterator:

    def __init__(self, words) -> None:
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError as ex:
            raise StopIteration()
        self.index += 1
        return word

    def __iter__(self):
        return self


def __example4() -> None:
    print(f'-*- Ejemplo de clase iterador implementado el patrón de GoF -*-')
    s = Sentence2("Ejemplos de clase iterador")
    print(f'Sentence2={s}')
    it_s = iter(s)
    print(f'Sentence2 iterador={it_s}')
    print(f'->{next(it_s)}')
    print(f'->{next(it_s)}')
    print(f'->{next(it_s)}')
    print(f'->{next(it_s)}')
    try:
        print(f'->{next(it_s)}')
    except StopIteration as ex:
        print(f'Fin de iteración. Exception=[{ex}]')
    print()


#
# Forma 3 para definir una clase iterable. Implementado un generador de función.
#

class Sentence3:
    """Definición de la clase Sentence3 con un generador de función.

    Sentence es una clase que define una lista con las palabras del string pasado por parámetro.
    """

    def __init__(self, text) -> None:
        self.text = text
        self.words = RE_WORLD.findall(text)

    def __repr__(self) -> str:
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for word in self.words:
            yield word
        return  # No es necesario.


def __example5() -> None:
    print(f'-*- Ejemplo de clase iterador con generador de función -*-')
    s = Sentence3("Ejemplos de clase iterador")
    print(f'Sentence3={s}')
    it_s = iter(s)
    print(f'Sentence3 iterador={it_s}')
    print(f'->{next(it_s)}')
    print(f'->{next(it_s)}')
    print(f'->{next(it_s)}')
    print(f'->{next(it_s)}')
    try:
        print(f'->{next(it_s)}')
    except StopIteration as ex:
        print(f'Fin de iteración. Exception=[{ex}]')
    print()


class Sentence4:
    """Definición de la clase Sentence4 con implementación perezosa.

    Sentence es una clase que define una lista con las palabras del string pasado por parámetro.
    """

    def __init__(self, text) -> None:
        self.text = text
        # self.words = RE_WORLD.findall(text)

    def __repr__(self) -> str:
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for word in RE_WORLD.finditer(self.text):
            yield word.group()
        # return  # No es necesario.


def __example6() -> None:
    print(f'-*- Ejemplo de clase iterador con implementación perezosa -*-')
    s = Sentence3("Ejemplos de clase iterador")
    print(f'Sentence4={s}')
    it_s = iter(s)
    print(f'Sentence4 iterador={it_s}')
    print(f'->{next(it_s)}')
    print(f'->{next(it_s)}')
    print(f'->{next(it_s)}')
    print(f'->{next(it_s)}')
    try:
        print(f'->{next(it_s)}')
    except StopIteration as ex:
        print(f'Fin de iteración. Exception=[{ex}]')
    print()


def __example7() -> None:
    """Ejemplo con generadores de expresiones.
    Un generador de expresiones se puede comprender como un list comprehension con evaluación perezosa 
    sin retornar una lista.

    Un generador de expresiones es una factoria de generadores.
    """
    print(f'-*- Ejemplo de Generador de expresiones -*-')

    def gen_ABC():
        print('start')
        yield 'A'
        print('continue')
        yield 'B'
        print('end')

    # Ejemplo con un List comprehension. Cuando se crea result1 se consume el generador
    result1 = [x*3 for x in gen_ABC()]
    print(f'Lista=>{result1}')
    for i in result1:
        print(f'-->{i}')

    # Ejemplo con una tupla. No se consume el resultado de la expresión.
    result2 = (x*3 for x in gen_ABC())
    print(f'Tupla=>{result2}')
    for i in result2:
        print(f'-->{i}')

#
# Generador de expresiones aritméticas.
#


class ArithmeticProgression:

    def __init__(self, begin, step, end=None) -> None:
        self.begin = begin
        self.step = step
        self.end = end  # None -> infinite series

    def __iter__(self):
        result = type(self.begin + self.step)(self.begin)
        forever = self.end is None
        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index


def __example8() -> None:
    """Ejemplo de generador de progresiones aritméticas.
    """

    print(f'-*- Ejemplo de Generador de expresiones aritméticas -*-')
    pa1 = ArithmeticProgression(0, 1, 3)
    print(f'pa1={list(pa1)}')

    pa2 = ArithmeticProgression(0, .5, 3)
    print(f'pa2={list(pa2)}')

    pa3 = ArithmeticProgression(0, 1/3, 1)
    print(f'pa3={list(pa3)}')

    from fractions import Fraction
    pa4 = ArithmeticProgression(0, Fraction(1, 3), 1)
    print(f'pa4={list(pa4)}')

    from decimal import Decimal
    pa4 = ArithmeticProgression(0, Decimal('.1'), .3)
    print(f'pa4={list(pa4)}')

    print()


def __example9() -> None:
    """Ejemplo de generador de progresiones aritméticas con itertools
    """

    import itertools

    print(f'-*- Ejemplo de Generador de expresiones aritméticas con itertools -*-')
    # Es una generación infinita. Para controlar, usamos takewhile.
    gen = itertools.count(1, .5)
    print(f'== Generación de número...')
    print(f'1-->{next(gen)}')
    print(f'2-->{next(gen)}')
    print(f'3-->{next(gen)}')
    print(f'4-->{next(gen)}')
    print(f'5-->{next(gen)}')
    print(f'6-->{next(gen)}')

    gen2 = itertools.takewhile(lambda n: n < 3, itertools.count(1, .5))
    print(f'== Generación de número...')
    print(f'-->{gen2}')

    # 1
    gen2_iter = iter(gen2)
    for i in gen2_iter:
        print(f'+>{i}')

    # 2
    # for i in list(gen2):
    #     print(f'->{i}')


def run() -> None:
    __example1()
    __example2()
    __example3()
    __example4()
    __example5()
    __example6()
    __example7()
    __example8()
    __example9()


if __name__ == '__main__':
    try:
        run()
    except Exception as ex:
        logging.error(f'[ERROR] Example1. Exception=[{ex}]')
