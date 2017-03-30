from sys import argv, exit, stdout
from pip import get_installed_distributions

INCLUDE_PKGS = None
USE_VERSION = False


def parse_arguments():
    """
    Searches argv for flags
    and sets some global variables
    """
    global USE_VERSION
    global files
    global INCLUDE_PKGS
    files = list()
    USE_VERSION = False
    if '--set-min' in argv:
        USE_VERSION = True
        argv.remove('--set-min') # Remove them so they don't intergere with others
    if '--dump' in argv:
        files.append(stdout)
        argv.remove('--dump')
    if '--include' in argv:
        INCLUDE_PKGS = input('Enter main requirements file ')
    files.extend(argv[1:])


def get_pkgs() -> list:
    """
    Get a list of names of modules installed
    """
    global USE_VERSION
    global INCLUDE_PKGS
    pkgs = []
    if INCLUDE_PKGS:
        pkgs.append(f'-r {INCLUDE_PKGS}')
    for mod in get_installed_distributions():
        if USE_VERSION:
            pkgs.append(f'{mod.project_name}>={mod.parsed_version}')
        else:
            pkgs.append(mod.project_name)
    pkgs.sort()  # Because pip freeze returns in sorted order
    print(len(pkgs))
    return pkgs


def open_file(file_name: str, mode: str):
    """
    Return a file object for the file_name sent with the given mode
    """
    try:
        if 'txt' in file_name.split('.'):
            return open(file_name, mode)
        else:
            if 'y' == input(f'Not a txt file: {file_name}. Continue?[y\\n]'):
                return open(file_name, mode)
    except FileNotFoundError:
        return open(file_name, 'w')


def get_files():
    """
    Returns file objects for all the files given
    """
    global files
    for fname in files:
        if fname == stdout:
            yield fname
        fin = open_file(fname, 'r+')
        yield fin
        fin.close()


# Iterate over the modules and format them to include
#<module> and write it to the opened file
def process():
    fout = (yield)
    for module in get_pkgs():
        print(module, file=fout)


if __name__ == '__main__':
    if len(argv) == 1:
        print("Usage generate_req.py [--dump] [--set-min] <output file name>\n\nOptions:\n--dump: Dump the requirements to stdout\n--set-min: Sets the current installed version as minimum for all packages\n")
    parse_arguments()
    line_processor = process()
    next(line_processor)
    for fname in get_files():
        try:
            line_processor.send(fname)
        except StopIteration:
            exit(0)
