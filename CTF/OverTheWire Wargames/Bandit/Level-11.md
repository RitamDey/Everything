# Bandit Level 11 -> Level 12

## Problem 
The password for the next level is stored in the file data.txt, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions


## Solution
The problem need to use the `tr` utility to translate the text from ROT13.
The wikipedia article provides character sets for the `tr` utility. Using the given command we pipe the output of `cat data.txt` to decrypt.

The command used `cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'`
