# flag


## Challenge Resources


## Writeup
Reading the challenge description, we can guess the file is a packed executable. Running `file` and `strings` on the file also confirms that the executable is packed using UPX packer.
One thing to remember here is that if the binary is packed, then before any reversing and debugging we must always unpack it, otherwise it hinders with the debug procdeure.
Once it has been decompressed using `upx flag -d`, we can just run `gdb` on it.
Disassemble **main** and then we can see comment with a address and annotation of **flag**.
Using `x/s 0x6c2070`, we can view the flag. Submit it
