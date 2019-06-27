# Imformation Theoretic Security and The One Time Pad

**Defination of Ciphers**

A cipher is defined over a tuple of sets of all possible key,
all possible message and all possible cipher texts, (K, M, C), 
is a pair of "efficient" algorithms (E, D) where :

- E: K x M $\to$ C, is the encryption algorithm and is often randomized
- D: K x C $\to$ M, is the decryption algorithm and is always deterministic

And the only condition every cipher needs to consider is:
$$
\forall m \in M, k \in K: D(k, E(k, m)) \to m
$$

## The One Time Pad  <small>(Vernam 1917)</small>
The OTP encryption system is basically the _xor_ of the plaintext message M with a key K, which has **the same bit-length as that of the message M**, i.e, <br>
$$ M, C, K \in \{0, 1\}^n $$
where **n** is the **bit-length of the message M** <br>
The encryption algorithm is basically 
$$C := E(K, M) = K \bigoplus M$$
And the decryption algorithm is
$$D := D(K, C) = K \bigoplus C$$


## What is a good cipher? a.k.a <b>Imformation Theoretic Security</b> <small>(Shannon 1949)</small>
Basic Idea is that Cipher Text **should reveal no imformation** about the Plain Text <br>

_Def_: A cipher (**E, D**) over (*K, M, C*) has _**perfect secrecy**_ if <br>
> $\forall m_0, m_1 \in M$

where $[len(m_0) = len(m_1)]$ and

> $\forall c \in C$

$Pr[\exist E[k, m_0] = c] = Pr[\exist E(k, m_1) = c]$

where k is uniform random variable in K

In other word, if as a attacker I have only the cipher c, then the probability that it is _the encryption of m0_ or _the encryption of m1_ **is equal** and thus **the ciphertext in itself reveals no imformation about the plaintext**

Shannon also proved that for any cipher system to have **perfect secrecy**, the _length of key_ $\eqslantgtr$ _length of message_ <br>
$$ \|K\| \eqslantgtr \|M\| $$


## Prove that OTP has perfect secrecy.
Proof
$$
\forall m,c \colon Pr_k[E(k, m) = c ] = \frac{\|k \in K \colon E(k, m) = c\|}{\|K\|}
$$
In other words, the **probability of a message m to be mapped to ciphertext c using a random choice key k** is same **the number of keys that map m to c divided by the total number of keys**

So $\forall m,c \colon \|\{k \in K \colon E(k, m)=c\}\| = const$ (actually 1) <br>
So for all messages m and ciphers c, the number of keys that map m to c is constant, then the probability of m mapping to c using a key k is same, i.e, $\forall m,c \colon Pr_k[E(k, m) = c]$ is same

This proves that OTP has perfect secrecy as any message m<sub>0</sub> and m<sub>1</sub>has the equal probability to map to c, thus giving us no info about the plaintext

$$
if E(K, M) = C
\implies K \bigoplus M = C   \implies K = M \bigoplus C
\implies \|\{k \in K \colon E(k, m) = c\}\| = 1   \forall m, c
$$