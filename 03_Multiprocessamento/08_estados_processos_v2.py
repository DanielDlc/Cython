"""
Compartilhando a memória entre os processos
"""

import ctypes
import multiprocessing
import time


def funcao_01(val, stat):
    if stat.value:
        res = val.value + 10
        stat.value = False
    else:
        res = val.value + 20
        val.value = 200
        stat.value = True

    print(f'O resultado da função 1 é {res}')
    time.sleep(0.001)


def funcao_02(val, stat):
    if stat.value:
        res = val.value + 30
        stat.value = False
    else:
        res = val.value + 40
        val.value = 400
        stat.value = True

    print(f'O resultado da função 2 é {res}')
    time.sleep(0.001)


# compartilhar as variáveis entre os dois processos
def main():
    valor = multiprocessing.Value('i', 100)
    status = multiprocessing.Value(ctypes.c_bool, False)

    p1 = multiprocessing.Process(target=funcao_01, args=(valor, status))
    p2 = multiprocessing.Process(target=funcao_02, args=(valor, status))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


if __name__ == '__main__':
    main()
