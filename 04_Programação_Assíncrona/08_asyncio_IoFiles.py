import asyncio

import aiofiles


async def exemplo_arquivo_01():
    async with aiofiles.open('10_texto.txt') as arquivo:
        conteudo = await arquivo.read()
    print(conteudo)


async def exemplo_arquivo_02():
    async with aiofiles.open('09_links.txt') as arquivo:
        async for linha in arquivo:
            print(linha)


def main():
    el = asyncio.get_event_loop()
    el.run_until_complete(exemplo_arquivo_01())
    el.close()


if __name__ == '__main__':
    main()
