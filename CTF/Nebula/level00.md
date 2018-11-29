# Solution for Level 00

This level requires you to find a user ID program that will run as the "flag00" account.
You could also find this page by looking for a directory.


### Solution

We need to use the _find_ utility to list all the files and executable that is owned by user **flag00**. 

The command needed is `find -depth -user flag00 / 2> /dev/null`.

The option explanations: <ul>
    <li> `-depth`: Instructs _find_ to recursively search all subdirectories </li>
    <li> `-user`: Instructs _find_ to list only the files and folders which _level00_ user owns </li>
    </ul>

The redirect `2> /dev/null` is used to redirect the permission denied errors to /dev/null. Shortens the output
