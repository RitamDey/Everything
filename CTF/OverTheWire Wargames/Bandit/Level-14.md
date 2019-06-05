# Bandit Level 14 -> Level 15


## Question
The password for the next level can be retrieved by submitting the password of the current level to port 30000 on localhost.


## Solution
A simple telnet connection to port _30000_ on _localhost_ would do.
Once connected just use just input the password of  **level14** and our are done.
However using **netcat** would be much simpler.

Just use `cat /etc/badit_pass/bandit14 | nc localhost 30000`.
