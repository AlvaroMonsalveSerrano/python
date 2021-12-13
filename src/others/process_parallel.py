'''
Ejemplos definido en el siguiente blob: https://pharos.sh/procesamiento-paralelo-en-python/
'''
import logging

from collections import abc
from multiprocessing import Pool, cpu_count, 
import multiprocessing
from time import sleep

logging.basicConfig(level=logging.DEBUG)


def square(x: int) -> int:
    return x*x


def __ejemplo_1_funciones_en_paralelo() -> None:
    '''
    Ejecución de funciones en paralelo utiliznado el módulo multiprocessing.
    Salida:
        Dataset: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        Result: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
    '''
    print(f'-*- EJEMPLO DE FUNCIONES EN PARALELO -*-')
    dataset = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    print('Dataset: ' + str(dataset))

    agents = 5  # Número de agentes de ejecución
    chunksize = 3  # Tamaño de los datos a procesar por agente.
    with Pool(processes=agents) as pool:
        result = pool.map(square, dataset, chunksize)

    print('Result: ' + str(result))


def calculate(process_name, tasks, results):
    '''
    Función worker de ejemplo.
    '''
    print('[%s] evaluation routine starts ' % process_name)
    seguir: bool = True
    while seguir:
        new_value = tasks.get()
        if new_value < 0:
            print('[%s] evaluation routine quits' % process_name)
            results.put(-1)
            seguir = False
        else:
            compute = new_value * new_value
            sleep(0.02 * new_value)

            print('[%s] received value: %i' % (process_name, new_value))
            print('[%s] calculated value: %i' % (process_name, compute))

            results.put(compute)


def __ejemplo_2_ejecucion_n_funciones_con_cola() -> None:
    print('-*- EJEMPLO DE EJECUCIÓN DE N FUNCIONES CON COLAS -*-')
    manager = multiprocessing.Manager()  # Gestor de procesos.

    # Definición de las colas para la comunicación entre procesos.
    tasks = manager.Queue()
    results = manager.Queue()

    # Definición de un grupo de procesos
    num_processes = 4
    pool = multiprocessing.Pool(processes=num_processes)
    processes = []  # Lista de procesos.

    # Inicialización de los procesos y arranque de los mismos.
    for i in range(num_processes):
        process_name = "P%i" % i
        new_process = multiprocessing.Process(
            target=calculate,
            args=(process_name, tasks, results))

        processes.append(new_process)

        new_process.start()

    # Inicializamos la cola con los datos a procesar
    task_list = [43, 1, 780, 256, 142, 68, 183, 334, 325, 3]
    for single_task in task_list:
        tasks.put(single_task)

    sleep(5)

    # Terminación de los procesos worker. Se encolan los valores de fin de cola para los procesos.
    for i in range(num_processes):
        tasks.put(-1)

    # Lectura de resultdos.
    num_finished_processes = 0
    seguir: bool = True
    while seguir:
        new_result = results.get()
        if new_result == -1:
            num_finished_processes += 1

            if num_finished_processes == num_processes:
                seguir = False

        else:
            print('Result:' + str(new_result))


def run() -> None:
    print(f'Numero cores={cpu_count()}')
    __ejemplo_1_funciones_en_paralelo()
    __ejemplo_2_ejecucion_n_funciones_con_cola()


if __name__ == '__main__':
    try:
        run()
    except Exception as ex:
        logging.error(f'[ERROR] process_parallel. Exception=[{ex}]')
