import time
from queue import Queue
from threading import Thread
import utils


WORKERS = 4
queue = Queue()


def worker():
    while True:
        address = queue.get()
        utils.check_website(address)

        # For each address popped, mark it as processed
        queue.task_done()


start_time = time.time()


threads = [Thread(target=worker) for _ in range(WORKERS)]

[queue.put(item) for item in utils.WEBSITE_LIST]


[thread.start() for thread in threads]

# Wait until `.task_done()` is called for all items popped out
queue.join()

end_time = time.time()

print("Time %s sec" %(end_time - start_time))
