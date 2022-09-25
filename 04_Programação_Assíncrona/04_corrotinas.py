import asyncio


async def oi_demorado():
    print('Oi...')
    await asyncio.sleep(2)
    print('Pessoal...')

el = asyncio.get_event_loop()
el.run_until_complete(oi_demorado())
el.close()
