# PRG Security Definitions
## Goal
Define what it means that
$$
[k <-^R  K, output: G(K)]
$$
is **"indistinguishable"** from
$$
[r <-^R \{0, 1\}^n, output: r]
$$
,i.e, the generated key, choosen uniformly random from a keyspace K, from the PRG is indistinguishable from the output distribution from a truly random string