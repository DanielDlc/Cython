import datetime
import math

# adicionando threading e multiprocessing para modificar a performance padrão
# multiprocessing para pegar a quantidade de core(s)
import threading
import multiprocessing


def main():
    # adicionando números de cores no processador
    qtd_cores = multiprocessing.cpu_count()
    print(f'Realizando o processamento matemático com {qtd_cores} core(s).')

    inicio = datetime.datetime.now()

    # threads com lista
    threads = []
    for n in range(1, qtd_cores + 1):
        ini = 50_000_000 * (n - 1) / qtd_cores
        fim = 50_000_000 * n / qtd_cores
        print(f'core {n} processando de {ini} até {fim}')
        threads.append(
            threading.Thread(
                target=computar,
                kwargs={'inicio': ini, 'fim': fim},
                daemon=True
            )
        )
    [th.start() for th in threads]
    [th.join() for th in threads]

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
2° terminou em 13.01 segundos, esse segundo teste. 
"""
