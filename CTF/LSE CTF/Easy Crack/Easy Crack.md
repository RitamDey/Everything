# LSE CTF

## Category: Crackme
## Problem : Easy Crack
## Url: [https://ctf.lse.epita.fr/ex/1/](https://ctf.lse.epita.fr/ex/1/)


The section of main we are interested can be found [here]().
Now in the **LoadArguments** the only thing that is of particular interest to us is `mov	rdx, [rsi+8]`, which loads the second entry of the **argv** command-line arguments into rdx. Note that here only the address to start of the entry of **argv** is copied, not the actual array entries. We also see register eax being initialized to 0 and the address in register rdx to register rdi.

Now moving to the next section, we see that the address of sector **unk_400808** being moved to register ecx, this section actually holds the value which we need to crack. Also register eax is set to 0, which is actually the initialization of the loop

Onto to the next section, we see values pointed by register rdx (our given passowd) to esi and  values pointed by register rcx (the target string) to edi. Once done it xor-es the value in register esi with the value in register eax and then compares it with the value in register edi. If they are same, we move to the incrementation part of the loop, where register eax is incremented by 10, rdx (our given password) value incremented to point to next character of the input and rcx (our target string) value incremented to point to the next target character. Also register eax is checked to see if it's value is equal to 80, which acts as our loop condition


This loop goes on, until either we have a mismtach, which makes the program print 'KO' and exit, or our entire 8 length-ed input checked against the target, which allows the program to print 'OK' and exit, letting us know it's our required password
