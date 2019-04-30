# Natas 15 -> Natas 16


## Target:
Url: [http://natas15.natas.labs.overthewire.org](http://natas15.natas.labs.overthewire.org) <br/>
Username: natas15 <br/>
Password: AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J <br/>
Attack Type: Blind SQL Injection <br/>


## Next Password
This level introduced us to the concept of Blind SQL Attacks. Unlike standard SQL Injections, Blind injections doesn't gives the result of the query. For example in this level because of the usage of the SQL query, the only imformation we get from the SQL injection, is that a record was present or not.
Thus we need to use this imformation only to perform injection and bruteforce the password. The logic behind the query used is that we know the target username would be **natas16** and it will have a associated password of length 32 consisting of lowercase, uppercase and numbers.

We use this information to guess each character and check if the username "**natas16**" has a password like the guessed charcters, case sensitive.
So the our target payload consists like this:
```SQL
natas16" AND password LIKE BINARY "<discovered part of the password><current guess>%
```
You can find the bruteforcer in the file _natas15-exploit.py_ in this folder.

NOTE: Here we have to use the `BINARY` keyword to make `LIKE` comparisons make a case-sensitive string comparisons.
P.S: I didn't solve this level on my own, as I didn't knew about blind SQL attacks. So I had to read a write-up to get a clue. The given payload is copied much from the writeup, although the the exploit code is my own creation.
