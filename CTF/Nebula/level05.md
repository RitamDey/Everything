# Solution for Nebual Level 05


# Level Info
Check the **flag05** home directory. You are looking for weak directory permissions

To do this level, log in as the **level05** account with the password **level05**. Files for this level can be found in /home/flag05.


# Solution
As the description says we need to look weak permissions in the home directory of **flag05**.
Although I don't know how adding executable bit means weaker permission than usual, we can copy the backup file to our home directory.
Once copied, we extract the backup archive and extract the `.ssh/` and set all the files to only reable by owner.
Once done use command `ssh -i .ssh/id_rsa flag05@localhost` to login to account **flag05** and you are done.
