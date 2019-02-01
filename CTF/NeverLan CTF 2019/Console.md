# NeverLAN CTF web


## Problem Statment
You control the browser

https://challenges.neverlanctf.com:1120



## Solution.
We need to look at the JS of the site. Eventhough it looks like the site is doing some MD5 hahsing, we need not to worry about the that. The main target is the `getThat()` function. If called using the console with the parameter **"Y"**, we get the flag printed in the page
