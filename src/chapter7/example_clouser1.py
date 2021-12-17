
import logging


class Averager():

    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)
        pass


def __ejemplo1() -> None:
    print(f'-*- Ejemplo de Clouser: cálculo de la media utilizando una clase con método call -*-')
    avg = Averager()
    print(f'avg(10)={avg(10)}')
    print(f'avg(11)={avg(11)}')
    print(f'avg(12)={avg(12)}')


def make_averager():
    '''
    Definición de una función de tipo clouser.
    '''
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)

    return averager


def __ejemplo2() -> None:
    print(f'-*- Ejemplo de Clouser: cálculo de la media utilizando un clouser  -*-')
    avg = make_averager()
    print(f'avg(10)={avg(10)}')
    print(f'avg(11)={avg(11)}')
    print(f'avg(12)={avg(12)}')


def make_averager2() -> None:
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total/count

    return averager


def __ejemplo3() -> None:
    print(f'-*- Ejemplo de Couser: utilizando una función con la clausula nonlocal -*-')
    avg = make_averager2()
    print(f'avg(10)={avg(10)}')
    print(f'avg(11)={avg(11)}')
    print(f'avg(12)={avg(12)}')
    pass


def run() -> None:
    __ejemplo1()
    __ejemplo2()
    __ejemplo3()


if __name__ == '__main__':
    try:
        run()
    except Exception as ex:
        logging.error(f'[ERROR] example_clouser1. Exception=[{ex}]')
