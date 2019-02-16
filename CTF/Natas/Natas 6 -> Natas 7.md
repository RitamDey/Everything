# Natas 6 -> Natas 7


## Target
Url: [http://natas5.natas.labs.overthewire.org/](http://natas5.natas.labs.overthewire.org/) <br>
Username: natas6 <br>
Password: aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1 <br>


## Next Password
I first approached the problem in the wrong way. I first thought I had to exploit the insecure PHP comparison, but in this level we need to bypass the authentication by requesting the secrets file itself.
Using the **View sourcecode**, we can see the `$secret` was included from a file called **includes/secret.inc**. We request this file manually and look at the source-code of the rendered page. And it is , the `$secret`. Now return to the level page and input the secret. And we get the password for next level
