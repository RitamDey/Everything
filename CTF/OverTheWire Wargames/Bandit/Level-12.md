# Bandit Level 12 -> Level 13


## Question
The password for the next level is stored in the file data.txt, which is a hexdump of a file that has been repeatedly compressed.
For this level it may be useful to create a directory under /tmp in which you can work using mkdir.
For example: mkdir /tmp/myname123. Then copy the datafile using cp, and rename it using mv (read the manpages!)


## Solution
This was till now the most boring level yet. The file was _gzipped_, _tar-ed_and _bzip-ed_ 8-9 times. But to get to the archives we needed to first decrypt the given hexdump which was done using the command `xxd -r data.txt`
