# CTFLearn V2


## Problem Statment
There are so many different ways of encoding and decoding information nowadays... One of them will work! Q1RGe0ZsYWdneVdhZ2d5UmFnZ3l9


## Solution
Looking in the code, we can easily guess it is a **Base64** encoded string.
So simply using the `echo "Q1RGe0ZsYWdneVdhZ2d5UmFnZ3l9" | base64 -d"`.
And here we have the flag
