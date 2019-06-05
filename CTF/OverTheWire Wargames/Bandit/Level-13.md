# Bandit Level 13 -> Level 14


## Question
The password for the next level is stored in `/etc/bandit_pass/bandit14` and can only be read by user _bandit14_.
For this level, you don’t get the next password, but you get a _private SSH key_ that can be used to log into the next level.
**Note: localhost is a hostname that refers to the machine you are working on**


## Solution
This level required the knowledge of `SSH Public/Private Key Authentication`.
We are given the required **private identification key** for user _bandit14_.
We just needed to login to the _bandit14_ account using SSH with the key.
Just issue  `ssh -i <file> bandit14@localhost`
