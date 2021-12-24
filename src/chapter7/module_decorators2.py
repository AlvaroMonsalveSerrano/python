import time

DEFAULT_FMT = '[{end:0.8f}s] {name}({args}) -> {result}'


def clock(fmt=DEFAULT_FMT):
    '''
    Función decoradora que permite recibir parámetros de entrada.
    '''
    def decorate(func):

        def clocked(*_args):
            start = time.time()
            _result = func(*_args)
            end = time.time() - start
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_result)
            print(fmt.format(**locals()))
            return _result

        return clocked

    return decorate
