import asyncio
import datetime
import math


def main():
    print('Realizando o processamento matemático de forma assíncrona.')

    el = asyncio.get_event_loop()
    inicio = datetime.datetime.now()

    tarefa_01 = el.create_task(computar(inicio=1, fim=10_000_000))
    tarefa_02 = el.create_task(computar(inicio=10_000_001, fim=20_000_000))
    tarefa_03 = el.create_task(computar(inicio=20_000_001, fim=30_000_000))
    tarefa_04 = el.create_task(computar(inicio=30_000_001, fim=40_000_000))
    tarefa_05 = el.create_task(computar(inicio=40_000_001, fim=50_000_000))

    tarefas = asyncio.gather(
        tarefa_01, tarefa_02, tarefa_03, tarefa_04, tarefa_05
    )
    el.run_until_complete(tarefas)

    tempo = datetime.datetime.now() - inicio
    print(f'Terminou em {tempo.total_seconds():.2f} segundos.')


async def computar(fim, inicio=1):
    pos = inicio
    fator = 1000 * 1000
    while pos < fim:
        pos += 1
        math.sqrt((pos - fator) * (pos - fator))

if __name__ == '__main__':
    main()
