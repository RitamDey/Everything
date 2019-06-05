# Bandit Level 18 -> Level 19


## Question
The password for the next level is stored in a file readme in the homedirectory.
Unfortunately, someone has modified .bashrc to log you out when you log in with SSH.


## Solution
For this solution, we will use the fact that we can specify the command when we login to a user using ssh.
So we can issue the command `ssh -p 2220 bandit18@bandit.labs.overthewire.org "cat *"` to read all the visible file. Actually the password is stored in a file called **readme**.


P.S: If you are interested to know how the connection always end, then you can `cat` the _.bashrc_ file, to see that the last command in the file is basically a exit command to exit the shell. 
And so if you want a shell for some reason, you can always pass `sh -i` command to start a dash shell session
