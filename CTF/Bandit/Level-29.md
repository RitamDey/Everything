# Bandit Level 29 → Level 30


## Question
There is a git repository at **ssh://bandit29-git@localhost/home/bandit29-git/repo**. The password for the user **bandit29-git** is the same as for the user **bandit29**.

Clone the repository and find the password for the next level.


## Solution
This level got us using the using the brach feature of git. Just remember that initially cloned repos won't show all the braches present in the upstream.
To show all the repos avaliable in the repo use `git branch -l`
