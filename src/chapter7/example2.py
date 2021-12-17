import logging
from typing import Any

from module_decorators import register_decorator


def function0() -> None:
    print(f'Run() function0')


@register_decorator
def function1() -> None:
    print(f'Run() function1')


def function2() -> None:
    print(f'Run() function2')


def run() -> None:
    '''
    La salida por consola es la siguiente:

        Entramos en register_decorator
        Run() function0
        running register(<function function1 at 0x10df85ca0>)
        Run() function1
        Run() function2    

    '''
    function0()
    function1()
    function2()


if __name__ == '__main__':
    try:
        run()
    except Exception as ex:
        logging.error(f'[ERROR] Example2. Exception=[{ex}]')
