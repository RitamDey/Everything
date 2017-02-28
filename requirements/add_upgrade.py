from sys import argv, exit

def open_file(file_name: str, mode: str):
    try:
        return open(file_name, mode)
    except FileNotFoundError:
        print(f'{file_name} could not be found.')
        exit(1)


fin = open_file(argv[1], 'r')  # Open the file now in read-only mode
modules = fin.read().split('\n')  # Get the contents and split by \n
fin.close()  # Best Practice, Close the file


fout = open_file(argv[1], 'r+')  # Open the file for final time in write mode

# Iterate over the modules and format them to include
# --upgrade <module> and write it to the opened file

for module in modules:
    if module == '' or len(module) == 1:
        continue
    if module.find('--upgrade') == 0:
        print(module, file=fout)
    else:
        print(f'--upgrade {module}', file=fout)

fout.close()  # Best Practice, Close the file
