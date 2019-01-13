# Leviathan Level 3 → Level 4


This level was a simple string matching problem. Using **ltrace** we can see the program does 2 `strcmp()`. If you see then the first `strcmp()` is just useless, doing comparision between 2 strings.
However the 2nd one, compares the userinput with the string **"snlprintf\n"**, which happens to be the password.
Restart the program, and enter the password, to get a shell of user **leviathan4** and just read the password from **/etc/leviathan**.


Password for level 4 -> vuH0coox6m
