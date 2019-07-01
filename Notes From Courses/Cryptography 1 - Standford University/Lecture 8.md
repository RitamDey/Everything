# Attacks on Stream Ciphers and The One Time Pad
Since the **Shanon's defination of perfect secrecy** doesn't holds for Stream Cipher, we can say that the **security of Stream Ciphers depends on the <em>unpredictability of the underlying PRG</em>**

## Attacks on the OTP
Attack when same key is used for multiple encryption

> By defination, one key can be used only once in an OTP encryption system. Reusing the keys breaks all the security promises of the OTP.
<br>$C_1 ← m_1 \bigoplus k$ <br>
$C_2 ← m_2 \bigoplus k$ <br>
> So basically now, if an attacker with $C_1$ and $C_2$ xor's both of them, then they have $m_1 \bigoplus m_2$. Because of the **characteristics of English** and the fact that messages were **encoded using ASCII**, an attacker can derive both of the messages. Historic examples:
> - Project Venona (1941 - 1946)
> - MS-PPTP (Windows NT)
> - 802.11b WEP

Avoid using related keys
> Notable attacks:
> - 802.11b WEP 2001 attack

Stream Ciphers and OTP is malleable
> Stream Ciphers and OTP does not gurantee any integrity of the plaintext message, once it has been encrypted. This just merely provides secrecy. Thus, modifications to ciphertext are undetected and have predictable impact on plaintext. Example

$C ← m \bigoplus k$  
Then the $p$ is $\bigoplus$ to $C$ to essentially form $(m \bigoplus k) \bigoplus p$.  
When decryption is done, the result obtainied is $m \bigoplus p$