import datetime
import math


def main():
    inicio = datetime.datetime.now()

    computar(fim=50_000_000)

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
terminou em 16.54 segundos.
"""
