# NeverLAN CTF Web


## Problem Statment
To keep my server from doing a lot of work, I made javascript do the heavy lifting of checking a user's password

https://challenges.neverlanctf.com:1135


## Solution
This level required use inspecting some JS code. Once we inspect the code, we can see that everytime we type a letter in username field, a XHR request is made to `get_username.php`. If we inspect once of the response, we can see we get a list of possible usernames in the system. From the list we select the username **Dr. Whom**. Then if we start typing in the password field, we can see a new XHR request made to `get_password.php` with the username as parameter.
If we inspect the response to the new XHR response, we see a **Base64** string, decode it and get the flag
