# Bandit Level 23 → Level 24


## Question
A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in **/etc/cron.d/** for the configuration and see what command is being executed.


NOTE: This level requires you to create your own first shell-script. This is a very big step and you should be proud of yourself when you beat this level!

NOTE 2: Keep in mind that your shell script is removed once executed, so you may want to keep a copy around…


## Solution
This level got us writing our very first shell script. What our script needs to do is basically read the file **/etc/bandit_pass/bandit24**, write it to a file in **/tmp** (Don't forget to change the ownership of the file to **bandit23**).
Once done wait for the `cron` to run the file as user **bandit24**. Doing so will result in a file in **/tmp** from where we can simply read the password for **bandit24**.
