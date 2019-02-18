# Natas 4 -> Natas 5


## Target
Url: [http://natas4.natas.labs.overthewire.org/index.php](http://natas4.natas.labs.overthewire.org/index.php). <br>
Username: natas4 <br>
Password: Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ <br>
Attack Type: HTTP Request Header Forging <br/>


## Next Password
This level demonstrated that [HTTP Refer Header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer) can be used to leak data from websites.

When we request the website for the first time, we saw a authorization failure saying we needed to be referred from natas5 URL. So to authorize, we just need to modify the _refer_ header to **http://natas5.natas.labs.overthewire.org**.

And voila, we have the password for level 5.
