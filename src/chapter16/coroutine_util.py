from functools import wraps


def coroutine(func):
    """
    Definición de un decorador para una corrutina.
    """
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    
    return primer