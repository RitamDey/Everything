# CTFLearn V2


## Problem Information
Try to bypass my security measure on this site! http://165.227.106.113/header.php


## Solution
From the statment, we can understand that we need to modify and tinker with the HTTP request headers. Opening the website source we can see the needed User Agent to be _Sup3rS3cr3tAg3nt_.
Requesting to the same site with that User Agen, we can see that the site expects us to referred from _awesomesauce.com_.

Using all these information and using `curl`, we request the site again using the command `curl --user-agent Sup3rS3cr3tAg3nt --referer awesomesauce.com http://165.227.106.113/header.php`, and we get the flag
