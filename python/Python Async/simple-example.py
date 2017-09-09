import asyncio


async def foo(delay):
    for i in range(10):
        print("Printing with delay %.2f" %delay, end=" ")
        print(i)
        await asyncio.sleep(delay)


def stopper(loop):
    loop.stop()


# Schedule a call to foo
loop = asyncio.get_event_loop()
loop.create_task(foo(0.5))
loop.create_task(foo(1))
loop.create_task(foo(0.25))
loop.call_later(12, stopper, loop)


# Block until loop.stop() is called
loop.run_forever()
loop.close()
