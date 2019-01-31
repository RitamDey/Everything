# Guid to Nebula Level 06


## Level Info 
The **flag06** account credentials came from a legacy unix system.

To do this level, log in as the **level06** account with the password **level06**. Files for this level can be found in /home/flag06.


## Solution
Eventhough the description says we shall find the files in `/home/flag06`, the real data we need is in `/etc/passwd`.
Use `cat /etc/passwd | grep flag06` to get the login entry for **flag06** account.
Once you have it, copy the info to your localmachine, and run _john_ on it.
