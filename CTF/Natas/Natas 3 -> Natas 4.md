# Natas 3 -> Natas 4


## Target
Url: [http://natas3.natas.labs.overthewire.org](http://natas3.natas.labs.overthewire.org)
Username: natas3
Password: sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14


## Next Password
This level was actually and I actually once thought it had something to do with Google Indexing. But it turns out that by **<!-- No more information leaks!! Not even Google will find it this time... -->**, the creators meant that they used a <b>_robots.txt_</b> to block spiders from indexing.

If we request the [robots.txt](http://natas3.natas.labs.overthewire.org/robots.txt), we can see the creators banned all spiders from indexing [/s3cr3t](http://natas3.natas.labs.overthewire.org/s3cr3t/).

So we head there, and were presented with a file listing with a single file [users.txt](http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt). Requesting the file, we are presented with the login credentials for level 4.
