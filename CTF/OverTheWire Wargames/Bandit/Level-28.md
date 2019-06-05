# Bandit Level 28 → Level 29


## Question
There is a git repository at **ssh://bandit28-git@localhost/home/bandit28-git/repo**. The password for the user **bandit28-git** is the same as for the user **bandit28**.

Clone the repository and find the password for the next level


## Solution
This level needed to check the hsitory of the repo for previous revisions of the file _README.md_. just keep checking them one-by-one and you get the password.
Get the repository history using `git log`
