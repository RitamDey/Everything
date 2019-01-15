# Krypton Level 1 → Level 2


## Problem
The password for level 2 is in the file ‘krypton2’. It is ‘encrypted’ using a simple rotation.
It is also in non-standard ciphertext format.
When using alpha characters for cipher text it is normal to group the letters into 5 letter clusters, regardless of word boundaries.
This helps obfuscate any patterns. This file has kept the plain text word boundaries and carried them to the cipher text. Enjoy!


## Solution
Upon reading the **README** in **/krypton/krypton1**, we can see that the cipher is _ROT13_. So even though we can solve it using web tool, I decided to write a [simple script](https://github.com/RitamDey/My-Simple-Programs/blob/master/CTF/Krypton/krypton1.py) to decrypt the cipher text. The decrypted text is the the password.


The password for Level 3 -> ROTTEN
