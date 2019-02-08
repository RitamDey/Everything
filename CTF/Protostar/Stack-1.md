# Protostar

## Stack One
This level looks at the concept of modifying variables to specific values in the program, and how the variables are laid out in memory.

This level is at /opt/protostar/bin/stack1

Hints
<ul>
<li>If you are unfamiliar with the hexadecimal being displayed, “man ascii” is your friend.</li>
<li>Protostar is little endian</li>
</ul>

```C
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
  volatile int modified;
  char buffer[64];

  if(argc == 1) {
      errx(1, "please specify an argument\n");
  }

  modified = 0;
  strcpy(buffer, argv[1]);

  if(modified == 0x61626364) {
      printf("you have correctly got the variable to the right value\n");
  } else {
      printf("Try again, you got 0x%08x\n", modified);
  }
}
```

Just like [Stack 0](https://github.com/RitamDey/My-Simple-Programs/blob/master/CTF/Protostar/Level-0.md), we need to overflow an array to modify a target variable. But here we need to set **modified** to a certain particular value.
From the source we understand the x86 is little-endian, and we need to convert it from little-endinan encoding to a string value that can be passed. I used `pwntools.p32()`, but it can be done with hand.

We know: <ul>
<li> 0x61: 'a' </li>
<li> 0x62: 'b' </li>
<li> 0x63: 'c' </li>
<li> 0x64: 'd' </li>
</ul>
And we know our target value to overwrite in **modified** is **0x61626364**, which when converted from little-endian equals to **0x64636261**, which when decoded usin the ASCII table is **"dcba"**.

Now we to overwrite **modified** with **"dcba"**, we can prefix it with a string of length 64, since **buffer** array is 64 long.
Using command like `./stack1 $(python -c "print 'A' * 64 + 'dcba'")` we can complete the level
