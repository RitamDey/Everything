# Natas 13 -> Natas 14


## Target
Url: [http://natas13.natas.labs.overthewire.org/](http://natas13.natas.labs.overthewire.org/) <br/>
Username: natas13 <br/>
Password: jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY <br/>
<<<<<<< HEAD
Attack Type: <br/>


## Next Password

=======
Attack Type: Unrestricted File Upload <br/>


## Next Password
This level was pretty similar to the previous level and it differed only in one place. This level employed a insecure protection against **Unrestricted File Upload** attack, via using PHP's `exif_imagetype()` which checks to see if the uploaded image is actually a image or not. 

To bypass this check we need to just write the magic bytes of JPEG in the very beginning of the payload we wish to upload to the server. I used the previous payload but prepened the magic bytes `FF D8 FF DB` in the begining of the file using a hex editor.

Once done, we also need to make sure the server saves the payload as PHP script to that when requested, the script would be executed. Once we are done, we can upload the modified payload to the server and then visit the generated URL to get the password for next level
>>>>>>> 94918c01abc922a554257c67f356dd5571864779
