import asyncio
import datetime


async def gerar_dados(quantidade: int, dados: asyncio.Queue):
    print(f'Aguarde a geração de {quantidade} dados...')

    for idx in range(1, quantidade + 1):
        item = idx * idx
        await dados.put((item, datetime.datetime.now()))
        await asyncio.sleep(0.001)
    print(f'foram gerados {quantidade} dados com sucesso...')


async def processar_dados(quantidade: int, dados: asyncio.Queue):
    print(f'Aguarde a geração de {quantidade} dados...')

    processados = 0
    while processados < quantidade:
        await dados.get()
        processados += 1
        await asyncio.sleep(0.001)
    print(f'foram processados {processados} itens')


def main():
    total = 1500
    dados: asyncio.Queue[int] = asyncio.Queue()
    print(f'Computacao {total * 2:.2f} dados. ')

    el = asyncio.get_event_loop()

    tarefa_01 = el.create_task(gerar_dados(total, dados))
    tarefa_02 = el.create_task(gerar_dados(total, dados))
    tarefa_03 = el.create_task(processar_dados(total * 2, dados))

    tarefas = asyncio.gather(tarefa_01, tarefa_02, tarefa_03)
    el.run_until_complete(tarefas)


if __name__ == '__main__':
    main()
