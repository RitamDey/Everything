# NeverLAN CTF Scripting/Coding


## Challenge Description
To verify that only computers can access the website, you must reverse the Caesar cipher There are a list of possible words that the cipher may be here

https://challenges.neverlanctf.com:1160



## Solution
This was a simple bruteforce problem. We needed to bruteforce the Caesar cipher present in the website with all possible key and send all possible deciphered text to the server to see if we got it right.
Eventually we will as there are only 26 valid keys in Caesar Cipher. I used this script to get the flag: [caesar-cipher-bruteforce.py](https://github.com/RitamDey/My-Simple-Programs/blob/master/CTF/NeverLan%20CTF%202019/caesar-cipher-bruteforce.py)
