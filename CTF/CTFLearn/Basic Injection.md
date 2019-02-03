# CTFLean V2


## Problem
See if you can leak the whole database. The flag is in there somwhere… [https://web.ctflearn.com/web4/](https://web.ctflearn.com/web4/)


## Solution
This is was simple SQL Injection attack. We can use simple **always true** injections like `' = '`. This will return true for all rows in all the tests.


<small>P.S: Even though I solved the problem, I later forgot how I did it and had to look at a writeup</small>
