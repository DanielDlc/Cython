"""
Uma pool (piscina de processos) nada mais é do que multiprocessos
que você cria para realizar uma determinada tarefa.
Podemos mapear tarefas (funções) para serem executadas pelo projeto através
do método map() da pool.
"""
import multiprocessing


def calcular(dado):
    return dado ** 2


def main():
    tamanho_pool = multiprocessing.cpu_count() * 2

    print(f'tamanho da pool: {tamanho_pool}')

    pool = multiprocessing.Pool(processes=tamanho_pool)

    entradas = list(range(7))
    saidas = pool.map(calcular, entradas)

    print(f'saídas: {saidas}')

    pool.close()
    pool.join()


if __name__ == '__main__':
    main()
