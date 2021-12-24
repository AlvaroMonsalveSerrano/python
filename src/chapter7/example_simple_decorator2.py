import logging
import time
import functools

from module_decorators2 import clock


@clock()
def snooze(seconds):
    time.sleep(seconds)


@clock('{name}: {end}s')
def snooze2(seconds):
    time.sleep(seconds)


@clock('{name}({args}) dt={end:0.3f}s')
def snooze3(seconds):
    time.sleep(seconds)


def __example1():
    print(f'-*- Parametrización de decorador -*-')
    print(f'[1]')
    for i in range(3):
        snooze(0.123)

    print(f'[2]')
    for i in range(3):
        snooze2(0.123)

    print(f'[3]')
    for i in range(3):
        snooze3(0.123)


def run() -> None:
    __example1()


if __name__ == '__main__':
    try:
        run()
    except Exception as ex:
        logging.error(f'[ERROR] example_simple_decorator. Exception=[{ex}]')
