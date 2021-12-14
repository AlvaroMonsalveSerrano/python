import logging
import sys
import re

from collections import abc

logging.basicConfig(level=logging.DEBUG)


def __generic_mapping() -> None:
    my_dict = {}
    print(f'={isinstance(my_dict, abc.Mapping)}')

    # Formas de definir un diccionario.
    a = dict(one=1, two=2, three=3)
    b = {'one': 1, 'two': 2, 'three': 3}
    c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
    d = dict([('two', 2), ('three', 3), ('one', 1)])  # lista de tuplas a list
    e = dict({'three': 3, 'two': 2, 'one': 1})
    print(f'a==b==c==d==e={a==b==c==d==e}')


def __dict_comprehension() -> None:

    DIAL_CODES = [
        (12, 'India'),
        (62, 'Francia'),
        (92, 'Italia'),
        (14, 'Argentina'),
        (52, 'España'),
    ]

    print(f'-*- Dict Comprehension -*-')
    r1 = {country: code for code, country in DIAL_CODES}
    print(f'r1={r1}')


def __handling_missing_key_1() -> None:
    print(f'-*- Missing keys 1-*-')
    # TODO

    WORD_RE = re.compile(r'\w+')

    index = {}

    with open('./resource/file_test.txt', encoding='utf-8') as fp:
        for line_no, line in enumerate(fp, 1):
            for match in WORD_RE.finditer(line):
                word = match.group()
                print(f'line_no={line_no} line={line}')

    fp.close()


def __set_example() -> None:
    l = ['spam', 'spam', 'eggs', 'eggs']
    print(f'l={l}')
    print(f'l={type(l)}')
    print(f'set(l)={set(l)}')
    queue = set(l)
    print(f'queue.pop()={queue.pop()}')  # Elimina un elemento.
    print(f'queue={queue}')

    # set comprenhension
    set_test1 = {i for i in range(10, 100) if (i % 2 == 0)}
    print(f'set_test1={set_test1}')

    set_test2 = {i for i in range(10, 100) if (i > 10 and i <= 30)}
    print(f'set_test2={set_test2}')


def run() -> None:
    __generic_mapping()
    __dict_comprehension()
    __handling_missing_key_1()
    __set_example()


if __name__ == '__main__':
    try:
        run()
    except Exception as ex:
        logging.error(f'[ERROR] Example1. Exception=[{ex}]')
