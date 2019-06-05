# Bandit Level 16 -> Level 17


## Question
The credentials for the next level can be retrieved by submitting the password of the current level to a port on localhost in the range 31000 to 32000.
First find out which of these ports have a server listening on them.
Then find out which of those speak SSL and which don’t.
There is only 1 server that will give the next credentials, the others will simply send back to you whatever you send to it.


## Solution
This level needs to be solved using NMAP (finally a real hacker's tool xD).
We needed to use NMAP's selective port range scanning feature to get the only open TCP ports, then simply connect to the one using SSL.
I used the commands <ul>
<li>    Scanning for the ports: `nmap -p 31000-32000 localhost` </li>
<li>    The using `openssl s_client -connect localhost:3790` to connect </li>
</ul>


<small>
P.S: This definately far from the best solution. It turns out that running _nmap_ with _version scanning -sV_ outputs the protocol type of ports too which is much helpful.
</small>
