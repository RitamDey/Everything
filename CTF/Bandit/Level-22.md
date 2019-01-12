# Bandit Level 22 → Level 23


## Question
A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in **/etc/cron.d/** for the configuration and see what command is being executed.

NOTE: Looking at shell scripts written by other people is a very useful skill. The script for this level is intentionally made easy to read.
If you are having problems understanding what it does, try executing it to see the debug information it prints.


## Solution
This solution needed a little bit of understanding of **bash scripting**. The script first read the username, then created a MD5 sum of the senctence **"I am user <username>"**.
Once done it, remove the ending spacing and "-" (which is used to denote that the input was from stdin, if I'm not wrong). Once the MD5 sum is avaiable, it gets the password and wites to file in **/tmp**.

So all we need to do is get the md5 sum. Once logged in, run `echo I am user bandit23 | md5sum` and copy the md5 sum string and open the file with corresponding name
