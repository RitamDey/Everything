from string import ascii_lowercase


cipher = "llkjmlmpadkkc"
key = "thisisalilkey"


if len(cipher) == len(key):
    print("picoCTF{", end="")
    for i in range(len(cipher)):
        print(ascii_lowercase[
                (ascii_lowercase.find(cipher[i]) - ascii_lowercase.find(key[i])) % 26
                ].upper(), end="")
print("}")
