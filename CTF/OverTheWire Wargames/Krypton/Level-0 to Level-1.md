# Krypton Level 0 → Level 1

Welcome to Krypton! The first level is easy. The following string encodes the password using Base64:

**S1JZUFRPTklTR1JFQVQ=**

Use this password to log in to krypton.labs.overthewire.org with username krypton1 using SSH on port 2222. You can find the files for other levels in /krypton/


Solution

Just use `echo S1JZUFRPTklTR1JFQVQ= | base64 -d` and we are done.

Password for Level 1 -> KRYPTONISGREAT
