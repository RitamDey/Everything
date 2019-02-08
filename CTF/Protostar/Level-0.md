# Protostar

## Stack Zero
This level introduces the concept that memory can be accessed outside of its allocated region, how the stack variables are laid out, and that modifying outside of the allocated memory can modify program execution.

This level is at /opt/protostar/bin/stack0

```C
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>

int main(int argc, char **argv)
{
  volatile int modified;
  char buffer[64];

  modified = 0;
  gets(buffer);

  if(modified != 0) {
      printf("you have changed the 'modified' variable\n");
  } else {
      printf("Try again?\n");
  }
}
```


The disassembly of the **main()** function.
```Assembly
;========================= Setup Stack and save return address ======================================================
0x080483f4 <main+0>:	push   ebp                        ; Push the Caller's base address in the stack. Now the address in stack pointer ESP can be used as base address for main()
0x080483f5 <main+1>:	mov    ebp,esp                    ; Copy the base stack address to base address pointer EBP, since stack pointer ESP is modified during execution
0x080483f7 <main+3>:	and    esp,0xfffffff0             ; Algin stack addresses for 32-bit
;======================== Main logic and code of main() =============================================================
0x080483fa <main+6>:	sub    esp,0x60                   ; Allocate 96 bytes memory as function stack
0x080483fd <main+9>:	mov    DWORD PTR [esp+0x5c],0x0   ; Initialize the modified variable
0x08048405 <main+17>:	lea    eax,[esp+0x1c]             ; Load the address for the base address of array buffer
0x08048409 <main+21>:	mov    DWORD PTR [esp],eax        ; Copy the calculated address to the top of stack
0x0804840c <main+24>:	call   0x804830c <gets@plt>       ; Call the gets() function
0x08048411 <main+29>:	mov    eax,DWORD PTR [esp+0x5c]   ; Copy the content of modified variable to register EAX
0x08048415 <main+33>:	test   eax,eax                    ; Test if register EAX is 0 or not
0x08048417 <main+35>:	je     0x8048427 <main+51>        ; Jump to else part if EAX is 0,
;================================================ IF Section ========================================================
0x08048419 <main+37>:	mov    DWORD PTR [esp],0x8048500  ; Copy the success message to the top of stack
0x08048420 <main+44>:	call   0x804832c <puts@plt>       ; Call the puts() function
0x08048425 <main+49>:	jmp    0x8048433 <main+63>        ; Jump to the return sequence 
;============================================== Else Section ========================================================
0x08048427 <main+51>:	mov    DWORD PTR [esp],0x8048529  ; Copy the failure message to the top of the stack
0x0804842e <main+58>:	call   0x804832c <puts@plt>
;==================================== End of If/Else Section ========================================================
;============================= Return Instruction for main() ========================================================
0x08048433 <main+63>:	leave                             ; Restore the caller function's base pointer register EBP
0x08048434 <main+64>:	ret                               ; Return to the caller function
```


In the C code, we see that `modified` variable is marked `volatile`. The significance of `volatile` keyword is that it informs the compiler that the variable may change any time and to avoid optimizing out the variable. It's needed for this stack overflow to work, since the only time `modified` variable is modified is during the overflow.

Now in the disassembly section 0x080483fa, we can see 96 bytes are made avaliable for the local variables, where 0xbffff74c (ESP + 0x1C) is start address for the array **buffer**. And the variable **modified** is located just after **buffer** ends, i.e 0xbffff780 (ESP + 0x5C).

We also know that **buffer** is 64 bytes long, thus feeding the program with a input larger than 64 will overflow and modify the **modified** variable and we successfully get the success message
