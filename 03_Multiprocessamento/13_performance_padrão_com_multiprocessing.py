import datetime
import math
import multiprocessing
from concurrent.futures.process import ProcessPoolExecutor


def main():
    qtd_cores = multiprocessing.cpu_count()
    print(f'Realizando o processamento matemático com {qtd_cores} core(s).')

    inicio = datetime.datetime.now()

    with ProcessPoolExecutor(max_workers=qtd_cores) as executor:
        for n in range(1, qtd_cores + 1):
            ini = 50_000_000 * (n - 1) / qtd_cores
            fim = 50_000_000 * n / qtd_cores
            print(f'core {n} processando de {ini} até {fim}')
            executor.submit(computar, inicio=ini, fim=fim)

    tempo = datetime.datetime.now() - inicio

    print(f"terminou em {tempo.total_seconds():.2f} segundos.")


def computar(fim, inicio=10):
    pos = inicio
    fator = 1000 * 10000
    while pos < fim:
        pos += 1
        math.sqrt((pos - fator) * (pos - fator))


if __name__ == '__main__':
    main()

"""
1° terminou em 16.54 segundos, o primeiro com a performance padrão.
2° terminou em 13.01 segundos, esse segundo teste com threads.
3° terminou em 1.92 segundos, esse terceiro com multiprocessamento.
"""
