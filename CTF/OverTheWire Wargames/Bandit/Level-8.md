# Bandit Level 8 -> Level 9


## Question
The password for the next level is stored in the file data.txt and is the only line of text that occurs only once


## Solution
This level was a bit tricky in the sense that even though you may be tempted to use `uniq -u data.txt` right away.
But we need to keep in mind that `uniq` only compares adjacent strings for uniqness and no where in the question it is said that repeating stringswill be placed adjacently.

So we need to first sort the file alphbetically, the apply `uniq -u` to get the only unique string

The command I used is `cat data.txt | sort | uniq -u`
