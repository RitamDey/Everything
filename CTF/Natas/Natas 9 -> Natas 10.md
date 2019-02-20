# Natas 9 -> Natas 10


## Target
Url: [http://natas9.natas.labs.overthewire.org/](http://natas9.natas.labs.overthewire.org/) <br/>
Username: natas9 <br/>
Password: W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl <br/>
Attack Type: Unsanitized input <br/>


## Next Password
This level is a big big rabbit hole. Looking at the source you may be lead to believe that the password is actually in _dictionary.txt_, and like me, may waste time in finding the right grep regex.
But upon closer one can see this level is actually abusing the lack of sanitization of input to escape grep command and execute arbitary shell command, here using something like **cat /etc/natas_webpass/natas10** to get the password
