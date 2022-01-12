
"""
Módulo 3 con ejemplo del capítulo 17 de concurrencia con Futuros.

"""
import os
import time
import logging
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
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        to_do = []
        for cc in sorted(cc_list):
            future = executor.submit(download_one, cc)
            to_do.append(future)
            msg = 'Scheduled for {}: {}'
            print(msg.format(cc, future))

        results = []
        for future in futures.as_completed(to_do):
            res = future.result()
            msg = '{} result: {!r}'
            print(msg.format(future, res))
            results.append(res)

    return len(results)


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
