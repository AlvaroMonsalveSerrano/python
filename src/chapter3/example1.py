import logging

from collections import abc

logging.basicConfig(level=logging.DEBUG)


def __generic_mapping() -> None:
    my_dict = {}
    print(f'={isinstance(my_dict, abc.Mapping)}')
    
    # Formas de definir un diccionario.
    a = dict(one=1, two=2, three=3)
    b = {'one':1, 'two':2, 'three':3}
    c = dict(zip(['one', 'two', 'three'], [1,2,3]))
    d = dict([('two', 2), ('three', 3), ('one', 1)]) # lista de tuplas a list
    e = dict({ 'three':3, 'two':2, 'one':1 })
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
    r1 = { country:code for code, country in DIAL_CODES}
    print(f'r1={r1}')
    
    pass    

def run() -> None:
    __generic_mapping()
    __dict_comprehension()
    

if __name__ == '__main__':
    try:
        run()
    except Exception as ex:
        logging.error(f'[ERROR] Example1. Exception=[{ex}]')