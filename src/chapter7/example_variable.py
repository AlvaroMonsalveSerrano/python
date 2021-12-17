import logging


def f1(a):
    print(a)
    print(c)


b = 6


def f2(a):
    print(a)
    print(b)
    b = 9  # Esta asignación produce la excepción. B


def f3(a):
    global b # Definición oblogatoria para poder utilizar una variable global.
    print(a)
    print(b)
    b = 9


def run() -> None:
    try:
        print(f'-> f1()\n')
        f1(3)
    except Exception as ex:
        print(f'Exception f1={ex}')

    try:
        print(f'-> f2()\n')
        f2(3)
        print(b)
    except Exception as ex:
        print(f'Exception f2={ex}')

    try:
        print(f'-> f3()\n')
        f3(3)
        print(b)
    except Exception as ex:
        print(f'Exception f2={ex}')


if __name__ == '__main__':
    try:
        run()
    except Exception as ex:
        logging.error(f'[ERROR] example_variable. Exception=[{ex}]')
