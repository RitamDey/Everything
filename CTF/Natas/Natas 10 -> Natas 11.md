# Natas 10 -> Natas 11


## Target
Url: [http://natas10.natas.labs.overthewire.org/](http://natas10.natas.labs.overthewire.org/) <br/>
Username: natas10 <br/>
Password: nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu <br/>
Attack Type: Improper/Incomplete sanitization of user input <br/>


## Next Password
This level was similar to previous level, but in this level we can't just use `&&` or `;` to escape the grep command. Instead to need to abuse the fact that input is just stitched into the existing hrad-coded command, and just also send the **/etc/natas_webpass/natas11** file along with a proper regex to match the password, like **[[::alnum::]]** which means any alpha-numeric string

Doing so greps both the passowrd file and the dictonary file, but since the passwod is the first file name in the command's file list, it will be grep-ed first and result shown first
