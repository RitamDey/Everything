from concurrent.futures import ThreadPoolExecutor as threads


if __name__ == '__main__':
    with threads(max_workers=4) as workers:
        pass
