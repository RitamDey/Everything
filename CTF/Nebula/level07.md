# Solution to Nebual Level 02

##Task <br>
The flag07 user was writing their very first perl program that allowed them to ping hosts to see if they were reachable from the web server.
To do this level, log in as the level07 account with the password level07. Files for this level can be found in /home/flag07.


## Solution <br>
This level required expoliting a weakness of `unsanitized input`. The PERL script takes a input via the HTTP request. <br>
To start the level, we need to open the _thttpd.conf_ (THTTP Server config file) to get the port number where the webserver is listening. <br>
Once found, it is a simple maliciously crafted request to the CGI (here the **PERL** script) to call the _getflag_ binary.


<small><<b> PS: I took help in the level as I had no clue how to send parameters to PERL scripts
