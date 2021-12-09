
'''
Chapter2: Un array de secuencias.
'''
import logging
import array
import os
import bisect
import random
import numpy

import array as arr
from collections import namedtuple, deque

logging.basicConfig(level=logging.DEBUG)


def __ejemplos_basicos_map_filter() -> None:
    '''
    Listcomps vs map y filter
    '''

    string_example = 'ABCDEFGH'
    string_list = [ord(s) for s in string_example]
    print(f'==>>{string_list}')

    string_list2 = [ord(s) for s in string_example if ord(s)
                    > 70]  # List comprehension (1)
    print(f'==>>{string_list2}')

    # Función map: 1 param, función ord; 2 parametro, conjunto de elementos iterable.
    map1 = map(ord, string_example)
    print(type(map1))
    print(f'{map1}')
    for elem in map1:
        print(elem)

    # filter y map (2).
    elem_f1 = list(filter(lambda c: c > 70, map(ord, string_example)))
    print(f'elem_f1={elem_f1}')

    # (1) y (2) son iguales.

def __ejemplos_listcomp() -> None:
    colors = ['black', 'white']
    sizes = ['S', 'M', 'L']
    tshirts = [(color, size) for color in colors for size in sizes]
    logging.info(f'\ntshirts={tshirts}')


def __generator_expressions() -> None:
    symbols = 'ABCDEFG'
    tupla1 = tuple(ord(symbol) for symbol in symbols )
    logging.info(f'tupla1={tupla1}')
    
    array1 = array.array("l", (ord(symbol) for symbol in symbols)) # 1 param, tipo datos; 2 param, datos.
    logging.info(f'array1={array1}')
    
    colors = ['black', 'white']
    sizes = ['S', 'M', 'L']
    
    for shirt in ('%s %s' % (c, s) for c in colors for s in sizes):
        logging.info(f'shirt = {shirt}')
        
def __tuplas_como_registros() -> None:
    lax_coordinates = (33,9425, -118,408056)
    city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)        
    traveler_ids = [('USA','123456789'), ('BRA','AW45612'), ('ESP','XDA12356')]
    
    logging.info(f'\n-*- VALORES COMO TUPLAS I -*-')
    for passport in sorted(traveler_ids):
        logging.info('%s/%s' % passport) # Operador % para manejar los valores de las tuplas.

    logging.info(f'\n-*- VALORES COMO TUPLAS II -*-')
    for country, _ in sorted(traveler_ids): # Operador _ (placeholder) para cualquier valor.
        logging.info(country) 
    
def __desempaquetamiento_tuplas() -> None:
    lax_coordinates = (33.9425, -118.408056)
    city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)        
    traveler_ids = [('USA','123456789'), ('BRA','AW45612'), ('ESP','XDA12356')]
    
    print(f'-*- DESEMPAQUETAMIENTO DE TUPLAS -*-')
    latitude, longitude = lax_coordinates
    print(f'latitude={latitude} longitude={longitude}')
       
    latitude, longitude =  longitude, latitude
    print(f'latitude={latitude} longitude={longitude}')     
    
    print(f'->{divmod(20,8)}')    
    t = divmod(20,8)
    print(f'->{t}')
    a, b = divmod(*t)
    print(f'a={a} b={b}')
    
    path, filename = os.path.split('~/.ssh/idrsa.pub')
    print(f'path={path}')
    print(f'filename={filename}')
    
    _, filename2 = os.path.split('~/.ssh/idrsa.pub')
    print(f'filename={filename2}')
    
    a, b, *rest = range(5)
    print(f'a={a} b={b} rest={rest}')
    
    a1, b1, *rest1 = range(3)
    print(f'a={a1} b={b1} rest={rest1}') 
    
    a2, b2, *rest2 = range(2)
    print(f'a={a2} b={b2} rest={rest2}')   
      
      
def __named_tuples() -> None:
    City = namedtuple('City', 'name country population coordinates')
    
    tokyo = City('Tokyo', 'JP', 369933, (35.46461286, 139.646321))
    
    print(f'tokyo={tokyo}')
    print(f'tokyo.population={tokyo.population}')
    print(f'tokyo.population={tokyo.coordinates}')
    print(f'tokyo[1]={tokyo[1]}, tokyo.country={tokyo.country}')
    print(f'City._fields={City._fields}')
    
