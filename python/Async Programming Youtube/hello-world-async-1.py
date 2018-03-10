import asyncio


loop = asyncio.get_event_loop()  # Get the main event loop


@asyncio.coroutine
def hello():
    # Using a generator function to print Hello World
    print("Hello")
    yield from asyncio.sleep(3)
    print("World!")


if __name__ == '__main__':
    loop.run_until_complete(hello())

