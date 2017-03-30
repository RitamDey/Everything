import subprocess
from sys import argv

FLAGS = []
URL = []
ERROR_URLS = []


def parse_flags(flags_statement: str):
    global FLAGS
    flags_statement = flags_statement.strip().split()
    flags_statement.remove('flags')
    for flag in flags_statement:
        if '=' in flag:
            x = flag.replace('=', ' ')
            flag = str(x)
        FLAGS.append(flag)


def parse_file(filename: str=None)-> list:
    if filename is None:
        raise ValueError('You must provide a file name.')
    with open(filename, 'r') as fin:
        statements = fin.read().split('\n')
        statements = sanitize_urls(statements)
        parse_flags(statements[0])
        del statements[0]
    return statements


def sanitize_urls(urls: list):
    for url in urls:
        if url == '':
            urls.remove(url)
    # print('Sanitized urls: ', urls)
    return urls


def parse_urls(statements: list)-> None:
    global URL
    # print('All statements: ', statements)
    for statement in statements:
        if 'dl' in statement:
            URL.append(statement.split()[1])
        if 'exec' in statement:
            print(statement.split())
    # print('Parsed urls are: ', URL)


def downloader(use_errors=False):
    global FLAGS, URL, ERROR_URLS
    stub = ['youtube-dl', ]
    stub.extend(FLAGS)
    if use_errors:
        for url in ERROR_URLS:
            stub.append(url)
            return_code = subprocess.call(stub)
            if return_code == 0:
                ERROR_URLS.remove(url)
    else:
        for url in URL:
            stub.append(url)
            return_code = subprocess.call(stub)
            if return_code != 0:
                ERROR_URLS.append(url)
                print('Error in url ', url)


if __name__ == '__main__':
    parse_urls(parse_file(argv[1]))
    # print('Flags to be passed to youtube-dl are: ', FLAGS)
    downloader()
    if ERROR_URLS:
        downloader()
