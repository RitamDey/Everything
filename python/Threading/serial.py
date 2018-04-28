import time
import utils


start_time = time.time()


for address in utils.WEBSITE_LIST:
    utils.check_website(address)

end_time = time.time()


print("Time in Serial %s sec" %(end_time - start_time))

