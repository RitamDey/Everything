# Solution for Nebula Level 03

## Problem
Check the home directory of **flag03** and take note of the files there.

There is a crontab that is called every couple of minutes.

To do this level, log in as the **level03** account with the password **level03**. Files for this level can be found in `/home/flag03`.


## Solution
The crontab that is set to run every couple of minutes, runs with the permissions of user `flag03`.
So to get the flag, we need a simple script in **writable.d** that pipe the output of `getflag` to a file in _/tmp_.
Once done we can read the file to indeed confirm the flag was executed.
