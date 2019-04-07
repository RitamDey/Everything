# Natas 14 -> Natas 15


## Target
Url: [http://natas14.natas.labs.overthewire.org/index.php](http://natas14.natas.labs.overthewire.org/index.php) <br/>
Username: natas14 <br/>
Password: Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1 <br/>
Attack Type: SQL Injection <br/>


## Next Password
This level was a classic SQL Injection level. All we needed to do in this level was to formulate the username data in such a way that it bypasses the check and creates a always true results and also comments out rest of the hardcoded query statment.


I targeted for this resulting SQL statment 
```SQL
SELECT * FROM users WHERE username="" OR "" = "" -- AND password=""
```

