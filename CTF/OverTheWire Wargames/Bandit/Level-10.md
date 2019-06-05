# Bandit Level 10 -> Level 11


## Problem
The password for the next level is stored in the file data.txt, which contains base64 encoded data


## Solution
This is actually very simple. The password is _base64_ encoded. Thus to decode the password we neede to use `base64 -d data.txt`
