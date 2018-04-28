import threading


count = 0


def increment():
    global count
    count += 1


def task(lock):
    for _ in range(10000):
        lock.acquire()
        increment()
        lock.release()


if __name__ == '__main__':
    for i in range(10):
        lock = threading.Lock()

        t1 = threading.Thread(target=task, args=(lock,))
        t2 = threading.Thread(target=task, args=(lock,))

        t1.start()
        t2.start()

        t1.join()
        t2.join()

        print("Interation {0}: {1}".format(i, count))



