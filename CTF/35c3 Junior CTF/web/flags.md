# 35C3 Junior CTF 2018


## Challenge
Fun with flags: http://35.207.132.47:84

Flag is at /flag

Difficulty estimate: Easy


<b> Score is 37 </b>


## Solution
This challenge was quite interesting. The PHP code running in the server is given to us.
Studying the code, we can see that the code fist get the **ACCEPT_LANGUAGE** HTTP header, and then takes the first value as input.
It then kindof santitizes `¯\_(ツ)_/¯` the input by removing the _../_ with a _""_. Our objective is to defeat this santization only.
We know that the flag is in **/flag** and the file is read from **/var/www/html/flags**.
So to defeat the sanitization, we can set the **Accept_Language** header with something like _..././..././..././..././flag_, which produces the output _../../../../flag_ after the sanitization.
Now we are done. The rest of the script takes care of reading the flag using path _flags/../../../../flag_, `base64` encoding it and sending it within the `<img>`.
Once we get the response back, we just need to BASE64 decode it using something like `echo flag | base64 -d` to get the plain text flag
Flag is `35c3_this_flag_is_the_be5t_fl4g`
