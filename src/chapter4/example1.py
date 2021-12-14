import logging
import sys
import re
import os

from collections import abc

logging.basicConfig(level=logging.DEBUG)


def __file_unicode() -> None:
    file_test = open('./resource/file_test.txt', encoding='utf-8')
    print(f'file_test={file_test}')
    file_test.close()

    print(f"Tamaño del fichero=>{os.stat('./resource/file_test.txt').st_size}")

    ft2 = open('./resource/file_test.txt', encoding='utf-8')
    print(f"Lectura del fichero=>{ft2.read()}")
    ft2.close()


def run() -> None:
    __file_unicode()


if __name__ == '__main__':
    try:
        run()
    except Exception as ex:
        logging.error(f'[ERROR] Example1. Exception=[{ex}]')
