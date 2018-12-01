# Bandit Level 4 -> Level 5

## Problem
The password for the next level is stored in the only human-readable file in the inhere directory. Tip: if your terminal is messed up, try the “reset” command.


## Solution
The `file` utility is used to find the type of the file. So to get the password we need to issue the command `file inhere/-file0*`. The only file with _ASCII text_ type is the password.
