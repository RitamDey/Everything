# NeverLAN CTF web


## Problem Statment
REPORT: A Client forgot his Password... again.
Could you get it for me?
He has a users account and his Lname is Miller if that helps at all.
Oh! and Ken was saying something about a new table called passwd; said it was better to separate things

https://challenges.neverlanctf.com:1155


## Solution
This was also a SQL injection challenge task but here we need to perform join. Although we can complete the task just by dumping the entire `passwd` table and decoding the only **Base64** value

The query I used
```SQL
SELECT * FROM passwd
```
