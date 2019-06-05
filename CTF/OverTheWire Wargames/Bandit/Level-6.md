# Bandit Level 6 -> Level 7


## Question
The password for the next level is stored somewhere on the server and has all of the following properties:
    [] owned by user bandit7
    [] owned by group bandit6
    [] 33 bytes in size


## Solution
This solution required using the `find` and `cat` utility.
The command for finding the file is `find -depth -size 33c -user bandit6 -group bandit7 2> /dev/null`. Then use the `cat` utility to read the file.

The explanation of switches are:
    [] `-depth`: Recursively search the subdirectories
    [] `-size 33c`: Only find the files which have size of 33 bytes
    [] `-user bandit6`: Only search for files which are owned by user <b>bandit6</b>
    [] `-group bandit7`: Only search for files which are in group <b>bandit7</b>
Also redirect the error output to `/dev/null`
