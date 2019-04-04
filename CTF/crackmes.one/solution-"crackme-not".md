The length of the input is in register rax
The length is copied into r15 accounting for the newline character.

At every iteration, r14 is set the value of r15+5.
That value is used to index into the welcome string (ds:welcome).
The value retrieved is copied to al and then added 5 to the ACSCII value of it.
This computed value is then compared the password string in reverse.

At the end of each loop iteration, r15 is decremented by 1.


Or simpler terms the input username should contain all the charcter of password string - 5, but in reverse order.
