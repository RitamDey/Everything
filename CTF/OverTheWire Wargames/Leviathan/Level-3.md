# Leviathan Level 2 → Level 3


I took some help in this. The binary we are given is a setuid program that first tires to check if I have access to a file and, if I have access, try to read it using `cat` command.
This internally it is using **access()** and **system()** syscalls, we can trick the binary with crafted filename like _&& bash_ or _; bash_ to get a shell


Password for level 3 -> Ahdiemoo1j
