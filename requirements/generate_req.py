from sys import argv, exit
from pip import get_installed_distributions


def get_pkgs() -> list:
    """
    Get a list of names of modules installed
    """
    pkgs = []
    for mod in get_installed_distributions():
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
            if 'y' == input('Not a txt file: {file_name}. Continue?[y\\n]'):
                return open(file_name, mode)
    except FileNotFoundError:
        return open(file_name, 'w')


def get_files():
    """
    Returns file objects for all the files given
    """
    for fname in argv[1:]:
        fin =  open_file(fname, 'r+')
        yield fin
        fin.close()


# Iterate over the modules and format them to include
#<module> and write it to the opened file
def process():
    fout = (yield)
    for module in get_pkgs():
        print(module, file=fout)


if __name__ == '__main__':
    line_processor = process()
    next(line_processor)
    for fname in get_files():
        try:
            line_processor.send(fname)
        except StopIteration:
            exit(0)
