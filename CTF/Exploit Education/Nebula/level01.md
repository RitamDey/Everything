# Solution for Nebula Level 01

Challenge: <br>
There is a vulnerability in the program that allows you to find it?
To do this level, log in the level01 account with the password level01.
Files for this level can be found in **/home/flag01**.


Solution: <br>
This challenge involved exploiting a _SETUID_ flaw in the target binary.
The binary owned by user **flag01** first gets the effective UID and GID of the use **flag01**. Then it sets it owner to **flag01** by calls to `setresgid` and `setresuid` and executes a call to `system()` to run the command `/usr/bin/env echo ...`.

Our target is to trick `/usr/bin/env` to execute a different binary that would log us in to user **flag01**, achieved by overiding the _PATH_ environment variable
