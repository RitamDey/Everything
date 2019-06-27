# Symmetric Ciphers
Symmetric ciphers are those cipher systems where **the encryptor algorithm and the decryptor algorithm both use the same key for encryption and decryption of the clear text/cipher text**

# Substitution Cipher
A substitution cipher is a form of _weak cipher system_ where **each letter is mapped to another letter using a displacement K, which is acts as the key to the whole encryption system**. Thus, the _strength of the cipher is entirely dependent upon the key space of K_.
- So for example, in a cipher system for 26 letter of English alphabets, the maximum key-space is the **26!**, or the permutation of each 26 letters of the enligsh alphabets.

## Problems with Substitution Ciphers
Substiution Ciphers _suffer from the worst form of cryptanalysis attacks, cipher text only attacks_. Thus if an attacker **has only the cipher, he/she can figure the whole clear text and the encryption key using trial-and-error.**

### Cryptanalysis on substitution ciphers 
Cryptanalysis on substitution ciphers are performed using _Letter Frequencies_.
Thus to figure out the encryption key, we can:
- Analyse how frequent each letter occur in the cipher text and replace it with english letters, that occur around the same frequency, thus making mappings from english letters to shifted letters.
- Analyse pais of letter, digrams and map the commonly occuring digrams in the cipher text with commonly occuring digrams in english text, thus discovering more entries in the tranformation table for the particular substitution encryption.
	
### Examples of Historic Substitution Ciphers
- Vingener Cipher (16th century, Rome): Vingener Cipher is a form of substitution cipher, but here **instead of using a single value key $K$ to form a substitution table, the key $K$ is accepted**. Once the key $K$ is accepted, then it is processed as follows:
	* If the length of key $K$ is smaller than message $M$, then K is replicated till we have a new key $\bar{K}$ which is of the same length as $M$.
	* If the length of key $K$ is same as message $M$, then $K$ is taken as is for the new key $\bar{K}$
	* If the length of key $K$ is more than message $M$, then it is truncated to be of the same length as $M$ and then taken as the new key $\bar{K}$

Once we have $\bar{K}$, the cipher text $C$ is formed as follows
$$
C[i] = (M[i] + K'[i]) \% 26
$$
where i is the position index into $C$, $M$ and $\bar{K}$. Decrypting a Vingener Cipher is just the same as encrytping and thus to decrypt cipher text $C$ into message $M$, we use
$$
M[i] = (C[i] - K'[i])
$$
Vingener Cipher can also be broken using only the letter frequency cipher text attacks and thus like Substitution Ciphers suffers from one the worst kind of cryptanalysis attacks possible.<br><small>** For the cryptanalysis of Vingener Cipher, refer video Lecture-3.mp4 **</small>
