# Bandit Level 9 -> Level 10


## Problem
The password for the next level is stored in the file data.txt in one of the few human-readable strings, beginning with several ‘=’ characters.


## Solution
This level required using the `strings` utility to find all the human readable strings in the binary encoded files. 
Although we needed to use `grep` utility to actually filter out only the password, But I couldn't find the required regex.

So what I did is find only the human readable strings using the command `strings data.txt`. Then I used some prior expirence to find the passowrd.
