# Bandit Level 19 -> Level 20


## Question
To gain access to the next level, you should use the setuid binary in the homedirectory.
Execute it without arguments to find out how to use it.
The password for this level can be found in the usual place `(/etc/bandit_pass)`, after you have used the **setuid binary**.


## Solution
This is one of the easiest problems in the track. We need to execute the _bandit20-do_ binary to get a shell with the priviledges of user **level20**.
Doing it pretty easy. Once you have tried some commands with the binary, you will see that it drops priviledges for the commands we pass to except except for `sh` command.
So doing something like `./bandit20-do "sh"` will give us a dash shell with the priviledges of user **level20** and once we are there we can just use it to read the file _/etc/badit_pass/bandit20_ file
