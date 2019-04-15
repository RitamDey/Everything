# Stack Level 5 Notes.


We need to create a breakpoint at `start_level` function at the _nop_ instruction.

The targeted return address is 138 bytes away from the buffer allocated. To view the memory, use the `x/64gx $rbp-0x80` command. It displays all the buffer and the return address in 64-bit format.

The return address is located at memory address **0x7fffffffdd28**. <em>It seems the value of register <b>rbp</b> of the main function is located at <b>0x7fffffffdd20</b></em>

The method using right now is to overflow the 138 bytes from start of buffer and modify the return address to point to the **0x7fffffffdd30**, which will hold the start of the shellcode.

This is hopefully return into the shellcode which will spawn a shell
