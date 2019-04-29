# Solution for "my_first_crackme_in_java"

Contains: <ul>
<li> .java: All the decompiled java files, which I cleaned and commented to help in the reversing. I used jadx Decompiler </li>
<li> calc_key.py: Code that I used to calculate the values used by the program during the key verfication </li>
</ul>

The key verification is really a confusing process. It first took the name of the user and a key and the also the user's country.
Once done, it calculates the sum of the ASCII values of characters in the user's name. and passed it to a class called "Dark" with the selected country and the given key

Inside the Dark class, the first thing that is done, using a class called PermutationGenerator, all the permutations of the selected country name's first 5 characters are calculated and of that the 4th character of the 4th, 11th and 18th permutation are retrieved.

Once done, some calculations are performed on the calculated sum of the name and the ASCII values of the characters. Following once matrix mupltiplication is done, with 2 arrays and the result is stored in array called c, which is a 3x3 matrix. The last of the array c and the calculated value of d, multiplited forms the required key for the given username and country
