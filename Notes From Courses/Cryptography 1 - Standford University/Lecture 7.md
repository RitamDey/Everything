# Stream Ciphers and Pseudo Random Generators
Shannon proved by his **Bad News Lemma** that even though One Time Pad have the perfect secrecy, the _key needs to be atleast as long as the message_
This is impractical to transfer such long keys securely and might as well be used to used transfer messages
$$
M=C=K=\{0,1\}^n
E(k, m) = k \bigoplus m, D(k, c) = k \bigoplus c
$$

### Stream Ciphers
The main idea and motivation of stream ciphers 