#!/usr/bin/python3
'''This Script is used to calculate total amount of a list of items .It can be from a file or from inputs'''
from sys import argv

def main():
    sum=0.0
    if argv[1]=="--file":
        for a in open(argv[2],"r"):
            if a!="\n":
                sum+=float(a)
    elif argv[1]=="--input":
        print("When you have ended type 'end'")
        a="0"
        while a!="end":
            a=input()
            if a!="end":
                sum+=float(a)
    elif argv[1]=="--help":
        sum="This script is used to calculate the amount of some amounts\nUsage:\n--file reads prices from a .txt file\n--input reads prices from your inputs\n--help lands you in this help menu"
    else:
        sum="Err!!!Option not found try with --help option"
    return sum

print(main())
amts=1
choice=str()
while choice!="n":
 print("Use again? (y/n) ")
 choice=input()
 if choice == "y":
     if argv[1]!="--input" or argv[1]!="--file":
         print("Enter your option without the --")
         argv[1]="--"+input()
         if argv[1]=="--file":
              print("Enter new .txt file name here")
              argv.append(input())
     print(main())
     amts+=1
 elif choice == "n":
    print("Used %i times\nThanks for using" %(amts))
 else:
     print("Err! Wrong choice "+choice)
