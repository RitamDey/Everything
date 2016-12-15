#!/usr/bin/python3
'''This Script is used to calculate total amount of a list of items .It can be from a file or from inputs'''
'''You must have Python 3.x installed . It comes with most Linux Distros check it by typing 'python3' in terminal'''

from sys import argv, exit

def main():
    sum=0.0
    if argv[1]=="--file":
        for a in open(argv[2],"r"):
            if a!="\n":
                sum+=float(a)
    elif argv[1]=="--input":
        print("Terminate by ctrl+D or ctrl+C")
        try:
            while True:
                sum += float(input())
        except (EOFError, KeyboardInterrupt):
            return sum

    elif argv[1]=="--help":
        return("This script is used to calculate the amount of some amounts\nUsage:\n--file reads prices from a .txt file\n--input reads prices from your inputs\n--help lands you in this help menu")

if len(argv) < 2:
    argv.append('--input')

print(main())
