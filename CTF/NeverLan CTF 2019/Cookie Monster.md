# NeverLan CTF Web


## Problem Description
It's a classic https://challenges.neverlanctf.com:1110


<b>Problem Score: 20</b>


## Solution
<b><em> I actually found the source code for the site before solving the challenge </em></b>
For this problem, we need to modify the cookies sent by the website. The particular cookie we are interested in `Red_Guy's_name`. The backend runs on PHP and expects a value which will match the regex `([Ee])(lmo)+`.
Therefore setting the value to something like _Elmo_ matches the regex, and we get the flag from the site.
