"""
Event Loop -> executamos multitarefas assíncronas em python
"""

import asyncio


async def hello():
    print('oi...')

el = asyncio.get_event_loop()
el.run_until_complete(hello())
el.close()
