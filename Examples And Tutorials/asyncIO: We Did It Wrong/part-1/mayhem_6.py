import asyncio
import logging
import random
import string
import uuid
import functools
import attr


@attr.s
class PubSubMessage:
    instance_name = attr.ib()
    message_id = attr.ib(repr=False)
    hostname = attr.ib(repr=False, init=False)
    restarted = attr.ib(repr=False, default=False)
    saved = attr.ib(repr=False, default=False)
    acked = attr.ib(repr=False, default=False)

    def __attrs_post_init__(self):
        self.hostname = f"{self.instance_name}.debian.local"


async def save(msg):
    # simulates saving a message to the database
    await asyncio.sleep(random.random())
    msg.saved = True
    logging.info(f"Saved {msg} into database")


async def restart_host(msg):
    # simulation of synchronous work I/O work
    await asyncio.sleep(random.random())
    msg.restarted = True
    logging.info(f"Restarted {msg.hostname}")


def cleanup(msg, context):
    # Non-async cleanup behaviour
    msg.acked = True
    logging.info(f"Done. Acked {msg}")


async def handle_message(msg):
    asyncio.create_task(save(msg))
    asyncio.create_task(restart_host(msg))

    # asyncio.gather runs awaitable objects in the sequence concurrently
    # The results of the awaitable objects are aggregrated into a result list, as well as the exceptions raised by them if return_exceptions is True
    futures = asyncio.gather(save(msg), restart_host(msg))

    callback = functools.partial(cleanup, msg)
    # Add the synchronous callback to be scheduled only when all the callbacks are completed
    futures.add_done_callback(callback)
    await futures


# simulating an external publisher of events
async def publish(queue, publisher_id):
    choices = string.ascii_lowercase + string.digits
    while True:
        msg_id = str(uuid.uuid4())
        host_id = ''.join(random.choices(choices, k=4))
        instance_name = f"cattle-{host_id}"
        msg = PubSubMessage(message_id=msg_id, instance_name=instance_name)
        # Using asyncio.create_task instead await for actually concurrency
        asyncio.create_task(queue.put(msg))
        logging.info(f"[{publisher_id}] Published {msg} message")

        await asyncio.sleep(random.random())
    await queue.put(None)  # Done publishing


async def consume(queue):
    while True:
        # wait for an item from the publisher
        msg = await queue.get()
        logging.info(f"Consumed {msg}")
        # create multiple tasks for scheduling the work
        asyncio.create_task(handle_message(msg))

        
if __name__ == '__main__':
    logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s %(levelname)s: %(message)s",
            datefmt="%H:%M:%S"
    )

    queue = asyncio.Queue()
    # This code for >= 3.7. Earlier versions need manual setup and teardown of event loop
    # asyncio.run(publish(queue, 5))
    # asyncio.run(consume(queue))
    # But for this tutorial we are sticking with the < 3.7 boilerplate, since this is a good habit for clean-up in a service that runs continually.
    loop = asyncio.get_event_loop()
    
    # Create a few number of publishers
    publishers = [publish(queue, i) for i in range(random.randint(1, 1))]
    consumers = [consume(queue) for i in range(random.randint(1, 1))]
    try:
        [loop.create_task(coro) for coro in publishers]
        [loop.create_task(coro) for coro in consumers]
        loop.run_forever()
    except KeyboardInterrupt:
        logging.info("Shutting down as requested....")
    finally:
        loop.close()
        logging.info("Shutdown the Mayhem service...")

