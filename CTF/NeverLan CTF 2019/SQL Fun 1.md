# NeverLAN CTF web


## Probelm Statment
REPORT: 'My Customer forgot his Password. His Fname is Jimmy. Can you get his password for me? It should be in the users table'

https://challenges.neverlanctf.com:1150


## Solution
This was a simple SQL Injection. Actually it's not a hack tbh. We just need to write a regular SQL query for the flag. If you actually wnat we can even dump the entire `users` table like
```SQL
SELECT * FROM users WHERE '' = ''
```
