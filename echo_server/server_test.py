import asyncio
import pytest


@pytest.mark.parametrize('message, response', [
    ('echo hi', 'hi'),
])
def test_coro(message, response, loop):
    async def do_test():
        reader, writer = await asyncio.open_connection('127.0.0.1', 8888, loop=loop)
        writer.write(message.encode())
        data = await reader.read(100)
        assert data.decode() == response

    loop.run_until_complete(do_test())
