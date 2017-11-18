import asyncio


def hello(loop):
    print("Hello World")
    loop.stop()


loop = asyncio.get_event_loop()

loop.call_soon(hello, loop)

loop.run_forever()
loop.close()
