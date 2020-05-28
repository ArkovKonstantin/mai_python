import asyncio
import datetime


async def handle_echo(reader, writer):
    commands = ['echo', 'calendar', 'stop']

    while True:
        data = await reader.read(100)
        msg = data.decode().split(' ')
        print(msg)
        cmd = msg[0].strip('\r\n')
        addr = writer.get_extra_info('peername')
        print("Received %r from %r" % (msg, addr))
        if cmd not in commands:
            writer.write((str(commands) + '\n').encode('utf-8'))
        elif cmd == 'echo':
            print("Send: %r" % msg[1])
            writer.write(msg[1].encode('utf-8'))
            await writer.drain()
        elif cmd == 'calendar':
            dt = datetime.datetime.now().strftime('%Y.%m.%d %H:%M') + '\n'
            print("Send: %r" % dt)
            writer.write(dt.encode('utf-8'))
        elif cmd == 'stop':
            writer.close()
            break

        writer.drain()


def start_server():
    loop = asyncio.get_event_loop()
    coro = asyncio.start_server(handle_echo, '127.0.0.1', 8888, loop=loop)
    server = loop.run_until_complete(coro)

    # Serve requests until Ctrl+C is pressed
    print('Serving on {}'.format(server.sockets[0].getsockname()))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    # Close the server
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()

start_server()