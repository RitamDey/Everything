# Crackeme: Java


To solve this level, we can either read the disassembled `Main.class` or use discompilers like [**JD-Core**](https://github.com/RitamDey/My-Simple-Programs/blob/master/CTF/LSE%20CTF/Java/Main.JD-Core.java) or [**Procyon**](https://github.com/RitamDey/My-Simple-Programs/blob/master/CTF/LSE%20CTF/Java/Main.Procyon.java). Once we get the decompiled Java Code, we can what we are doing is a really just a **XOR Encryption**.
The key is located in the first integer array, and the second integer array holds the cipher we need to achieve and argument we pass is the flag which when **xor-ed** with the key, will produce the cipher.

Now since we know `a xor b = c` and `c xor b = a`, we can just **xor** the entire the cipher array with the key array to produce the required argument we need to pass to produce the cipher array


Flag for the Level **Crackme: Java** -> **1a_JAVa_D_bomb_Atomik**
