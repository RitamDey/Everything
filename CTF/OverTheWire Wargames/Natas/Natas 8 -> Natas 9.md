# Natas 8 -> Natas 9


## Target
Url: [http://natas8.natas.labs.overthewire.org](http://natas8.natas.labs.overthewire.org) <br/>
Username: natas8 <br/>
Password: DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe <br/>
Attack Type: <br/>


## Next Password
This level was pretty simple. Using the **View sourcecode** link, we saw the PHP code for the webpage, which also include the secret needed to get the password.

We see out input is first base64 encoded, then reversed and then convered to a hex-string and matched against a defined secret. So we can implement the reverse operations on the secret to recover the needed input, that will give us the password for next level

Here's the reverse script: [decoder.php](https://github.com/RitamDey/My-Simple-Programs/blob/master/CTF/Natas/decoder.php)
