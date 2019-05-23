# bof


## Challenge Resources
Url: nc pwnable.kr 9000 <br/>


## Writeup
This challenge was a introduction to Buffer Overflow techniques. Like any buffer overflow vulun, this challenge involved using a unchecked input function like `gets()`.
The main buffer was 32 bytes long and the target memory was 52 bytes offset away from the start of the buffer. So to overflow the buffer we need to overflow it with 52 bytes of padding and the append the value **"cafebabe"** to the explot to successfully overflow the buffer with the target value.
Also we need to use the `cat -` technique to keep the stdin open even after the first part of the exploit has executed. It prevents the interactive shell from exiting immediatedly due to a close standard in.

The used expoit was
```bash
(python -c 'print "A"*52 + "\xbe\xba\xfe\xca"'; cat -) | nc pwnable.kr 9000
```
