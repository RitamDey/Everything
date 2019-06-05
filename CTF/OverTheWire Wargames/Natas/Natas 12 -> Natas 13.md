# Natas 12 -> Natas 13


## Target
Url: [http://natas12.natas.labs.overthewire.org/](http://natas12.natas.labs.overthewire.org/) <br/>
Username: natas12 <br/>
Password: EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3 <br/>
Attack Type: Unrestricted File Upload<br/>


## Next Password
I didn't solved this challenge and took help of a online writeup. This level introduced us to the concept of Unrestricted File Upload vulnerability in web applications. The server wanted us to upload a image file and it does some pre-computations and gives us the filename that it will use to save our uploaded file.

Since the webapp doesn't does and verification for the file type of the uploaded file, we can just upload a PHP script to the webapp. Although if we do that, we need to first change the destination filename to a **'.php'** or otherwise our browser will try to interpret them as images and out attack shall fail. Once we have uploaded the payload script and changed the extension then, just visiting the uploaded file link will give us the password or next level.

The script I used was
```PHP
<? readfile("/etc/natas_webpass/natas13") ?>
```
