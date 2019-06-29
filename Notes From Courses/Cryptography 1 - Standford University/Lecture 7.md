# Stream Ciphers and Pseudo Random Generators
Shannon proved by his **Bad News Lemma** that even though One Time Pad have the perfect secrecy, the _key needs to be atleast as long as the message_
This is impractical to transfer such long keys securely and might as well be used to used transfer messages
$$
M=C=K=\{0,1\}^n
E(k, m) = k \bigoplus m, D(k, c) = k \bigoplus c
$$

### Stream Ciphers
The main idea and motivation of stream ciphers is to use a **"pseudorandom" key** instead of a **"random" key**

#### Pseudo Random Generator
Pseudo Random Generator or PRG is a function $G: \{0,1\}^s_{seed}$ -> $\{0,1\}^n_{output}$ where $n \gt\gt s$ and has properties:
- Can compute efficiently
- Is an deterministic algorithm
- Ouput should look random
The only thing random in the PRG is the seed that is given as input

To build a stream cipher, we will use out short key $K$ as seed for the PRG function $G$ to generate a pseudo-random key with the same length as the message $G(K)$. That pseudo-random key will be used as key for xor-ing the message $M$ or cipher-text $C$.
In mathematical functions:
$$
C = E(K, M): M \bigoplus G(K)
$$
$$
M = D(K, C): C \bigoplus G(K)
$$

<b> Is a stream cipher perfectly secure? </b>
No, since by defination for a cipher to be perfectly secure, the length of the key needs to be as long as the message is. Since in Stream Cipher, a shorter key is used as seed to procduce the actual key, via PRG, disqualifies it's perfect secrecy.

