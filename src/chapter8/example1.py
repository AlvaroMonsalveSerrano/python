

import logging
import time
import functools
import copy


class Bus:

    def __init__(self, passenguers=None) -> None:
        if passenguers is None:
            self.passenguers = []
        else:
            self.passenguers = list(passenguers)

    def pick(self, name):
        self.passenguers.append(name)

    def drop(self, name):
        self.passenguers.remove(name)


def __example1():
    print(f'-*- Deep and shallow copies -*-')
    bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
    bus2 = copy.copy(bus1)  # Copia solo etiquetas.
    bus3 = copy.deepcopy(bus1)  # Copia etiquetas y valores

    print(f'bus1={bus1}')
    print(f'bus2={bus2}')
    print(f'bus3={bus3}')
    print()
    print(f'bus1={bus1.passenguers}')
    print(f'bus2={bus2.passenguers}')
    print(f'bus3={bus3.passenguers}')
    print()

    print(f'id(bus1)={id(bus1)}')
    print(f'id(bus2)={id(bus2)}')
    print(f'id(bus3)={id(bus3)}')
    print()

    bus1.drop('Bill')  # Elimina de bus1 y bus2.

    print(f'bus1={bus1}')
    print(f'bus2={bus2}')
    print(f'bus3={bus3}')
    print()

    print(f'bus1={bus1.passenguers}')
    print(f'bus2={bus2.passenguers}')
    print(f'bus3={bus3.passenguers}')
    print()


def __example2():
    print(f'-*- Ciclos -*-')
    a = [10, 20]
    b = [a, 30]
    print(f'a={a}')
    print(f'b={b}')
    print()

    a.append(b)
    print(f'a={a}')  # a=[10, 20, [[...], 30]] -> [...]=ciclo
    print(f'b={b}')  # b=[[10, 20, [...]], 30] -> [...]=ciclo
    print()

    c = copy.deepcopy(a)
    print(f'a={a}')
    print(f'c={c}')
    print()


class TwilightBus:
    """Ejemplo de un bus con programación defensiva con el parámetro de entrada, una lista.
    """

    def __init__(self, passenguers=None) -> None:
        """
        Se define con valor por defecto a None porque los valores por defecto son evaluados 
        cuando se carga el módulo.

        Args:
            passenguers ([type], optional): Lista de pasajeros. Defaults to None.
        """
        if passenguers is None:
            self.passenguers = []

        else:
            self.passenguers = list(passenguers)

    def pick(self, name):
        self.passenguers.append(name)

    def drop(self, name):
        self.passenguers.remove(name)

    def __repr__(self) -> str:
        elem = ""
        if len(self.passenguers) > 0:
            for passe in self.passenguers:
                elem = elem + f" '{passe}'"

        return 'TwilightBus([%s])' % (elem)


def __example3():
    print(f'-*- Programación defensiva -*-')
    bus1 = TwilightBus([])

    print(f'bus1={str(bus1)}')
    print()

    bus1.pick('A1')
    bus1.pick('A2')
    print(f'bus1={bus1}')
    print()


def run() -> None:
    __example1()
    __example2()
    __example3()


if __name__ == '__main__':
    try:
        run()
    except Exception as ex:
        logging.error(f'[ERROR] example1. Exception=[{ex}]')