def __mutable_inmutable_list() -> None:
    print(f'-*- MUTABLE INMUTABLE LIST -*-')
    # Inmutable lista
    l = [1, 2, 3, 4]    
    print(type(l))
    print(l)
    print(id(l))
    l *= 2
    print(l)
    print(id(l))
    
    # Mutable tupla
    t = (1, 2, 3, 4)    
    print(type(t))
    print(t)
    print(id(t))
    t *= 2
    print(t)
    print(id(t))    
    
    
def __ordered_example() -> None:
    fruits = ['grape', 'raspberry', 'apple', 'banana']   
    print(f'-*- Ejemplos de ordenación -*-') 
    print(f'fruits={fruits}')
    print(f'fruits={sorted(fruits)}')
    print(f'fruits={sorted(fruits, reverse=True)}')
    print(f'fruits={sorted(fruits, key=len)}')
    print(f'fruits={sorted(fruits, key=len, reverse=True)}')
    fruits.sort()
    print(f'fruits.sort()={fruits}')
    
def __insert_bisect() -> None:
    
    SIZE = 7
    
    random.seed(1729)
    print(f'-*- Insert bisect (Inserción ordenada en una lista) -*-')
    my_list = []
    for i in range(SIZE):
        new_item = random.randrange(SIZE * 2)
        bisect.insort(my_list, new_item)
        print('%2d ->' % new_item, my_list)
        
        
def __operation_array() -> None:  
    print(f'-*- Operaciones con Array -*-')
    try:
        ints = arr.array("i", (i for i in range(5)))
        print(f'ints={ints[-1]}')
        
        
        floats = arr.array('d', (random.random() for i in range(10**2)))
        print(f'floats={floats[-1]}')
        
        fp = open('floats.bin', 'wb') # Escritura en un fichero desde array
        floats.tofile(fp)
        fp.close()
        
        floats2 = arr.array('d')
        fp2 = open('floats.bin', 'rb') # Lectura de un fichero a un array.
        floats2.fromfile(fp2, 10**2)
        fp2.close()

        print(f'floats2={floats2[-1]}')
        
        
    except Exception as ex:
        raise ex
      
      
def __memory_view() -> None:
    print(f'-*- Operaciones con Memory View -*-')
    numbers = arr.array('h', [-2, -1, 0, 1, 2])
    
    memv = memoryview(numbers)
    print(f'Memv={memv}')
    print(f'len(memv)={len(memv)}')
    print(f'Memv={memv[0]}')
    
    memv_oct = memv.cast('B')
    print(f'memv_oct.tolist={memv_oct.tolist()}')
    memv_oct[5] = 4 # Se cambia la posición de memoria en octal.
    print(f'numbers={numbers}')
    
def __example_numpy() -> None:
    
    print(f'-*- Ejemplos Numpy -*-')
    floats = numpy.loadtxt('floats-lines.txt')
    print(f'floats={floats[-1]}')
    print(f'floats={type(floats)}')
    print(f'floats={floats}')
    
    numpy.save('floats-lines-numpy', floats)
    floats2 = numpy.load('floats-lines-numpy.npy', 'r+')
    floats2 *= 6
    print(f'floats2[-3:]={floats2[-3:]}')
       

def __dequeue_queue() -> None:
    print(f'-*- Ejemplos dequeue -*-')
    dq = deque(range(10), maxlen=10)
    print(f'dequeue={dq}')
    dq.rotate(3) # Rota la posición de los elementos de la cola en 3 elementos.
    print(f'dequeue={dq}')
    dq.rotate(-4)
    print(f'dequeue={dq}')
    dq.appendleft(-1) # Inserción por la izquierda.
    print(f'dequeue={dq}')
    dq.extend([11, 22, 33]) # Inserción por la cola.
    print(f'dequeue={dq}')
    dq.extendleft([10, 20, 30, 40]) # Inserción por la cola.
    print(f'dequeue={dq}')
      
       
def run() -> None:
    __ejemplos_basicos_map_filter()
    __ejemplos_listcomp()
    __generator_expressions()
    __tuplas_como_registros()
    __desempaquetamiento_tuplas()
    __named_tuples()
    __mutable_inmutable_list()
    __ordered_example()
    __insert_bisect()
    __operation_array()
    __memory_view()
    __example_numpy()
    __dequeue_queue()


if __name__ == '__main__':
    try:
        run()
    except Exception as ex:
        logging.error(f'[ERROR] Example1. Exception=[{ex}]')
