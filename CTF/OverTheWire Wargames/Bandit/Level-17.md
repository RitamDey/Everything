# Bandit Level 17 -> Level 18


## Question
There are 2 files in the homedirectory: **passwords.old** and **passwords.new**.
The password for the next level is in **passwords.new** and is the only line that has been changed between **passwords.old** and **passwords.new**


## Solution
This level needs to be solved using the _diff_ tool. The _diff_ is used to view the difference between the contents in 2 two files.
I use _diff_ with the `-u` option only because I more used to `git diff`.
So to find the password we use `diff -u passwords.old passwords.new`.
There will be a line starting with the **+** sign. That's the password for Level 18 _kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd_
