# fd


## Challenge Resources
Url: fd@pwnable.kr <br/>
Port: 2222 <br/>
Password: guest <br/>


## Writeup
This challenge was about the basics of Linux IO, especially how Linux handles file descriptors and the standard input.
Since everthing in Linux is just a file, the standard input of a process is also treated as a file, with the file descriptor of **0**.
So the challenge basically requires to send a number that when subtracted from **0x1234** will result to **0**.
If we send the correct number, then when the program tries to open the file with file descriptor **0**, it will actually open the standard input of the process for reading.
Once we are there, we just need to type in the string **LETMEWIN**, which will get us our flag
