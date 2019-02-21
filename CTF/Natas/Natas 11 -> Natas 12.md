# Natas 11 -> Natas 12


## Target
Url: [https://natas11.natas.labs.overthewire.org](https://natas11.natas.labs.overthewire.org) <br/>
Username: natas11 <br/>
Password: U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK <br/>
Attack Type: Encryption (here Xor Encryption) Reverse Engineering<br/>


## Next Password
I actually had to take help in this level as I couln'd get my decrypter script to work properly. This level required us to reverse engineer the Xor encryption to reveal the key.

The main weakness in the encryption is that when the site is loaded for the first time, i.e without any cookies, it creates an encryption with the **defaultdata**. This is done through a call to **loadData()** which looks at the cookies recived to reconstruct any previous data or return the argument passed. This introducdes to the weakness that without cookies the encryption of **defaultdata** is stored and since we have the clear-text in form of the **defaultdata**, we can reverse the key from it.

Once done, we can enploy the same **xor_encrypt()** function to create a new cookie value with the values changed to reveal the next level password.
