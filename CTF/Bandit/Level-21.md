# Bandit Level 21 -> Level 22


## Question
A program is running automatically at regular intervals from cron, the time-based job scheduler.
Look in **/etc/cron.d/** for the configuration and see what command is being executed.


## Solution
This level was pretty easy. When we read the crontab files in **/etc/cron.d**,  we will see a file called `cronjob_bandit22` which is run at every reboot.
Reading the file, we can see it execute another script `/usr/bin/cronjob_bandit22.sh`, which just read the password for **level 22** and writes to a file in _/tmp_.
Since read permission is turned off in _/tmp_, opening the file with `nano` or `vim` will give you the password for **level 22**


Password Level 22: Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI
