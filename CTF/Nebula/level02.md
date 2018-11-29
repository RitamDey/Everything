# Solution to Nebual Level 02

##Task <br>
There is a vulnerability in the below program that allows arbitrary programs to be executed, can you find it?
To do this level, log in as the level02 account with the password level02. Files for this level can be found in /home/flag02.


## Solution

This problem, like the previous one, involved using a _SETUID_ permission exploit to get in the target account **flag02**. 
Unlike the previous level, this level required manuipulation to the `USER` environment variable. To exploit the binary, we need to modify the `USER` to the following value `; /bin/bash;`.
This value when copied and executed by the binary, via the `system()` syscall, starts a shell for the account **flag02**.
