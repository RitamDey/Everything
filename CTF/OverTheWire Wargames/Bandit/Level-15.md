# Bandit Level 15 -> Level 16


## Question
The password for the next level can be retrieved by submitting the password of the current level to port 30001 on localhost using SSL encryption.


## Solution
This solution got me looking at the testing with OpenSSL (Look at the recommended reading material :P).

We need to use the client tool that comes with OpenSSL, which works pretty much like telnet except works on the SSL Layers and can use multiple protocols like HTTP, telnet, SMTP.
Just use the <i>s_client</i> like `openssl s_client -connect localhost:30001`.
Unfortunately, piping the output of password to the command doesn't seem to work.
