# Natas 2 -> Natas 3


## Target
Url: [http://natas2.natas.labs.overthewire.org/](http://natas2.natas.labs.overthewire.org/) <br>
Username: natas2 <br>
Password: ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi <br>
Attack Type: Leaking Directory Listing <br>


## Next Password
This level was quite tricky and I couldn't solve it at first. We need to carefully cross-look the page's source with the rendered page.

If we do cross-look closely we would see this line `lang=html <img src="files/pixel.png">`. If we open the image in a new tab, we would see that it's indeed a white pixel.

Putting a white pixel in a webpage with white background only means one thing, it's the path to password XD. Since the requested url for the image is [http://natas2.natas.labs.overthewire.org/files/pixel.png](http://natas2.natas.labs.overthewire.org/files/pixel.png), we can try requesting [http://natas2.natas.labs.overthewire.org/files](http://natas2.natas.labs.overthewire.org/files).

And indeed we are returned file listing with a strange text file [users.txt](http://natas2.natas.labs.overthewire.org/files/users.txt).

Request the file and we will get the password for next level listed in the file
