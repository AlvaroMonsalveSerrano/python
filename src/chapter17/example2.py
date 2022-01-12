
"""
Módulo 2 con ejemplo del capítulo 17 de concurrencia con Futuros.

"""
import os
import time
import logging
import itertools
import sys
import requests
from concurrent import futures

POP20_CC = ('CN IN US ID BR PK NG BD RU JP '
            'MX PH VN ET EG DE IR TR CD FR').split()

BASE_URL = 'http://flupy.org/data/flags'

DEST_DIR = 'downloads/'

MAX_WORKERS = 20


def save_flag(img: bytes, filename: str):
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img)


def get_flag(cc):
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    resp = requests.get(url)
    return resp.content


def show(text):
    print(text, end=' ')
    sys.stdout.flush()


def download_one(cc: str) -> str:
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc


def download_many(cc_list: list):
    workers = min(MAX_WORKERS, len(cc_list))
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(download_one, sorted(cc_list))
        return len(list(res))


def main(download_many):
    t0 = time.time()
    count = download_many(POP20_CC)
    elapsed = time.time() - t0
    msg = '\n{} flags downloaded in {:.2f}s'
    print(msg.format(count, elapsed))


def __example1() -> None:
    print(f'-*- Ejemplo 2 descarga de imagenes con Threads. -*-')
    main(download_many)


def run() -> None:
    try:
        __example1()
    except Exception as siex:
        print(f'Exception __example1={siex}')


if __name__ == '__main__':
    try:
        run()
    except Exception as ex:
        logging.error(f'[ERROR] Example2. Exception=[{ex}]')
