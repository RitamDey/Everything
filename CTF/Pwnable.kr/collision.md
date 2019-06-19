# collision


## Challenge
ssh: `ssh -p2222 col@pwnable.kr`
password: guest


## Solution
This level introduced us to hash collisions and CPU endianess using a toy hash function. We are asked to supply the program with a input that would produce the target hash.
The `check_password` hash function takes the argument as a char array, and casts it to int array. Doing so, every 4 elements in the char array forms one element in the int array.
Summation of these elements forms the hash.

N.B: When providing the input, we need keep in the CPU endianess. I was stuck for longest time beacause of this.

Exploit code
```bash
./col $(python -c "print '\xc9\xce\xc5\x06'*4 + '\xc8\xce\xc5\x06'")
```
