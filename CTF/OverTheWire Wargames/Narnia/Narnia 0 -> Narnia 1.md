# Narnia Level 0 -> Level 1


## Level Info
SSH: [narnia.labs.overthewire.org](narnia.labs.overthewire.org)
Port: 2226
Username: narnia0
Password: narnia0
Attack Type: Stack Buffer Overflow


## Explation
This level was a simple stack buffer overflow. We were a binary that has a buffer of size 20.
From the given source code, we can understand that the target is located just after the buffer, in the stack and also there is no padding between the buffer and variable.
This works for our benifit since now we can fill the buffer with random valeues appended with the target value **\xdeadbeef** in `Little-endian` format.
Also we need to take care to make sure out stdin remains open after the exploit command runs, to get a interactive shell.


Keeping all that in mind, that exploit command I used:
```bash
(python -c"print 'A'*20 + '\xef\xbe\xad\xde'"; cat -) | ./narnia0
```

This gave kept the stdin open for the shell to work, and using that opened shell, I `cat`-ed the password for narnia1

