import time
import concurrent.futures as future
import utils


WORKERS = 4


start = time.time()


with future.ThreadPoolExecutor(max_workers=4) as executor:
    futures = {executor.submit(utils.check_website, address) for address in utils.WEBSITE_LIST}
    future.wait(futures)

end = time.time()


print("Time: %s sec" %(end - start))
