# Natas 5 -> Natas 6


## Target
Url: [http://natas5.natas.labs.overthewire.org/](http://natas5.natas.labs.overthewire.org/) <br>
Username: natas5 <br>
Password: iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq <br>


## Next Password
This level introduced us that insecure Session Cookies that can abused to bypass authorization of the website. 
Here we see that when we first requested the site, a Session Cokkie called <em>loggedin</em> was set to 0, indicatting we are not logged into the site. Modifying to 1 and requesting the site again, bypassed the authorization of the site and we get the password of next level.
